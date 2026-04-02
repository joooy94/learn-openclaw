# OpenClaw 架构教程

> 从零理解始终在线的 AI 助手——12 章源码分析，18 万字，普通人也能看懂。

## 这本教程讲什么

**OpenClaw** 是 GitHub 历史上增长最快的开源项目之一（60 天超越 React 十年记录，335K+ 星标）。它是一个**始终在线的个人 AI 助手**——你不说话，它也在干活。它同时连接 WhatsApp、Telegram、Discord、Slack 等 20+ 消息平台，像一个全能管家一样帮你处理邮件、管理日程、查询天气、操作 GitHub。

本教程基于 OpenClaw 的 TypeScript 源码（约 43 万行），用通俗的语言和大量的生活类比，带你从零理解它的架构设计。

## 适合谁读

- **程序员**：想理解多平台 AI 助手的架构设计，学习 TypeScript 大型项目的工程实践
- **非程序员**：对 AI 应用感兴趣，想了解"始终在线的 AI"是怎么做到的
- **创业者/产品经理**：想评估 AI 助手产品的技术可行性

每章都有术语速查表，每个专业术语首次出现时都会用括号标注简单解释。

## 章节目录

### 第一部分：入门

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| 第1章 | [OpenClaw 是什么](01-what-is-openclaw.md) | 始终在线 vs 前景 Agent，龙虾的故事，四层架构 |
| 第2章 | [两个核心原语](02-two-primitives.md) | 自主触发 + 外部记忆，操作系统类比 |
| 第3章 | [三层架构与消息流](03-three-layer-architecture.md) | Gateway/Channel/LLM，7 级路由，完整 8 步消息流 |

### 第二部分：核心机制

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| 第4章 | [System Prompt 与身份系统](04-system-prompt.md) | SOUL/MEMORY/USER/AGENTS.md，优先级链 |
| 第5章 | [Gateway 核心与事件流](05-gateway-core.md) | WebSocket/HTTP，三种 stream，150ms 节流 |
| 第6章 | [Channel 多平台系统](06-channel-system.md) | 适配器模式，提及门控，配对机制 |
| 第7章 | [Session 管理与持久化](07-session-management.md) | 文件锁，磁盘预算，修剪策略 |
| 第8章 | [Skill 与工具系统](08-skills-and-tools.md) | SKILL.md 格式，ClawHub，MCP 协议 |
| 第9章 | [Hook 系统与事件自动化](09-hook-system.md) | 三层管道，4 内置 Hook，Cron 集成 |

### 第三部分：高级特性

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| 第10章 | [Context Engine 与记忆系统](10-context-engine.md) | 向量嵌入，QMD 查询，压缩机制 |
| 第11章 | [安全与审计](11-security-and-audit.md) | 危险工具过滤，Skill Scanner，审计日志 |

### 第四部分：实战

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| 第12章 | [TypeScript 实现最小 Gateway](12-ts-minimal-gateway.md) | 6 步搭建可运行的多通道 Gateway |

## 项目信息

- **总字数**：约 18 万字
- **章节数**：12 章
- **配图**：13 张 Graphviz 架构图
- **源码参考**：OpenClaw（TypeScript，~43 万行）

## 相关项目

- [learn-claude-code](https://github.com/joooy94/learn-claude-code) — Claude Code 源码分析教程（14 章）
