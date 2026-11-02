# Claude-Code-GitHub-Actions

> 来源：<https://code.claude.com/docs/en/github-actions>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Claude Code GitHub Actions

官方文档：在 GitHub Actions 中运行 Claude Code（如 PR 审查、自动化任务）。

## 英文正文摘录

Claude Code GitHub Actions is a GitHub Action that runs Claude Code inside your repository’s workflows. Mention
@claude in a pull request or issue comment to have Claude analyze code, implement changes, and push commits. You can also give the Claude Code GitHub Action a prompt to run automatically on any GitHub event. Use it to turn issues into pull requests, fix bugs from a comment, or automate recurring tasks.
Several products share the Claude Code name. This page covers the claude-code-action workflow integration, which you configure with workflow files in your repository. For the related products, see:
- Code Review: automatic review on every pull request, without writing a workflow
- Claude Code in the cloud: Claude Code sessions that run on cloud infrastructure instead of your machine
- Claude Agent SDK: custom automation outside GitHub Actions. The Claude Code GitHub Action is built on the SDK
- GitHub Enterprise Server: Claude Code with self-hosted GitHub
Setup
You can set up the Claude Code GitHub Action in one of two ways:
- Quick setup: run /install-github-app from Claude Code. Claude Code installs the GitHub App, adds your authentication secret, and prepares the workflow pull request for you
- Manual setup: install the app, add the secret, and copy the workflow file into your repository yourself. Use this path when you don’t run Claude Code locally, when the command fails, or when you want full control of the workflow files
For either path, you need admin access to the repository.
Quick setup
/install-github-app works only with github.com repositories. If your repository’s git remote is on gitlab.com or bitbucket.org, the command prints a notice and exits instead of starting setup. To run Claude Code from GitLab pipelines, see Claude Code GitLab CI/CD.
Before you start, install the GitHub CLI and authenticate it with gh auth login. Claude Code checks for it and warns you if it’s missing.
Open claude in the repository you want to connect, run /install-github-app, and follow the prompts. Claude Code installs the Claude GitHub App, then sets up an authentication secret for the workflows:
- If Claude Code already has an API key, it reuses that key, and offers to keep the repository’s existing ANTHROPIC_API_KEY secret if one is already set
- Otherwise, choose between creating a long-lived token with your Claude subscription and pasting in an API key
Claude Code saves the credential as a repository secret, named
ANTHROPIC_API_KEY for an API key or CLAUDE_CODE_OAUTH_TOKEN for a subscription token.
Claude Code then pushes a branch with the workflow files you select, already set to use that secret, and opens GitHub in your browser with a pull request ready to create. Create and merge that pull request, and @claude works in the repository.
To stop setup partway through, press Esc. A step already in progress finishes, and no later step starts. The closing message lists what already happened in the repository, such as a pushed branch or a saved secret.
If you select the review workflow, Claude posts each review on the pull request itself, as an inline comment on each issue it finds or as one summary comment when it finds none. Claude skips some pull requests, such as drafts. The review workflow example uses the same skill and lists them. Before v2.1.229, Claude wrote its review only to the workflow run log.
To update a review workflow that an earlier version generated, do one of the following:
- Run /install-github-app again. When the repository already has a claude.yml, select Update workflow file with latest version. Claude Code pushes fresh copies of the workflow files to a new branch and opens the pull request, the same as a first install.
- Add the --comment argument and the claude_args line from the review workflow example to the checked-in file yourself, which keeps any other edits you made to it.
After installing the GitHub App, Claude Code asks whether to continue with GitHub Actions setup. Choose Skip for now to stop with only the GitHub App installed. Run
/install-github-app again later to finish the workflow and secret steps.
- When you install the GitHub App, you grant it several permissions. See GitHub App permissions for the full set
- Quick setup works with the Claude API and Claude subscriptions. If you use Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry, see Use Claude Code GitHub Actions with cloud providers
Manual setup
To configure the Claude Code GitHub Action without running/install-github-app, install the app, add a secret, and copy a workflow file yourself:
1
Install the Claude GitHub App
Install the Claude GitHub App to your repository. The Claude Code GitHub Action relies on three of the app’s permissions:
- Contents: read and write, so Claude can modify repository files
- Issues: read and write, so Claude can respond to issues
- Pull requests: read and write, so Claude can create PRs and push changes
During installation, you also grant permissions that other C

*[Snapshot truncated for archival size; images omitted.]*
