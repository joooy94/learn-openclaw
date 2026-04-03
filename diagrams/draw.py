"""
OpenClaw 教程配图生成器
用法: python3 draw.py <图名>
生成的 PNG 图片保存在 diagrams/ 目录下
"""

import graphviz
import sys
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# -- 配色方案 --
COLORS = {
    "user":      "#4A90D9",   # 蓝色 - 用户/输入
    "llm":       "#7B68EE",   # 紫色 - AI/LLM
    "tool":      "#2ECC71",   # 绿色 - 工具/Skill
    "core":      "#E74C3C",   # 红色 - 核心模块/Gateway
    "data":      "#F39C12",   # 橙色 - 数据/存储/Session
    "security":  "#E67E22",   # 深橙 - 安全/权限
    "channel":   "#1ABC9C",   # 青色 - Channel
    "hook":      "#9B59B6",   # 紫色 - Hook
    "memory":    "#3498DB",   # 亮蓝 - 记忆
    "bg_light":  "#F8F9FA",   # 浅灰背景
    "bg_user":   "#EBF5FB",   # 浅蓝背景
    "bg_llm":    "#F4ECF7",   # 浅紫背景
    "bg_tool":   "#EAFAF1",   # 浅绿背景
    "bg_core":   "#FDEDEC",   # 浅红背景
    "bg_channel":"#E8F8F5",   # 浅青背景
}


def make_dot(name: str, label: str = "", **kwargs) -> graphviz.Digraph:
    """创建一个预配置的 Digraph"""
    dot = graphviz.Digraph(name=name, format="png")
    dot.attr(
        rankdir="LR",
        bgcolor=COLORS["bg_light"],
        fontname="Arial",
        label=label,
        labelloc="t",
        fontsize="20",
        fontcolor="#2C3E50",
        pad="0.5",
        nodesep="0.4",
        ranksep="0.6",
        dpi="300",
        size="15,9",
        ratio="fill",
    )
    return dot


def node(dot, name, label, color, shape="box", fontsize="14"):
    """添加一个带样式的节点"""
    dot.node(
        name,
        label=label,
        shape=shape,
        style="filled,rounded",
        fillcolor=color,
        fontcolor="white",
        fontname="Arial",
        fontsize=fontsize,
        penwidth="0",
        margin="0.2,0.1",
    )


def edge(dot, src, dst, label="", style="solid", color="#7F8C8D"):
    """添加一条带样式的边"""
    dot.edge(
        src, dst,
        label=label,
        color=color,
        fontname="Arial",
        fontsize="11",
        fontcolor="#7F8C8D",
        style=style,
        penwidth="1.5",
    )


def save(dot, name):
    """保存到文件"""
    path = os.path.join(OUTPUT_DIR, name)
    dot.render(path, cleanup=True)
    print(f"[OK] {path}.png")


# == 第1章配图 ==

