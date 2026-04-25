# AI Learning Workspace

一个面向 AI 应用工程师学习和沉淀的仓库，内容包括学习路线、概念笔记、资料索引，以及一组可直接复用的 Codex skills 示例。

## 这是什么

这个仓库用于把 AI 应用工程师相关的学习过程整理成一个可长期维护的项目，而不是零散笔记集合。

这里同时保留 3 类内容：

- 学习路线和阶段目标
- 概念、资料和实践记录
- 可直接复用的 Codex skill 示例

如果你想系统理解 `skill`、`prompt`、`rule`、`MCP`、`RAG` 和 AI 应用工程实践之间的关系，这个仓库就是围绕这些主题持续沉淀的。

## 项目目标

这个仓库的目标不是单纯收集资料，而是把学习路线、方法论和可复用工作流整理成一个长期维护的项目。

目标方向：

1. 从“会用 AI 工具”进阶到“能独立设计和迭代 AI 应用”
2. 把零散学习记录沉淀成结构化概念和项目经验
3. 用真实示例理解 `skill`、`MCP`、`prompt`、`RAG` 等概念
4. 逐步形成自己的 AI 应用工程方法库

## 适合谁

- 想从“会调用模型”走向“会做 AI 应用”的开发者
- 想系统理解 Codex skill 写法和触发方式的人
- 想把学习记录、概念卡片和工作流沉淀成仓库的人
- 想基于中文示例快速上手 AI 应用工程方法的人

## 仓库亮点

- 一份从基础到工程化的 [学习路线](roadmap/ai-application-engineer-roadmap.md)
- 一组可直接参考的 [Codex skills](skills/README.md)
- 一套围绕 skill 编写的模板、检查表和判断指南，位于 `materials/`
- 一组概念笔记，帮助区分 `skills`、`rules`、`MCP`、`prompts`、`RAG`

## 仓库内容

- `roadmap/`
  学习路线、阶段目标、阶段规划
- `materials/`
  学习资料索引、skill 写作模板、质量检查表、概念判断指南
- `notes/`
  概念沉淀、每日学习记录、项目实践记录、阶段日志
- `skills/`
  一组中文 Codex skill 示例，覆盖文档查询、学习整理、功能实现、bug 排查、代码审查、重构和任务总结
- `docs/`
  额外专题文档

## 快速开始

1. 阅读 [roadmap/ai-application-engineer-roadmap.md](roadmap/ai-application-engineer-roadmap.md) 了解整体学习路径。
2. 阅读 [materials/how-to-write-a-codex-skill.md](materials/how-to-write-a-codex-skill.md) 和配套模板，理解 skill 的写法。
3. 查看 [skills/README.md](skills/README.md) 快速浏览当前 skill 列表。
4. 学习过程中持续更新：
   - `materials/resource-index.md`
   - `notes/concepts/`
   - `notes/daily/`
   - `notes/projects/`

## 当前重点

当前主线建议：

1. LLM 基础
2. Prompt 与工作流设计
3. 工具接入与 MCP
4. 后端工程能力
5. RAG 与知识增强
6. Eval、监控与可靠性

## Skills 示例

当前仓库内已经包含这些可直接参考的示例：

- `query-openai-docs`
- `organize-ai-learning-notes`
- `generate-study-plan`
- `daily-learning-review`
- `ai-material-organizer`
- `implement-feature-with-tests`
- `bug-triage`
- `codebase-review`
- `refactor-with-safety`
- `summarize-task-changes`

## 推荐阅读顺序

1. 先看学习路线，建立整体框架
2. 再看 `materials/` 里的 skill 写作模板和检查表
3. 接着浏览 `skills/` 中的具体示例
4. 最后把自己的理解继续沉淀到 `notes/` 中

## 维护原则

- 记录自己的理解，不要只摘抄资料
- 每条笔记尽量回答“是什么、为什么、怎么用”
- 项目记录优先写真实问题和真实取舍
- skill 保持轻量，流程放 `SKILL.md`，细节按需放到 `references/`
- 每周至少做一次阶段复盘

## 适合怎么用

- 作为个人 AI 学习与实践仓库持续维护
- 作为理解 Codex skills 的中文示例仓库
- 作为后续扩展更多项目模板、工程流程和实战案例的基础仓库

## 贡献

欢迎补充：

- 新的中文 skill 示例
- 更清晰的概念解释
- 更实用的学习资料索引
- 项目实践记录和复盘模板

详细说明见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

本仓库使用 [MIT License](LICENSE)。
