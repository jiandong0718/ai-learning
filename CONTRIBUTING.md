# Contributing

这个仓库目前是一个以 AI 应用工程学习、沉淀和 Codex skill 示例为核心的项目。欢迎继续补充内容，但更重要的是保持结构清楚、可复用、可长期维护。

## 适合提交什么

- 新的学习资料索引
- 新的概念笔记
- 新的项目实践记录
- 新的 Codex skill 示例
- 对现有 skill、模板或说明文档的改进

## 提交前建议

1. 先确认新增内容属于哪个目录：
   - `roadmap/`
   - `materials/`
   - `notes/`
   - `skills/`
   - `docs/`
2. 保持命名清楚，避免使用模糊文件名。
3. 尽量写自己的理解，不要只复制资料。
4. 对 skill 类内容，优先保持轻量结构：
   - `SKILL.md`
   - `agents/openai.yaml`
   - `references/`
   - `scripts/`（按需）

## 写 skill 的建议

- `description` 必须同时写清“做什么”和“什么时候用”
- `SKILL.md` 重点写执行流程，不要写成长篇背景说明
- 长资料放到 `references/`
- 固定逻辑再放到 `scripts/`
- 输出规则一定要明确，避免 agent 脑补

推荐先参考：

- [materials/how-to-write-a-codex-skill.md](materials/how-to-write-a-codex-skill.md)
- [materials/skill-template.md](materials/skill-template.md)
- [materials/skill-quality-checklist.md](materials/skill-quality-checklist.md)

## 提交风格

- 小步提交，尽量一次只解决一类问题
- 文档更新尽量保持简洁直接
- 新增 skill 时，优先保证触发清晰、流程可执行、资源有用
- 不要引入和仓库主题无关的内容

## 如果你要新增一个 skill

建议最少包含：

```text
my-skill/
├── SKILL.md
├── agents/openai.yaml
└── references/
```

新增后，最好同步更新：

- [skills/README.md](skills/README.md)
- 根目录 [README.md](README.md)（如果这是一个重要示例）

## License

向本仓库提交内容，即表示你同意这些内容在本仓库的 MIT License 下分发。