def ch01_ecosystem():
    """第1章: OpenClaw 生态全景"""
    dot = make_dot("ch01_ecosystem", "OpenClaw 生态全景")
    dot.attr(rankdir="TB", nodesep="0.3", ranksep="0.4")

    # Gateway 核心
    node(dot, "gateway", "Gateway\n核心枢纽\nWebSocket + HTTP\n会话管理 + 事件分发", COLORS["core"])

    # Channels
    with dot.subgraph(name="cluster_channels") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_channel"], label="Channels 消息通道", fontname="Arial", fontsize="13")
        node(c, "whatsapp", "WhatsApp", COLORS["channel"])
        node(c, "telegram", "Telegram", COLORS["channel"])
        node(c, "discord", "Discord", COLORS["channel"])
        node(c, "slack", "Slack", COLORS["channel"])
        node(c, "imessage", "iMessage", COLORS["channel"])
        node(c, "signal", "Signal", COLORS["channel"])

    # Skills
    with dot.subgraph(name="cluster_skills") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_tool"], label="Skills 技能 (50+)", fontname="Arial", fontsize="13")
        node(c, "weather", "天气查询", COLORS["tool"])
        node(c, "github", "GitHub", COLORS["tool"])
        node(c, "notion", "Notion", COLORS["tool"])
        node(c, "spotify", "Spotify", COLORS["tool"])
        node(c, "more", "... 50+ 更多", COLORS["tool"])

    # LLM Providers
    with dot.subgraph(name="cluster_llm") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_llm"], label="LLM Providers", fontname="Arial", fontsize="13")
        node(c, "anthropic", "Anthropic\nClaude", COLORS["llm"])
        node(c, "openai", "OpenAI\nGPT", COLORS["llm"])
        node(c, "ollama", "Ollama\n本地模型", COLORS["llm"])

    # Companion Apps
    with dot.subgraph(name="cluster_apps") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_user"], label="Companion Apps", fontname="Arial", fontsize="13")
        node(c, "ios", "iOS", COLORS["user"])
        node(c, "android", "Android", COLORS["user"])
        node(c, "macos", "macOS", COLORS["user"])

    # 连线
    for ch in ["whatsapp", "telegram", "discord", "slack", "imessage", "signal"]:
        edge(dot, ch, "gateway", "")
    for sk in ["weather", "github", "notion", "spotify", "more"]:
        edge(dot, "gateway", sk, "")
    for llm in ["anthropic", "openai", "ollama"]:
        edge(dot, "gateway", llm, "")
    for app in ["ios", "android", "macos"]:
        edge(dot, app, "gateway", "")

    save(dot, "ch01_ecosystem")


# == 第2章配图 ==

def ch02_two_primitives():
    """第2章: 两个核心原语"""
    dot = make_dot("ch02_two_primitives", "OpenClaw 的两个核心原语")
    dot.attr(rankdir="TB", nodesep="0.4", ranksep="0.5")

    with dot.subgraph(name="cluster_trigger") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_core"], label="原语 1: 自主触发 (Autonomous Invocation)", fontname="Arial", fontsize="14", fontcolor="#2C3E50")
        node(c, "trigger", "trigger -> route -> run\n闹钟响了 -> 找到正确对话 -> 开始干活", COLORS["core"])
        node(c, "cron", "Cron 定时任务\n\"每天早上9点\n看一眼日历\"", COLORS["data"])
        node(c, "heartbeat", "Heartbeat 心跳\n\"每30分钟检查\n有没有新邮件\"", COLORS["llm"])
        node(c, "webhook", "Webhook 外部触发\n\"收到 Gmail\n新邮件通知\"", COLORS["channel"])
        node(c, "voice", "Voice 语音唤醒\n\"Hey Jarvis!\"", COLORS["user"])
        edge(c, "cron", "trigger", "")
        edge(c, "heartbeat", "trigger", "")
        edge(c, "webhook", "trigger", "")
        edge(c, "voice", "trigger", "")

    with dot.subgraph(name="cluster_memory") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_tool"], label="原语 2: 外部记忆 (Externalized Memory)", fontname="Arial", fontsize="14", fontcolor="#2C3E50")
        node(c, "memory_core", "disk = source of truth\ncontext = cache\ncompactor keeps cache bounded", COLORS["tool"])
        node(c, "write", "Write\n把重要信息\n写到磁盘", COLORS["memory"])
        node(c, "retrieve", "Retrieve\n从磁盘找到\n相关笔记", COLORS["memory"])
        node(c, "compact", "Compact\n压缩上下文\n防止爆炸", COLORS["security"])
        edge(c, "write", "memory_core", "")
        edge(c, "retrieve", "memory_core", "")
        edge(c, "compact", "memory_core", "")

    save(dot, "ch02_two_primitives")


def ch02_minimal_arch():
    """第2章: 最小架构三框图"""
    dot = make_dot("ch02_minimal_arch", "最小可行架构: 三个框就够了")
    dot.attr(rankdir="LR", nodesep="0.5", ranksep="0.8")

    node(dot, "triggering", "Triggering\n调度器\n闹钟 + 门铃", COLORS["core"], fontsize="16")
    node(dot, "state", "Persistent State\n持久状态\n笔记本", COLORS["tool"], fontsize="16")
    node(dot, "session", "Session Semantics\n会话语义\n找到正确的对话", COLORS["llm"], fontsize="16")

    edge(dot, "triggering", "session", "触发 -> 找对话")
    edge(dot, "session", "state", "查笔记 -> 干活")
    edge(dot, "state", "triggering", "写笔记 -> 等下次", style="dashed", color=COLORS["data"])

    save(dot, "ch02_minimal_arch")


