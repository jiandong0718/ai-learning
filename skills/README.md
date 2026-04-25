# Skills Index

这个目录存放可直接参考的 Codex skill 示例。每个 skill 都尽量保持轻量结构：

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/   # 按需提供
```

## 学习与整理类

- `query-openai-docs`
  查询 OpenAI 官方文档，优先官方来源和官方 MCP
- `organize-ai-learning-notes`
  整理零散学习记录，输出结构化复盘
- `generate-study-plan`
  根据目标、时间和基础生成学习计划
- `daily-learning-review`
  把日常学习内容整理成每日复盘
- `ai-material-organizer`
  整理学习资料、分类主题、评估优先级

## Coding 类

- `implement-feature-with-tests`
  在现有代码库里实现功能并补必要测试
- `bug-triage`
  先定位 bug、缩小范围，再决定是否实施最小修复
- `codebase-review`
  以 findings-first 方式做代码审查
- `refactor-with-safety`
  在保持行为边界的前提下做受控重构
- `summarize-task-changes`
  总结一次任务做了什么、改了哪些文件、多少行代码、涉及哪些类或模块

## 怎么看这些示例

建议优先看每个 skill 的：

1. `SKILL.md`
2. `agents/openai.yaml`
3. `references/` 里的模板和检查清单

如果你想自己写一个新 skill，先看：

- [materials/how-to-write-a-codex-skill.md](../materials/how-to-write-a-codex-skill.md)
- [materials/skill-template.md](../materials/skill-template.md)
- [materials/skill-quality-checklist.md](../materials/skill-quality-checklist.md)
