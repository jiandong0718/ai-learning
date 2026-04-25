先给你一个能建立框架的版本。你这 5 个问题，核心是在区分三层东西：

- rules：给 AI 的长期行为约束
- skills：给 AI 的专项能力包
- MCP：给 AI 接外部工具和数据源的协议/接口

1. Codex 怎么使用 skills
   在你这个环境里，skills 不是“每次手动执行的命令”，更像“会话中的能力包”。

实际使用方式通常是两种：

1. 直接点名技能
   例如你说：用 openai-docs skill 帮我查最新 Responses API 文档
2. 提需求，让系统自动匹配技能
   例如你说：帮我创建一个新 skill
   系统会匹配到 skill-creator

你这个环境里的技能机制，核心是看每个技能目录下的 SKILL.md：

- frontmatter 里有 name 和 description
- 命中后，系统再加载这个 skill 的正文说明
- 如有需要，再继续读取它的 references/、scripts/、assets/

所以你可以把 skills 理解成：
“给 Codex 的专项作业手册 + 可选资源包”。

补一句很重要的现实差异：
我刚查了你当前 codex CLI，这个版本明确有 mcp 子命令，但没有暴露一个单独的 codex
skills ... 命令入口。这说明这里的 skills 更偏“运行时能力机制”，不是 CLI 插件管理命令。

2. Codex 怎么使用 MCP
   MCP 是 Model Context Protocol，本质是让 AI 连接外部工具/数据源的标准方式。

你当前环境里已经配置了这些 MCP 服务：

- context7
- fetch
- memory
- sequential-thinking
- time
- openaiDeveloperDocs

本地我查到的常用命令是：

codex mcp list
codex mcp get openaiDeveloperDocs
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp

两种接法：

1. HTTP MCP

codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp

2. 本地命令启动的 stdio MCP

codex mcp add memory -- npx -y @modelcontextprotocol/server-memory

你可以把 MCP 理解成：
“给 Codex 装手和眼睛”，让它能访问文档、时间、记忆、网页抓取、外部系统等。

3. 如何理解 skills
   最准确的理解是：

skills = 面向任务的能力封装
不是模型本身变聪明了，而是给它一套稳定的工作方法。

一个 skill 通常提供四类东西：

- 专项流程：这个任务应该怎么做
- 领域知识：某个业务、框架、接口的特殊规则
- 工具使用方式：什么情况下调用什么工具
- 资源包：脚本、模板、参考文档

所以 skill 的价值不在“多一段说明”，而在：
它把一个经常做、容易做错、步骤多的任务，变成可复用的套路。

一句话：
rules 管行为，skills 管做事方法。

4. skills 和 rules 有什么区别
   这是最容易混的地方。

rules
是全局约束，告诉 AI：

- 该怎么说话
- 什么能做、什么不能做
- 遇到什么情况必须先确认
- 输出格式、权限边界、风险边界

例如：

- 修改文件必须用 apply_patch
- 搜代码优先用 rg
- 不要乱改用户已有改动

skills
是专项能力包，告诉 AI：

- 遇到某类任务时，按什么流程做
- 该看哪些参考资料
- 哪些脚本和模板能复用

对比记忆法：

- rules = 公司制度 / 安全规范
- skills = 岗位 SOP / 作战手册

再直白一点：

- rules 回答的是：你应该怎么行动
- skills 回答的是：这类事具体怎么做更专业

5. AI 应用工程师，需要会什么技能
   如果你想做“AI 应用工程师”，我建议按下面这 8 块去学。

1. Prompt 设计

- 会写清晰任务指令
- 会做结构化输出
- 会处理 few-shot、角色、约束、长上下文

2. 模型调用与 API

- 会用 OpenAI API / Responses API
- 会处理流式输出、工具调用、错误重试、限流
- 会做模型选型和成本控制

3. Tool Use / MCP / Agent

- 会给模型接工具
- 会设计工具 schema
- 会理解什么时候该让模型“查”、什么时候该让模型“做”

4. RAG

- 分块、embedding、检索、rerank
- 知道“不是所有问题都该微调，很多问题先用 RAG”

5. 后端工程能力

- Python 或 Node 至少熟一门
- API、数据库、队列、缓存、鉴权、日志
- 因为 AI 应用最后还是软件系统

6. 前端/产品落地能力

- 至少能做一个可用的聊天界面或工作台
- 理解用户流程，不只是“把模型接上”

7. 评测与观测

- 会做 eval
- 会看 hallucination、latency、cost、success rate
- 会通过数据迭代 prompt、工具、检索链路

8. 安全与治理

- Prompt injection
- 数据泄露
- 权限隔离
- 人工确认机制
- MCP/插件风险控制

如果你想更接近“能找工作/能做项目”的标准，我建议最低能力模型是：

- 能独立做一个 聊天 + RAG + 工具调用 + 后端接口 + 简单前端
- 能解释为什么这么设计
- 能做基本评测和成本优化

建议你的学习顺序
如果你是从零到一，按这个顺序效率最高：

1. 先学 LLM 基础概念
2. 再学 Prompt
3. 再学 API 调用
4. 再学 RAG
5. 再学 Tool / MCP / Agent
6. 再学评测、安全、工程化

你现在可以立刻记住的三句话

- rules 是约束，skills 是能力包，MCP 是外部工具协议。
- skills 让 Codex“更会做某类事”，MCP 让 Codex“能接触外部世界”。
- AI 应用工程师的本质不是“会聊天模型”，而是“会把模型变成稳定可用的软件能力”。

参考：

- OpenAI Docs MCP: https://platform.openai.com/docs/docs-mcp
- OpenAI MCP 概览: https://platform.openai.com/docs/mcp/overview
- OpenAI Codex: https://platform.openai.com/docs/codex
- OpenAI Code Generation: https://platform.openai.com/docs/guides/code-generation

如果你愿意，我下一步可以直接给你整理一份：
AI 应用工程师 30 天学习路线图
并且按“每天学什么 + 做什么项目”展开。