# == 第3章配图 ==

def ch03_three_layers():
    """第3章: 三层架构"""
    dot = make_dot("ch03_three_layers", "三层架构: Gateway -> Channel -> LLM")
    dot.attr(rankdir="TB", nodesep="0.4", ranksep="0.5")

    # Gateway 层
    with dot.subgraph(name="cluster_gw") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_core"], label="Gateway Layer (快递分拣中心)", fontname="Arial", fontsize="14")
        node(c, "gw_session", "Session 管理\n每个用户一个记录", COLORS["core"])
        node(c, "gw_queue", "消息队列\n排队处理", COLORS["core"])
        node(c, "gw_auth", "认证权限\n谁能用?", COLORS["security"])
        node(c, "gw_ws", "WebSocket\n实时连接", COLORS["core"])

    # Channel 层
    with dot.subgraph(name="cluster_ch") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_channel"], label="Channel Layer (不同快递公司)", fontname="Arial", fontsize="14")
        node(c, "ch_adapter", "适配器模式\n统一消息格式", COLORS["channel"])
        node(c, "ch_route", "路由规则\nDM? 群聊? @?", COLORS["channel"])
        node(c, "ch_event", "事件处理\n收消息/发消息", COLORS["channel"])

    # LLM 层
    with dot.subgraph(name="cluster_llm") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_llm"], label="LLM Layer (翻译官)", fontname="Arial", fontsize="14")
        node(c, "llm_provider", "Provider 接口\n统一调用方式", COLORS["llm"])
        node(c, "llm_tool", "Tool Use\n工具调用", COLORS["llm"])
        node(c, "llm_stream", "流式响应\n打字机效果", COLORS["llm"])

    edge(dot, "ch_adapter", "gw_session", "标准化消息")
    edge(dot, "gw_session", "llm_provider", "发送给 AI")
    edge(dot, "llm_stream", "gw_ws", "流式返回")
    edge(dot, "gw_ws", "ch_event", "发回给用户")

    save(dot, "ch03_three_layers")


def ch03_message_flow():
    """第3章: 完整消息流"""
    dot = make_dot("ch03_message_flow", "一条消息的完整旅程")
    dot.attr(rankdir="TB", nodesep="0.3", ranksep="0.4")

    steps = [
        ("s1", "1. WhatsApp 收到消息\n\"今天天气怎么样?\"", COLORS["channel"]),
        ("s2", "2. Channel 适配器\n转换成统一格式", COLORS["channel"]),
        ("s3", "3. 路由决策\n是 DM? 用户有权限?", COLORS["data"]),
        ("s4", "4. Gateway 分发\n找到用户的 Session", COLORS["core"]),
        ("s5", "5. 组装请求\nSystem Prompt + 历史 + 当前消息", COLORS["llm"]),
        ("s6", "6. LLM 处理\nClaude 思考并生成回复", COLORS["llm"]),
        ("s7", "7. 响应返回\n流式传回 Gateway", COLORS["core"]),
        ("s8", "8. Channel 发送\n\"北京今天晴，25度\"", COLORS["channel"]),
    ]

    for name, label, color in steps:
        node(dot, name, label, color)

    for i in range(len(steps) - 1):
        edge(dot, steps[i][0], steps[i+1][0])

    save(dot, "ch03_message_flow")


# == 第4章配图 ==

