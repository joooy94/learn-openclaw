# learn_open_claw

OpenClaw 源码分析教程项目，基于 GitHub openclaw/openclaw 仓库。

## 项目状态

正在写一本 12 章的教程，目标 15-20 万字。当前进度：规划完成，开始写第 1 章。

### 章节规划

**入门篇（第 1-3 章）**
- 第1章：OpenClaw 是什么 (`01-what-is-openclaw.md`)
- 第2章：两个核心原语 (`02-two-primitives.md`)
- 第3章：三层架构与消息流 (`03-three-layer-architecture.md`)

**中级篇（第 4-8 章）**
- 第4章：System Prompt 与身份系统 (`04-system-prompt.md`)
- 第5章：Gateway 核心与事件流 (`05-gateway-core.md`)
- 第6章：Channel 多平台系统 (`06-channel-system.md`)
- 第7章：Session 管理 (`07-session-management.md`)
- 第8章：Skill 与工具系统 (`08-skills-and-tools.md`)

**高级篇（第 9-11 章）**
- 第9章：Hook 系统与事件自动化 (`09-hook-system.md`)
- 第10章：Context Engine 与记忆系统 (`10-context-engine.md`)
- 第11章：安全与审计 (`11-security-and-audit.md`)

**实战篇（第 12 章）**
- 第12章：TypeScript 实现最小 Gateway (`12-ts-minimal-gateway.md`)

## 写作风格要求

- **目标读者**: 普通人 + 程序员都能看懂
- **通俗优先**: 每个专业术语首次出现时用括号标注简单解释
- **生活比喻多**: 快递分拣中心、管家、闹钟+笔记本等类比贯穿全文
- **过渡自然**: 知识点之间需要过渡段，不能生硬切换
- **章末有术语速查表**
- **配图用 Graphviz**: `diagrams/draw.py` 生成 PNG，Markdown 中用 `![](diagrams/xxx.png)` 嵌入
- **深度渐进**: 第1-3章入门，4-8章中级（读源码），9-11章高级（算法细节），12章实战
- **核心概念**: 两个核心原语（自主触发 + 外部记忆）贯穿全文

## 排版要求

- 最终可转 PDF 打印，A4 纸
- 图片最大 140mm 宽 x 100mm 高，按比例缩放，居中显示
- draw.py 设置: `size="15,9"`, `dpi="300"`, `ratio="fill"`

## OpenClaw 仓库关键源码

所有源码来自 GitHub openclaw/openclaw，通过 ZRead MCP 读取：

| 文件/目录 | 内容 | 对应章节 |
|-----------|------|---------|
| `src/entry.ts` | CLI 入口，启动流程 | 第3/5章 |
| `src/gateway/server.ts` | Gateway 主服务器 | 第5章 |
| `src/gateway/server-chat.ts` | Chat 流式传输与事件处理 | 第5章 |
| `src/gateway/agent-prompt.ts` | Agent Prompt 构建 | 第4章 |
| `src/gateway/assistant-identity.ts` | 助手身份定义 | 第4章 |
| `src/gateway/boot.ts` | Gateway 启动引导 | 第5章 |
| `src/gateway/server-startup.ts` | 启动序列 | 第5章 |
| `src/channels/` | 消息通道（Discord/Slack/Telegram/WhatsApp/iMessage/Signal） | 第6章 |
| `src/channels/plugins/` | Channel 插件系统 | 第6章 |
| `src/sessions/` | Session ID 解析与生命周期事件 | 第7章 |
| `src/config/sessions/` | Session 持久化存储 | 第7章 |
| `skills/` | 50+ 内置 Skill（SKILL.md） | 第8章 |
| `src/mcp/` | MCP 协议实现 | 第8章 |
| `src/hooks/` | Hook 系统 | 第9章 |
| `src/hooks/bundled/` | 内置 Hook（boot-md/session-memory/command-logger） | 第9章 |
| `src/context-engine/` | Context Engine 核心注册表 | 第10章 |
| `packages/memory-host-sdk/` | Memory Host SDK（embeddings/storage/query） | 第10章 |
| `src/security/` | 安全审计、allowlist、dangerous-tools | 第11章 |
| `src/gateway/auth.ts` | 认证系统 | 第11章 |
| `src/gateway/device-auth.ts` | 设备认证与配对 | 第11章 |
| `src/config/` | 配置系统（Zod schema） | 贯穿全文 |
| `src/routing/` | 消息路由 | 第6章 |
| `src/auto-reply/` | 自动回复系统 | 第9章 |
| `src/cron/` | 定时任务 | 第9章 |

## 关键工具

```bash
cd diagrams
python3 draw.py all              # 重新生成所有配图
python3 draw.py ch01_ecosystem   # 生成指定配图
```

## 参考资源

- [OpenClaw Architecture, Explained (ppaolo)](https://ppaolo.substack.com/p/openclaw-system-architecture-overview)
- [Decoding OpenClaw: Two Simple Primitives (binds.ch)](https://binds.ch/blog/openclaw-systems-analysis)
- [Three-Layer Architecture Deep Dive (eastondev)](https://eastondev.com/blog/en/posts/ai/20260205-openclaw-architecture-guide/)
- [OpenClaw Architecture Overview (official docs)](https://zread.ai/openclaw/openclaw)
