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
  environment.yml
```

## Day 0 完成内容

- 创建项目结构
- 创建 Conda + Python 3.11 环境说明
- 创建 requirements-day0.txt
- 创建 environment.yml
- 创建环境验证脚本
- 记录本机环境
- 初始化 Git

## Conda 环境

本项目统一使用 Conda 环境 `llm-intern`，不使用系统 Python 3.9，也不使用 `.venv`。

环境要求：

- 环境名：`llm-intern`
- Python 版本：3.11.x

创建环境：

```bash
conda create -n llm-intern python=3.11 -y
```

激活环境：

```bash
conda activate llm-intern
```

检查 Python：

```bash
python --version
```

期望输出：

```text
Python 3.11.x
```

如果 `llm-intern` 环境已经存在但不是 Python 3.11，可以尝试：

```bash
conda install -n llm-intern python=3.11 -y
```

如果升级失败，请手动确认是否删除并重建环境。

也可以根据 `environment.yml` 创建环境：

```bash
conda env create -f environment.yml
```

## 安装 Day 0 依赖

在已激活 `llm-intern` 后执行：

```bash
python -m pip install --upgrade pip
pip install -r requirements-day0.txt
```

或者不依赖当前 shell 激活状态，直接使用：

```bash
conda run -n llm-intern python -m pip install --upgrade pip
conda run -n llm-intern python -m pip install -r requirements-day0.txt
```

## Jupyter Kernel

在 `llm-intern` 环境中注册 Jupyter kernel：

```bash
python -m ipykernel install --user --name llm-intern --display-name "Python (llm-intern)"
```

以后打开 Jupyter Notebook / JupyterLab 时，选择 kernel：

```text
Python (llm-intern)
```

## PyTorch GPU 安装说明

如果 CPU 版 PyTorch 能正常运行，Day 1 可以继续。

如果需要 NVIDIA GPU 版 PyTorch，不要手动猜 CUDA 命令，请去 PyTorch 官方 Start Locally 页面选择适合当前系统、包管理器、Python 版本和 CUDA 版本的安装命令。

## 环境检查

先激活 Conda 环境：

```bash
conda activate llm-intern
python 00_setup/check_env.py
```

或者不依赖当前 shell 激活状态：

```bash
conda run -n llm-intern python 00_setup/check_env.py
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
- [Conda 用户指南](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html)
- [Git 官方文档](https://git-scm.com/doc)
