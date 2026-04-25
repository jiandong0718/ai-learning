# 如何编写 Codex Skill

这份文档只讲最实用的写法，目标不是一次讲全，而是让你能尽快写出第一个可用的 skill。

配套资料：

- [Skill 模板](skill-template.md)
- [Skill 质量检查表](skill-quality-checklist.md)
- [什么时候用 skill、rule、prompt、MCP、RAG](when-to-use-skill-rule-prompt-mcp-rag.md)

## 一、先建立正确理解

skill 不是单独的“功能开关”，而是一套面向某类任务的执行方法。

写 skill 时真正要回答的问题是：

- 哪类任务会反复出现
- 这类任务有哪些固定步骤
- 哪些信息需要稳定提醒给 agent
- 哪些资源应该提前准备好

如果一类任务每次都要临时重新组织思路，就很适合做成 skill。

## 二、一个 skill 最少需要什么

最少只需要一个 `SKILL.md` 文件。

一个较完整的 skill 常见结构如下：

```text
my-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── scripts/
└── assets/
```

各目录的作用：

- `SKILL.md`：核心说明，定义这个 skill 做什么、何时使用、如何执行
- `agents/openai.yaml`：界面和产品侧元数据
- `references/`：详细参考资料
- `scripts/`：可执行脚本
- `assets/`：模板、图片、样板文件等资源

## 三、写 skill 前先做 4 个决定

### 1. 这个 skill 用来处理什么任务

例如：

- 查询 OpenAI 官方文档
- 整理 AI 学习笔记
- 生成学习计划
- 处理某种固定格式文件

### 2. 什么样的用户请求应该触发它

至少写出 3 个真实触发例子。

例如：

- “帮我查一下 OpenAI 官方文档里怎么做结构化输出”
- “把我今天的 AI 学习笔记整理一下”
- “根据我的目标给我做一个 4 周学习计划”

### 3. `description` 里必须写什么

这是最关键的一步。

`description` 要同时写清楚两件事：

- 这个 skill 做什么
- 什么时候应该使用它

如果只在正文里写“什么时候用”，触发阶段看不到，等于没有写。

### 4. 哪些内容应该放到资源目录

判断方法：

- 会反复引用的长资料，放 `references/`
- 会反复执行的固定逻辑，放 `scripts/`
- 会反复复用的模板文件，放 `assets/`

## 四、写 `SKILL.md` 的最小结构

一个最小可用 skill，建议按这个结构写：

```md
---
name: my-skill
description: 写清楚它做什么，以及什么时候使用
---

# 标题

## 概述

用 1 到 2 句话说明它解决什么问题。

## 快速开始

写执行这类任务时最短的 4 到 6 步。

## 工作流程

按步骤写清楚怎么做。

## 输出规则

说明输出时不能犯哪些错。

## 典型触发语句

列出会触发这个 skill 的常见请求。

## 资源

告诉 agent 什么时候读哪个参考文件、用哪个脚本。
```

## 五、写 skill 时最常见的错误

### 1. `description` 写得太短

错误示例：

`description: 帮助总结笔记`

问题：

- 太泛
- 看不出什么时候该触发

更好的写法应该把“任务类型”和“触发场景”一起写进去。

### 2. 把所有细节都塞进 `SKILL.md`

问题：

- 太长
- 浪费上下文
- 不利于按需读取

正确做法：

- 核心流程放 `SKILL.md`
- 长资料放 `references/`

### 3. 只写概念，不写动作

坏 skill 常见的问题是解释很多，但执行时还是不知道下一步做什么。

正文里应该多写动作指令，例如：

- 先阅读原始材料，再下结论
- 先区分事实和推断
- 明确列出未解决的问题

### 4. 没有输出约束

如果不写输出规则，agent 容易：

- 脑补细节
- 过度总结
- 丢失关键术语
- 忽略不确定信息

## 六、当前目录里的 3 个示例

我已经在当前目录创建了 3 个中文示例 skill：

- `ai-learning/skills/query-openai-docs/`
- `ai-learning/skills/organize-ai-learning-notes/`
- `ai-learning/skills/generate-study-plan/`

你可以重点看每个 skill 里的这几个文件：

- `SKILL.md`
- `references/` 下的模板或参考文件
- `agents/openai.yaml`

## 七、自己创建新 skill 的顺序

建议按这个顺序来：

1. 先定义任务类型
2. 写出 3 到 5 条真实触发语句
3. 写 `description`
4. 写“快速开始”和“工作流程”
5. 决定是否需要 `references/`、`scripts/`、`assets/`
6. 用真实请求跑一遍，检查它是不是太空、太泛、太长

## 八、判断一个 skill 是否合格

用这 3 个问题判断：

1. 别的 agent 拿到它后，能不能立刻知道什么时候用
2. 进入 skill 后，能不能立刻知道下一步做什么
3. 做完任务后，输出质量会不会明显比“没有 skill”更稳定

如果这 3 个问题大多都能回答“能”，这个 skill 就已经合格了。
