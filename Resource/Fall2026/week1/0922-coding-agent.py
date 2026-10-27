import inspect
import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import List, Dict, Any, Tuple
from pathlib import Path

load_dotenv()

openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are a helpful coding assistant whose goal is to help complete coding tasks. 
You have access to a series of tools you can execute. Here are the tools you have access to:

{tool_list_str}

When you want to use a tool reply with exactly one line in the format: 'tool: TOOL_NAME({{JSON_ARGS}})' and nothing else.
Use compact single-line JSON with double quotes. After receiving a tool_result(...) message, continue the task.
If no tool is needed, respond normally.
"""

YOU_COLOR = "\u001b[94m"
ASSISTANT_COLOR = "\u001b[93m"
RESET_COLOR = "\u001b[0m"

def resolve_abs_path(path_str: str) -> Path:
    path = Path(path_str).expanduser()
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    return path

def read_file_tool(filename: str) -> Dict[str, Any]:
    """
    Gets the full content of a file provided by the user.
    :param filename: The name of the file to read.
    :return: The full content of the file.
    """
    full_path = resolve_abs_path(filename)
    print(full_path)
    with open(str(full_path), "r") as f:
        content = f.read()
    return {
        "file_path": str(full_path),
        "content": content
    }

def list_files_tool(path: str) -> Dict[str, Any]:
    """
    Lists the files in a directory provided by the user.
    :param path: The path to the directory to list files from.
    :return: A list of files in the directory.
    """
    full_path = resolve_abs_path(path)
    all_files = []
    for item in full_path.iterdir():
        all_files.append({
            "filename": item.name,
            "type": "file" if item.is_file() else "dir"
        })
    return {
        "path": str(full_path),
        "files": all_files
    }

def edit_file_tool(path: str, old_str: str, new_str: str) -> Dict[str, Any]:
    """
    Replaces first occurrence of old_str with new_str in file. If old_str is empty, creates/overwrites file with new_str.
    :param path: The path to the file to edit.
    :param old_str: The string to replace.
    :param new_str: The string to replace with.
    :return: A dictionary with the path to the file and the action taken.
    """
    full_path = resolve_abs_path(path)
    p = Path(full_path)
    if old_str == "":
        p.write_text(new_str, encoding="utf-8")
        return {
            "path": str(full_path),
            "action": "created_file"
        }
    original = p.read_text(encoding="utf-8")
    if original.find(old_str) == -1:
        return {
            "path": str(full_path),
            "action": "old_str not found"
        }
    edited = original.replace(old_str, new_str, 1)
    p.write_text(edited, encoding="utf-8")
    return {
        "path": str(full_path),
        "action": "edited"
    }

TOOL_REGISTRY = {
    "read_file": read_file_tool,
    "list_files": list_files_tool,
    "edit_file": edit_file_tool
}

def get_tool_str_representation(tool_name: str) -> str:
    tool = TOOL_REGISTRY[tool_name]
    return f"""
    Name: {tool_name}
    Description: {tool.__doc__}
    Signature: {inspect.signature(tool)}
    """

def create_full_system_prompt() -> str:
    tool_str_repr = ""
    for tool_name in TOOL_REGISTRY:
        tool_str_repr += "TOOL\n===" + get_tool_str_representation(tool_name)
        tool_str_repr += f"\n{"="*15}\n"
    return SYSTEM_PROMPT.format(tool_list_str=tool_str_repr)

def extract_tool_invocations(text: str) -> List[Tuple[str, Dict[str, Any]]]:
    """Return list of (tool_name, args) requested in 'tool: name({...})' lines.

    The parser expects single-line, compact JSON in parentheses.
    """
    invocations: List[Tuple[str, Dict[str, Any]]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("tool:"):
            continue
        # Expected format: tool: NAME(JSON)
        try:
            after = line[len("tool:") :].strip()
            name, rest = after.split("(", 1)
            name = name.strip()
            args, _ = json.JSONDecoder().raw_decode(rest)
            invocations.append((name, args))
        except Exception:
            # Ignore malformed tool requests
            continue
    return invocations

def execute_llm_call(conversation: List[Dict[str, str]]) -> str:
    response = openai_client.responses.create(
        model="gpt-5.6-terra",
        input=conversation,
        max_output_tokens=5000,
    )
    return response.output_text

def run_coding_agent_loop():
    conversation = [{
        "role": "developer",
        "content": create_full_system_prompt()
    }] 
    while True:
        try:
            user_msg = input(f"{YOU_COLOR}You{RESET_COLOR}: ")
        except (EOFError, KeyboardInterrupt):
            break
        conversation.append({
            "role": "user",
            "content": user_msg.strip()
        })
        while True:
            assistant_resp = execute_llm_call(conversation)
            tool_invocations = extract_tool_invocations(assistant_resp)
            if not tool_invocations:
                print(f"{ASSISTANT_COLOR}Assistant{RESET_COLOR}: {assistant_resp}")
                conversation.append({
                    "role": "assistant",
                    "content": assistant_resp
                })
                break
            print(f"{ASSISTANT_COLOR}Assistant{RESET_COLOR}: {assistant_resp}")
            conversation.append({
                "role": "assistant",
                "content": assistant_resp
            })
            for name, args in tool_invocations:
                tool = TOOL_REGISTRY[name]
                resp = []
                if name == "read_file":
                    resp = tool(args.get("filename", "."))
                elif name == "list_files":
                    resp = tool(args.get("path", "."))
                elif name == "edit_file":
                    resp = tool(args.get("path", "."), args.get("old_str", ""), args.get("new_str", ""))
                conversation.append({
                    "role": "user",
                    "content": f"tool_result({json.dumps(resp)})"
                })
            


if __name__ == "__main__":
    run_coding_agent_loop()