def ch04_prompt_layers():
    """第4章: System Prompt 四层构建"""
    dot = make_dot("ch04_prompt_layers", "System Prompt 的四层构建")
    dot.attr(rankdir="TB", ranksep="0.3", size="10,5!")

    node(dot, "soul", "SOUL.md\n人格定义\n\"你叫 Jarvis\n语气要简洁\"", COLORS["core"])
    node(dot, "memory", "MEMORY.md\n长期记忆\n\"用户喜欢中文回复\n每周一有例会\"", COLORS["memory"])
    node(dot, "user", "USER.md\n用户信息\n\"名字: 小王\n时区: UTC+8\"", COLORS["user"])
    node(dot, "agents", "AGENTS.md\n多 Agent 配置\n\"天气 Agent 用 fast 模型\"", COLORS["llm"])

    node(dot, "assembled", "Assembled System Prompt\n组装好的完整 Prompt", COLORS["data"])
    node(dot, "context", "Conversation Context\n对话历史 + 当前消息", COLORS["tool"])
    node(dot, "final", "发送给 LLM\n的完整请求", COLORS["llm"])

    edge(dot, "soul", "assembled", "")
    edge(dot, "memory", "assembled", "")
    edge(dot, "user", "assembled", "")
    edge(dot, "agents", "assembled", "")
    edge(dot, "assembled", "final", "")
    edge(dot, "context", "final", "")

    save(dot, "ch04_prompt_layers")


# == 第5章配图 ==

def ch05_event_stream():
    """第5章: Agent 事件流"""
    dot = make_dot("ch05_event_stream", "Agent 事件流: 三种 stream")
    dot.attr(rankdir="TB", nodesep="0.3", ranksep="0.4")

    node(dot, "agent_run", "Agent 运行\n一次 LLM 调用", COLORS["core"])

    node(dot, "assistant", "assistant stream\nAI 的文字回复\n\"北京今天晴...\"", COLORS["llm"])
    node(dot, "tool", "tool stream\n工具调用\n{phase: start/running/done}", COLORS["tool"])
    node(dot, "lifecycle", "lifecycle stream\n生命周期\n{phase: start/end/error}", COLORS["data"])

    node(dot, "chat_delta", "Chat Delta\n流式推送给客户端\n150ms 节流", COLORS["user"])
    node(dot, "chat_final", "Chat Final\n最终完整回复", COLORS["user"])

    edge(dot, "agent_run", "assistant", "")
    edge(dot, "agent_run", "tool", "")
    edge(dot, "agent_run", "lifecycle", "")
    edge(dot, "assistant", "chat_delta", "emitChatDelta()")
    edge(dot, "lifecycle", "chat_final", "emitChatFinal()")

    save(dot, "ch05_event_stream")


def ch05_chat_streaming():
    """第5章: Chat 流式传输"""
    dot = make_dot("ch05_chat_streaming", "Chat 流式传输: delta -> buffer -> broadcast")
    dot.attr(rankdir="LR", nodesep="0.3", ranksep="0.4")

    node(dot, "delta", "Delta 片段\n\"今天天气\"", COLORS["llm"])
    node(dot, "buffer", "Buffer 缓冲\n\"今天天气很好\"", COLORS["data"])
    node(dot, "throttle", "150ms 节流\n防止刷屏", COLORS["security"])
    node(dot, "broadcast", "Broadcast 广播\n推送给所有连接", COLORS["core"])
    node(dot, "final", "Final 最终\n完整回复", COLORS["user"])

    edge(dot, "delta", "buffer", "追加到缓冲区")
    edge(dot, "buffer", "throttle", "合并文本")
    edge(dot, "throttle", "broadcast", "节流后发送")
    edge(dot, "broadcast", "final", "lifecycle end")

    save(dot, "ch05_chat_streaming")


# == 第6章配图 ==

