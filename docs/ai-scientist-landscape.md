# AI Scientist 与自动化科研：调研及 MySciAgent 取舍

调研日期：2026-10-15。范围：25 项代表性研究、实现与评测，覆盖科研假设、文献、代码复现、实验搜索、协作记忆和验证。以作者论文、官方项目、官方工程文章为来源；这是覆盖主要路线的调研，不是互联网全部项目的穷尽清单。动态仓库版本见 [源码查阅记录](ai-scientist-sources.json)。

## 结论：把研究过程做成有证据的反馈循环

对 MySciAgent 的设计建议：现有应用接入负责取得资料、代码和算力；研究工作流负责状态、交接、实验与证据；专用研究引擎负责单次实现或多轮搜索。三者通过共同的课题和实验协议连接。

```text
已有应用与资源
      ↓
研究问题 → 证据与方法规格 → 假设/方案 → 代码/工具
      ↑                                  ↓
共享研究记录 ← 结论与下一步 ← 独立评测 ← 真实运行
```

这个设计是对下列工作的综合推导。实验得到有效反馈，比增加机器人名称和聊天轮数更接近自动化科研的核心。

## 一、代表性工作地图

### A. 小步实验与程序进化

| 工作 | 实际做什么 | 可借鉴机制 | 适用边界与来源 |
|---|---|---|---|
| Karpathy autoresearch | 在固定的小型 LLM 训练环境中修改代码、运行、比较并继续 | 受限改动范围、固定单次预算、结果账本、保留/舍弃决策 | 针对明确指标的训练探索，不是通用论文到应用平台。[源码与说明](https://github.com/karpathy/autoresearch) |
| Google FunSearch | 由 LLM 提出候选函数，执行评测，再基于优良候选继续搜索 | 程序种群、可计算评分、搜索多样性 | 需要明确可评测的程序问题。[官方实现](https://github.com/google-deepmind/funsearch) |
| Google AlphaEvolve | 用模型集成、自动验证及进化搜索优化算法 | 多模型、候选数据库、评测驱动的选择 | 官方结果仓不是完整引擎。[官方介绍](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)、[结果仓说明](https://github.com/google-deepmind/alphaevolve_results) |
| OpenEvolve | 社区开源的 AlphaEvolve 路线实现 | 候选程序、评估器、种群与并行搜索 | 独立社区项目，不能当作 Google 官方代码。[源码](https://github.com/algorithmicsuperintelligence/openevolve) |
| Sakana ShinkaEvolve | LLM 引导的程序进化与样本效率优化 | 程序档案、模型集成、并行评测、运行/检查入口 | 适合已有可靠 verifier 的代码优化。[源码](https://github.com/SakanaAI/ShinkaEvolve) |

### B. 完整研究流程与科研协作

| 工作 | 实际做什么 | 借鉴点 | 适用边界与来源 |
|---|---|---|---|
| Sakana AI Scientist v1 | 从模板出发生成想法、实验、分析和论文 | 固定基线与明确阶段 | 成功依赖任务和起始模板，不代表任意课题自主研究。[源码](https://github.com/SakanaAI/AI-Scientist)、[论文](https://arxiv.org/abs/2408.06292) |
| Sakana AI Scientist v2 | 减少模板依赖，用实验管理 Agent 和树搜索组织探索 | 多候选实验、实验管理、逐步扩展 | 作者明确提示：更开放的 v2 不保证比模板充分的 v1 成功率高。[源码](https://github.com/SakanaAI/AI-Scientist-v2)、[论文](https://arxiv.org/abs/2504.08066) |
| Google AI co-scientist | 围绕研究目标提出、评议、排序和演化假设 | 假设竞争、反思、证据驱动改进 | 主要参考科学思考机制；不等于能自动执行任意实验。[官方介绍](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) |
| Agent Laboratory | 辅助人类把研究想法推进为文献综述、实验和报告 | 分阶段协作、人工反馈、外部工具 | 更接近个人科研助理的产品体验。[源码](https://github.com/SamuelSchmidgall/AgentLaboratory) |
| AgentRxiv | Agent 实验室共享并检索研究报告 | 研究成果积累、跨任务复用 | 报告共享本身不能保证结论可靠，仍需回到实验。[论文](https://arxiv.org/abs/2503.18102) |
| Microsoft RD-Agent | 将提出研究想法与开发验证连接，面向数据和模型研发 | Hypothesis、Experiment、Feedback 等可分离协议 | 场景化实现，适合作为接口设计参考，不要求整包成为平台核心。[源码](https://github.com/microsoft/RD-Agent) |
| HKUDS AI-Researcher | 覆盖文献、方案、实现、验证、分析与写作 | 研究阶段和可交付成果组织 | 其性能结论属于作者评测，应按目标课题复验。[源码](https://github.com/HKUDS/AI-Researcher)、[论文](https://arxiv.org/abs/2505.18705) |
| Edison Kosmos | 长期科研任务、数据分析、文献与协作，维护研究世界模型 | 持续更新研究认识，长任务与用户反馈 | 本次可见的是产品及工程说明，不是可完整自部署的开源平台。[官方工程说明](https://advances.edisonscientific.com/research/how-we-built-kosmos/) |
| Stanford Virtual Lab | PI Agent、专业科学家 Agent 与人类研究者协作 | 专业分工、研究会议、人类反馈 | 真实实验仍需相应计算工具、实验资源与研究人员。[论文](https://www.nature.com/articles/s41586-025-09442-9) |

### C. 把论文变为代码、工具和可查询证据

| 工作 | 实际做什么 | MySciAgent 用法 | 来源 |
|---|---|---|---|
| Paper2Code / PaperCoder | 规划、实现细节分析、按依赖生成代码仓库 | 没有可复用实现时，生成方法规格和最小实现 | [作者仓库](https://github.com/going-doer/Paper2Code)、[论文](https://arxiv.org/abs/2504.17192) |
| Stanford Paper2Agent | 将论文和研究代码转为经过验证的技能/MCP 工具 | 已有研究代码优先封装为可调用方法，累计个人方法库 | [作者仓库](https://github.com/jmiao24/Paper2Agent)、[论文](https://www.nature.com/articles/s41586-026-11044-y) |
| FutureHouse PaperQA2 | 对科研资料检索、收集证据并生成带引用回答 | 文献证据子流程，不承担实验正确性判断 | [源码](https://github.com/Future-House/paper-qa) |

### D. 机器学习实验执行与搜索

| 工作 | 定位 | 借鉴点 | 来源 |
|---|---|---|---|
| Weco AIDE | 机器学习工程 Agent | draft/debug/improve 与实验 journal，根据运行结果选择下一步 | [源码](https://github.com/WecoAI/aideml) |
| ML-Master | 结合探索与推理进行机器学习工程搜索 | 将候选探索、实现和反馈持续连接 | [论文](https://arxiv.org/abs/2506.16499)、[作者实现](https://github.com/elchulito88/ml-master) |
| Meta AIRA-dojo | 开发和评测 AI research agents 的框架 | 比较搜索、探索、资源与泛化，避免仅展示单个成功案例 | [源码](https://github.com/facebookresearch/aira-dojo)、[论文](https://arxiv.org/abs/2507.02554) |

### E. 衡量能力的基准，不能当作现成应用

| 工作 | 测什么 | 对本项目的启发 | 来源 |
|---|---|---|---|
| MLE-bench | 机器学习工程任务的执行表现 | 用固定任务、数据和算力比较 Agent | [源码](https://github.com/openai/mle-bench) |
| PaperBench | 论文复现，按层次化细项评分 | 将“复现成功”拆成可验收子任务 | [论文](https://arxiv.org/abs/2504.01848) |
| MLR-Bench | 开放式研究的分阶段和端到端评估 | 检查想法、实验和结果的真实性 | [论文](https://arxiv.org/abs/2505.19955) |
| MLRC-Bench | 研究改进任务的客观评估 | 用真实指标检验研究贡献 | [论文](https://arxiv.org/abs/2504.09702) |
| Automated LLM Speedrunning | 在约束下复现 NanoGPT 训练改进 | 固定训练问题与资源，衡量实际改进 | [论文](https://arxiv.org/abs/2506.22419) |

## 二、重点工作的实现方式

### Karpathy：先构造一个足够小的自主实验环境

其核心环境分为固定的数据/评测文件、允许修改的训练文件，以及给编码 Agent 的研究指令。单次训练预算约五分钟，以 val_bpb 比较候选；运行后记录代码版本、指标、显存和保留/舍弃/崩溃状态。直接使用既有编码 Agent 驱动循环。[README](https://github.com/karpathy/autoresearch/blob/master/README.md)、[研究指令](https://github.com/karpathy/autoresearch/blob/master/program.md)

借鉴建议：先固定一个现有科研基线、评测和允许修改的范围。五分钟是这个训练环境的设定，不应硬套到水文或其他长实验。MySciAgent 应设置总预算、停止条件和中断恢复；失败候选也保留记录，避免把工作区回退等同于删除历史证据。

### AlphaEvolve：把生成模型放进可验证的候选搜索系统

系统组合较快模型的广度探索和较强模型的深度建议，生成候选程序，由评测器验证、执行、评分，再将候选和结果存入数据库供下一轮选择。该机制依赖可计算的任务目标。[官方说明](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)、[技术报告](https://arxiv.org/abs/2506.13131)

借鉴建议：优先实现 evaluator 和候选记录，再接进化搜索。目标可以是验证集误差、正确性、运行时间和资源约束；开放式研究问题不能仅凭单一分数判断。官方 alphaevolve_results 明确不提供完整运行代码，OpenEvolve、ShinkaEvolve 应作为独立开源实现分别评估。[官方成果仓](https://github.com/google-deepmind/alphaevolve_results)

### AI co-scientist：让方案经过竞争与修正

Google 的系统围绕目标组织假设生成、反思、排序、演化、相近假设组织和综合评议，并使用竞赛式比较改善候选。它更适合参考科学思考和方案筛选的组织方式。[官方介绍](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)

借鉴建议：让规划步骤给出有差异的候选假设，再按证据、可证伪性、可实施性和资源成本比较。语言模型的排序是实验优先级建议，最终结论仍由相应实验决定。

### Sakana：开放探索需要显式实验管理

v1 围绕模板串联研究阶段；v2 引入实验管理 Agent 和渐进树搜索。公开说明承认更开放不保证更高成功率，因此应按任务条件选择模板复用或开放探索。[v1](https://github.com/SakanaAI/AI-Scientist)、[v2](https://github.com/SakanaAI/AI-Scientist-v2)

借鉴建议：首版由人给研究目标和可靠基线，先跑通有限轮次的实验；结果稳定以后，再启用更开放的候选扩展。论文生成应消费有效结果，不作为实验成功的替代品。

### Paper2Code 与 Paper2Agent：两个不同的复用入口

PaperCoder 的规划、分析和生成阶段输出代码及中间设计产物，适合从论文形成实现。[作者实现](https://github.com/going-doer/Paper2Code)

Paper2Agent 当前入口区分论文知识技能与基于代码的 MCP 工具；工具必须绑定真实仓库代码并完成验证，再交付使用说明与产物。适合把研究方法变为以后可重复调用的能力。[作者实现](https://github.com/jmiao24/Paper2Agent)、[入口工作流](https://github.com/jmiao24/Paper2Agent/blob/main/skills/paper2agent/SKILL.md)

借鉴建议：先找官方或已有实现；能复用时走“代码验证 → 工具封装”，缺实现时才走“论文规格 → 代码生成 → 复现验证”。两条路线最终汇入同一个方法注册表。

### RD-Agent 与 AIDE：用结构化对象承接反馈

RD-Agent 的核心接口区分 Hypothesis、Hypothesis2Experiment 和 HypothesisFeedback，适合参考研究到开发的交接。[接口源码](https://github.com/microsoft/RD-Agent/blob/main/rdagent/core/proposal.py)

AIDE 根据 journal 选择新建、调试或改进候选，执行回调返回结果，再记录到 journal；不是只让多个模型对话。[实现源码](https://github.com/WecoAI/aideml/blob/main/aide/agent.py)

借鉴建议：状态、实验、结果和失败类型必须先结构化。MySciAgent 的工作流可以包住不同引擎，而不是被某个引擎内部格式绑定。

### Kosmos 与 AgentRxiv：研究记忆必须能够被后续任务使用

Kosmos 的官方工程文章强调持续科研任务、研究世界模型、代码执行和人类反馈。它的 world model 不应简单理解为对话历史摘要；本次没有审计其完整内部实现。[工程文章](https://advances.edisonscientific.com/research/how-we-built-kosmos/)

AgentRxiv 研究通过共享和检索报告，让 Agent 实验室利用已有研究继续探索。[论文](https://arxiv.org/abs/2503.18102)

借鉴建议：个人研究记录包含假设、证据、反证、代码、数据、Run 和结论之间的关联；聊天摘要只是入口。过时或未验证的结论必须带状态，不能自动作为新任务的可靠事实。

## 三、对 MySciAgent 的架构建议

应用接入、科研协调和研究引擎分层。现有 Hermes/OpenClaw/编码助手继续作为入口或执行器；可复用的实验引擎通过适配器接入，不要求先同时部署多个完整科研框架。

| 层 | 负责内容 | 第一版选择 |
|---|---|---|
| 资源与应用 | Zotero/PDF、语雀、Git、已有服务器、消息入口 | 使用真实应用及个人仓库；按需求补缺失适配器 |
| 科研协调 | 课题、任务依赖、审批、预算、中断恢复、模型路由 | 一套共享任务和事件协议，避免各入口维护互不相通的事实 |
| 研究引擎 | 单任务实现、候选搜索、复现或工具封装 | 先实现小型预算循环；Paper2Code 与 Paper2Agent 分路；以后按需接一种进化引擎 |
| 运行与评测 | 环境、命令、代码版本、日志、指标、独立验证 | 原始证据和评测器优先，实验在独立工作区运行 |
| 研究积累 | 论文、方法、假设、Run、结论、失败经验 | 可追溯记录，向原笔记应用回写结论与引用 |

多模型分工建议：高能力模型负责难点理解、研究方案和关键审查；DeepSeek 承担适合的实现与整理任务；遇到复杂代码或证据冲突允许升级。不能预先假定所有代码都能由低成本模型完成。AlphaEvolve 的模型组合用于互补探索，不能直接推导出特定供应商的成本或成功率保证。

## 四、实现顺序与验收

1. **固定一个真实基线与评测。** 选择已有代码和数据、算力可承受的课题。完成一次基线 Run；冻结评价协议，明确可修改模块、预算和改进目标。
2. **实现受约束的研究循环。** 候选方案 → 工作区修改 → 测试与运行 → 指标 → 保留/拒绝/修复/升级。记录每次失败与实际耗时、费用；先少量轮次，再增加预算。
3. **接入论文和方法复用。** 建立方法规格与论文引用；已有代码走工具封装，缺少代码走生成与验证。明确论文缺失的假设和实现偏差。
4. **扩大到候选搜索与多 Agent。** 对固定任务、相同模型和总预算比较简单循环与一种搜索引擎；只有收益可验证才保留复杂度。规划、执行、验证、分析围绕同一记录交接。
5. **接回日常工作。** 在真实文献库、笔记、仓库和服务器上跑通整条任务，支持用户中途反馈和恢复，最终将结论及证据写回已有应用。

建议先验证一个现有课题的“读资料 → 提改进 → 改代码 → 小实验 → 比基线 → 写回笔记”。这一主线比一次接入全部应用更容易检验平台是否真有帮助。具体实现任务和接口见 [接入设计](research-engine-integration.md)。

## 五、评价标准与调研限制

| 维度 | 必须回答的问题 |
|---|---|
| 方法正确性 | 实现了论文的哪些设定？哪些是补充假设？单测、参考输出和独立审查证据在哪里？ |
| 实验有效性 | 数据划分、评测器、预算是否一致？是否存在泄漏？小预算候选是否经过完整训练/多种子复验？ |
| 研究真实性 | 每个数字能否定位到 Run、原始文件和代码版本？失败和负结果是否保留？ |
| 自主执行能力 | 同样预算下，完成率、人工接管次数、有效候选比例和恢复能力如何？ |
| 实际价值 | 相比人工流程或单一编码助手，是否减少操作、节省时间或提升有效结果？ |

PaperBench 提供细粒度复现 rubric；MLR-Bench 特别指出其评测中的实验无效/编造成果问题。这些是设定验收协议的依据，不是对当前模型或本项目效果的现成结论。[PaperBench](https://arxiv.org/abs/2504.01848)、[MLR-Bench](https://arxiv.org/abs/2505.19955)

本次未安装、运行、复现上述系统，也没有取得 Kosmos 或 AlphaEvolve 的完整内部平台。作者声称的效果、费用和案例不等于本地可复现结果；源码查阅深度以公开说明和少量核心接口为主。源码目录、模型接口、许可证和算力条件应在实际采用前核对。若开始对比引擎，应锁定源码版本并保存任务、预算和结果。
