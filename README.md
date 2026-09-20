项目名称：多步决策 Agent 系统（基于 Kaggriculture 模拟环境）
核心架构：纯 Python 实现 Observe → Think → Act 决策循环。
关键技术点：

状态机与条件路由：通过 isinstance 判断土地状态（空地/作物/杂草），路由到 PLANT / WATER / HARVEST / DIG 等不同动作。

资源调度与资金管理：实现了“资金兜底”策略（保证买种子后有余钱），以及基于动态市场价格（>=250 全卖，>=180 卖一半）的囤货与抛售逻辑。

多智能体接口：定义了主 Agent（Farmer）与子 Agent（Hands）的 Action Schema 契约，主 Agent 统管市场交易与资源调度。

防御性编程：使用 .get() 和 or {} 处理环境数据缺失，避免了因 KeyError 导致的 Agent 崩溃。