def ch06_adapter_pattern():
    """第6章: Channel 适配器模式"""
    dot = make_dot("ch06_adapter_pattern", "Channel 适配器模式: 统一接口")
    dot.attr(rankdir="TB", nodesep="0.3", ranksep="0.4")

    node(dot, "standard", "StandardMessage\n{userId, content,\n timestamp, metadata}", COLORS["core"])

    with dot.subgraph(name="cluster_adapters") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_channel"], label="平台适配器", fontname="Arial", fontsize="13")
        node(c, "wa", "WhatsApp\n{from, body, type}", COLORS["channel"])
        node(c, "tg", "Telegram\n{message.chat.id,\n message.text}", COLORS["channel"])
        node(c, "dc", "Discord\n{author.id, content}", COLORS["channel"])
        node(c, "sl", "Slack\n{user, text,\n channel}", COLORS["channel"])

    node(dot, "gateway", "Gateway\n只处理 StandardMessage\n不关心来源平台", COLORS["core"])

    for adapter in ["wa", "tg", "dc", "sl"]:
        edge(dot, adapter, "standard", "adaptMessage()")
    edge(dot, "standard", "gateway", "")

    save(dot, "ch06_adapter_pattern")


# == 第7章配图 ==

def ch07_session_lifecycle():
    """第7章: Session 生命周期"""
    dot = make_dot("ch07_session_lifecycle", "Session 生命周期状态机")
    dot.attr(rankdir="TB", nodesep="0.4", ranksep="0.5")

    node(dot, "create", "创建\n用户首次发消息\nper-channel-peer 隔离", COLORS["core"])
    node(dot, "idle", "空闲 idle\n等待下一条消息", COLORS["data"])
    node(dot, "processing", "处理中\nLLM 正在思考", COLORS["llm"])
    node(dot, "streaming", "流式输出\n正在发送回复", COLORS["channel"])
    node(dot, "archived", "归档\n超过保留期\n写入磁盘", "#95A5A6")
    node(dot, "compact", "压缩\ntoken 太多\n生成摘要", COLORS["security"])

    edge(dot, "create", "idle", "")
    edge(dot, "idle", "processing", "收到消息")
    edge(dot, "processing", "streaming", "LLM 开始输出")
    edge(dot, "streaming", "idle", "回复完成")
    edge(dot, "idle", "archived", "超时未使用")
    edge(dot, "idle", "compact", "token 超限")
    edge(dot, "compact", "idle", "压缩完成")

    save(dot, "ch07_session_lifecycle")


# == 第8章配图 ==

def ch08_skill_lifecycle():
    """第8章: Skill 生命周期"""
    dot = make_dot("ch08_skill_lifecycle", "Skill 生命周期: 发现 -> 加载 -> 执行")
    dot.attr(rankdir="LR", nodesep="0.4", ranksep="0.5")

    node(dot, "discover", "发现\nClawHub 搜索\n或本地 skills/ 目录", COLORS["channel"])
    node(dot, "parse", "解析\n读取 SKILL.md\n提取元数据", COLORS["data"])
    node(dot, "register", "注册\n添加到工具列表\nAI 可以调用", COLORS["core"])
    node(dot, "invoke", "调用\nAI 决定使用\n这个 Skill", COLORS["llm"])
    node(dot, "execute", "执行\n运行脚本\n返回结果", COLORS["tool"])
    node(dot, "result", "结果\n返回给 AI\n继续对话", COLORS["user"])

    edge(dot, "discover", "parse", "")
    edge(dot, "parse", "register", "")
    edge(dot, "register", "invoke", "")
    edge(dot, "invoke", "execute", "")
    edge(dot, "execute", "result", "")

    save(dot, "ch08_skill_lifecycle")


# == 第9章配图 ==

def ch09_hook_chain():
    """第9章: Hook 事件链"""
    dot = make_dot("ch09_hook_chain", "Hook 系统: 事件驱动的自动化")
    dot.attr(rankdir="TB", nodesep="0.3", ranksep="0.4")

    # 事件源
    node(dot, "events", "Gateway 事件总线\n消息/启动/会话变更", COLORS["core"])

    # Hook 类型
    with dot.subgraph(name="cluster_hooks") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_tool"], label="内置 Hook", fontname="Arial", fontsize="13")
        node(c, "boot_md", "boot-md\n启动时执行\n读取 Markdown 指令", COLORS["tool"])
        node(c, "session_mem", "session-memory\n会话记忆\n自动保存重要信息", COLORS["memory"])
        node(c, "cmd_logger", "command-logger\n命令日志\n记录所有操作", COLORS["data"])
        node(c, "gmail", "Gmail Watcher\n邮件监控\n新邮件触发处理", COLORS["hook"])

    # 执行
    node(dot, "executor", "Hook Executor\n执行处理器\n修改上下文", COLORS["security"])

    edge(dot, "events", "boot_md", "")
    edge(dot, "events", "session_mem", "")
    edge(dot, "events", "cmd_logger", "")
    edge(dot, "events", "gmail", "")
    for h in ["boot_md", "session_mem", "cmd_logger", "gmail"]:
        edge(dot, h, "executor", "")

    save(dot, "ch09_hook_chain")


