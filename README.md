# llm-intern-roadmap

## 项目目标

这是一个面向大模型算法 / 应用算法 / 推理部署 / RAG Agent 方向实习准备的 28 天学习仓库。目标覆盖：

- PyTorch 基础
- Transformer from scratch
- LLM 架构和训练目标
- 分布式训练基础
- LoRA / SFT
- RL 后训练入门
- vLLM 推理部署
- RAG / Agent 项目

## 当前阶段

当前是 Day 0：环境和仓库准备。今天只确认本机基础环境、创建项目结构、准备最小依赖和验证脚本，不实现 Day 1 训练代码。

## 目录结构

```text
llm-intern-roadmap/
  00_setup/                       # 环境检查脚本和第 0 天准备材料
  01_pytorch_basics/              # Day 1 PyTorch 基础练习
  02_transformer_from_scratch/    # Transformer from scratch 学习代码
  03_llm_architecture_notes/      # LLM 架构和训练目标笔记
  04_distributed_training_notes/  # 分布式训练基础笔记
  05_lora_sft_project/            # LoRA / SFT 小项目
  06_rl_post_training_verl/       # RL 后训练入门材料
  07_vllm_serving/                # vLLM 推理部署练习
  08_rag_agent_project/           # RAG / Agent 项目
  notes/                          # 每日环境、学习和排错记录
  interview/                      # 面试复盘、八股和项目表达材料
  outputs/                        # 实验输出和模型产物，不提交大文件
  README.md
  .gitignore
  requirements-day0.txt
```

## Day 0 完成内容

- 创建项目结构
- 创建 Python 虚拟环境说明
- 创建 requirements-day0.txt
- 创建环境验证脚本
- 记录本机环境
- 初始化 Git

## Python 虚拟环境

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

安装 Day 0 / Day 1 最小依赖：

```bash
pip install -r requirements-day0.txt
```

如果你使用 NVIDIA GPU，但不确定 CUDA 与 PyTorch 版本如何匹配，不要手动猜安装命令。请到 PyTorch 官方 Start Locally 页面选择对应系统、pip/conda、Python 和 CUDA 版本后，再使用官方生成的安装命令。

## 如何运行环境检查

```bash
python 00_setup/check_env.py
```

如果系统默认命令是 `python3`：

```bash
python3 00_setup/check_env.py
```

## 后续 Day 1 预告

- Tensor 基础
- autograd
- nn.Module
- optimizer / loss / backward / step
- 第一个 MLP 分类器

## 参考材料

- [PyTorch Start Locally](https://pytorch.org/get-started/locally/)
- [PyTorch Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)
- [Python venv 官方文档](https://docs.python.org/3/library/venv.html)
- [Git 官方文档](https://git-scm.com/doc)
