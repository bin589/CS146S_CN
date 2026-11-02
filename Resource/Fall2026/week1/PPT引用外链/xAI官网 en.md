# x.ai homepage snapshot

> 来源：<http://x.ai>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
> Product/marketing homepage snapshot only.
for everything you
build.
Reasoning, code, voice, images, and video. 
Trained on the world's largest supercluster.
Explain quantum entanglement simply
Two particles become linked — measuring one instantly determines the other, regardless of distance.
Why is the sky blue?
Shorter blue wavelengths scatter more off air molecules than longer red ones.
How do black holes form?
ChatExplore →
projects/main
|11.60%|
❯Migrate auth from sessions to JWT.
Thinking...
▸ read_filesrc/middleware/auth.ts68 lines
▸ grep"session" src/4 matches
▸ read_filesrc/lib/jwt.ts42 lines
|Audit auth middlewareexplore
[running]
|Design token rotationgeneral
[running]
|Find session referencesexplore
[done]
Thought for 4.1s
Editsrc/middleware/auth.ts
42export async function handler(req) {
43  const token = extractBearer(req);
BuildExplore →
BotExplore →
ImagineExplore →
VoiceExplore →
For developers
Every modality.
Text, code, voice, images, and video — all through a single unified API. Start building in seconds.
1M+
API calls per day
<200ms
Median latency
5+
Model families
- 300300 M+
- queries processed daily
- 150150 K
- GPUs in
Launch your AI-powered product with:
- Access to all Grok models
- Usage-based pricing
- Automatically increasing rate limits
- Comprehensive documentation and guides
Custom rate limits and hands-on support for your team.
- Dedicated onboarding support
- Custom rate limits
- Billing via monthly invoices
- Single sign-on and audit logging
- Data residency options