# == 第10章配图 ==

def ch10_memory_arch():
    """第10章: 记忆系统架构"""
    dot = make_dot("ch10_memory_arch", "记忆系统: embeddings + storage + retrieval")
    dot.attr(rankdir="TB", nodesep="0.4", ranksep="0.5")

    # 写入路径
    with dot.subgraph(name="cluster_write") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_user"], label="写入路径", fontname="Arial", fontsize="13")
        node(c, "info", "重要信息\n\"用户喜欢中文\"", COLORS["user"])
        node(c, "embed", "Embeddings\n把文字变成向量\n[0.12, -0.34, ...]", COLORS["memory"])
        node(c, "store", "Storage\n存到磁盘\nMarkdown 文件", COLORS["data"])

    # 读取路径
    with dot.subgraph(name="cluster_read") as c:
        c.attr(style="filled", fillcolor=COLORS["bg_llm"], label="读取路径", fontname="Arial", fontsize="13")
        node(c, "query", "Query 查询\n\"用户喜欢什么语言?\"", COLORS["llm"])
        node(c, "search", "QMD 检索\n向量相似度搜索\n找到相关笔记", COLORS["memory"])
        node(c, "retrieve", "Retrieve\n\"用户喜欢中文回复\"", COLORS["tool"])

    node(dot, "context", "Context Engine\n注册表 + 委托机制\n决定注入哪些记忆", COLORS["core"])

    edge(dot, "info", "embed", "")
    edge(dot, "embed", "store", "")
    edge(dot, "query", "search", "")
    edge(dot, "search", "retrieve", "")
    edge(dot, "store", "context", "")
    edge(dot, "retrieve", "context", "")

    save(dot, "ch10_memory_arch")


# == 第4章新增配图 ==

def ch04_priority_chain():
    """第4章: 身份解析优先级链"""
    dot = make_dot("ch04_priority_chain", "身份解析: 谁说了算？")
    dot.attr(rankdir="TB", nodesep="0.3", ranksep="0.4")

    node(dot, "config", "1. config.json\nui.assistant\n全局配置", COLORS["core"])
    node(dot, "agent", "2. agents 配置\nagents.list[id]\n特定 Agent 配置", COLORS["llm"])
    node(dot, "workspace", "3. workspace 文件\nIDENTITY.md\n工作目录身份", COLORS["channel"])
    node(dot, "default", "4. 默认值\n\"Assistant\"\n兜底", "#95A5A6")
    node(dot, "result", "最终身份\nname + avatar + emoji", COLORS["data"])

    edge(dot, "config", "agent", "未定义?")
    edge(dot, "agent", "workspace", "未定义?")
    edge(dot, "workspace", "default", "未定义?")
    edge(dot, "default", "result", "")

    save(dot, "ch04_priority_chain")


# == 第5章新增配图 ==

def ch05_startup_seq():
    """第5章: Gateway 启动序列"""
    dot = make_dot("ch05_startup_seq", "Gateway 启动序列 (容错设计)")
    dot.attr(rankdir="TB", nodesep="0.25", ranksep="0.3")

    steps = [
        ("s1", "1. 清理锁文件\n防止死锁", COLORS["security"]),
        ("s2", "2. Gmail Watcher\n邮件监控", COLORS["hook"]),
        ("s3", "3. Hook 加载\n内部处理器", COLORS["tool"]),
        ("s4", "4. 模型预热\nprewarm", COLORS["llm"]),
        ("s5", "5. Channel 启动\n连接所有平台", COLORS["channel"]),
        ("s6", "6. Plugin 服务\n扩展功能", COLORS["tool"]),
        ("s7", "7. QMD 记忆后端\n长期存储", COLORS["memory"]),
        ("s8", "8. 就绪!\n开始接受请求", COLORS["core"]),
    ]

    for name, label, color in steps:
        node(dot, name, label, color)

    for i in range(len(steps) - 1):
        edge(dot, steps[i][0], steps[i+1][0])

    # 非阻塞标注
    dot.node("note", "每步独立\n失败不阻塞后续", shape="note", style="filled", fillcolor="#FDEBD0", fontname="Arial", fontsize="11", fontcolor="#7F8C8D")
    edge(dot, "note", "s5", "如 Gmail 失败\nChannel 照常启动", style="dashed", color="#BDC3C7")

    save(dot, "ch05_startup_seq")


# == 第11章新增配图 ==

def ch11_security_layers():
    """第11章: 安全防御分层"""
    dot = make_dot("ch11_security_layers", "安全架构: 多层防御")
    dot.attr(rankdir="TB", nodesep="0.3", ranksep="0.4")

    # 外层
    node(dot, "allowlist", "Allowlist 白名单\n谁能和 AI 对话?\npairing / open / disabled", COLORS["channel"])
    node(dot, "danger", "Dangerous Tools 过滤\n5 + 10 项危险工具\n执行命令/写文件/删文件", COLORS["security"])
    node(dot, "scanner", "Skill Scanner\n安装前扫描\n防止恶意插件", COLORS["tool"])
    node(dot, "external", "External Content\n防 Prompt Injection\n防 SSRF", COLORS["llm"])
    node(dot, "audit", "Audit Log 审计日志\n记录一切操作\n事后追溯", COLORS["data"])
    node(dot, "safe", "Safe Internal\n经过所有防线\n安全执行", COLORS["core"])

    edge(dot, "allowlist", "danger", "")
    edge(dot, "danger", "scanner", "")
    edge(dot, "scanner", "external", "")
    edge(dot, "external", "safe", "")
    edge(dot, "safe", "audit", "记录操作")

    save(dot, "ch11_security_layers")


# == 主入口 ==

ALL_DIAGRAMS = {
    # 第1章
    "ch01_ecosystem": ch01_ecosystem,
    # 第2章
    "ch02_two_primitives": ch02_two_primitives,
    "ch02_minimal_arch": ch02_minimal_arch,
    # 第3章
    "ch03_three_layers": ch03_three_layers,
    "ch03_message_flow": ch03_message_flow,
    # 第4章
    "ch04_prompt_layers": ch04_prompt_layers,
    # 第5章
    "ch05_event_stream": ch05_event_stream,
    "ch05_chat_streaming": ch05_chat_streaming,
    # 第6章
    "ch06_adapter_pattern": ch06_adapter_pattern,
    # 第7章
    "ch07_session_lifecycle": ch07_session_lifecycle,
    # 第8章
    "ch08_skill_lifecycle": ch08_skill_lifecycle,
    # 第9章
    "ch09_hook_chain": ch09_hook_chain,
    # 第10章
    "ch10_memory_arch": ch10_memory_arch,
    # 第4章 (新增)
    "ch04_priority_chain": ch04_priority_chain,
    # 第5章 (新增)
    "ch05_startup_seq": ch05_startup_seq,
    # 第11章 (新增)
    "ch11_security_layers": ch11_security_layers,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 draw.py <diagram_name>")
        print(f"Available: {', '.join(ALL_DIAGRAMS.keys())}")
        print("Or: python3 draw.py all  (generate all)")
        sys.exit(1)

    name = sys.argv[1]
    if name == "all":
        for n, fn in ALL_DIAGRAMS.items():
            fn()
    elif name in ALL_DIAGRAMS:
        ALL_DIAGRAMS[name]()
    else:
        print(f"Unknown diagram: {name}")
        print(f"Available: {', '.join(ALL_DIAGRAMS.keys())}")
        sys.exit(1)


if __name__ == "__main__":
    main()
