# Day 0 环境搭建记录

## 1. 本机环境

- 操作系统：macOS 26.1, Build 25B78, Darwin 25.1.0, arm64
- Python 版本：系统默认 `python3` 为 Python 3.14.6；本项目 `.venv` 使用 `/usr/bin/python3` 创建，为 Python 3.9.6
- pip 版本：系统默认 pip 26.1.2；本项目 `.venv` 中 pip 已升级到 26.0.1
- Git 是否可用：可用，git version 2.50.1 (Apple Git-155)
- NVIDIA GPU / nvidia-smi：`nvidia-smi` 不存在，未检测到 NVIDIA GPU；本机显示芯片为 Apple M2 GPU
- PyTorch 是否安装：已在 `.venv` 中安装；系统默认 Python 3.14.6 中未安装 PyTorch
- PyTorch 版本：2.8.0
- CUDA 是否可用：False
- MPS 是否可用：False；`torch.backends.mps.is_built()` 为 True，但 `torch.backends.mps.is_available()` 为 False
- 当前推荐 device：cpu

`00_setup/check_env.py` 运行摘要：

```text
Python version: 3.9.6
Platform: macOS-26.1-arm64-arm-64bit
Machine: arm64
PyTorch installed: yes
PyTorch version: 2.8.0
CUDA available: False
CUDA device count: 0
MPS available: False
Selected device: cpu
Tensor a shape: (2, 3)
Tensor b shape: (3, 4)
Matmul result shape: (2, 4)
```

## 2. 已创建的目录

```text
llm-intern-roadmap/
  00_setup/
    check_env.py
  01_pytorch_basics/
    .gitkeep
  02_transformer_from_scratch/
    .gitkeep
  03_llm_architecture_notes/
    .gitkeep
  04_distributed_training_notes/
    .gitkeep
  05_lora_sft_project/
    .gitkeep
  06_rl_post_training_verl/
    .gitkeep
  07_vllm_serving/
    .gitkeep
  08_rag_agent_project/
    .gitkeep
  notes/
    day0_setup.md
  interview/
    .gitkeep
  outputs/
    .gitkeep
  README.md
  .gitignore
  requirements-day0.txt
```

## 3. 已安装或计划安装的依赖

已在 `.venv` 中安装 `requirements-day0.txt` 的依赖：

- numpy：数值计算
- pandas：表格数据处理
- matplotlib：画图
- jupyter：交互式实验
- ipykernel：Jupyter kernel
- tqdm：进度条
- scikit-learn：传统机器学习和数据划分工具
- torch：PyTorch 核心库
- torchvision：视觉相关扩展，当前不是重点，但常和 torch 一起安装
- torchaudio：音频相关扩展，当前不是重点，但常和 torch 一起安装

## 4. 今天必须理解的概念

- 虚拟环境：项目专用的 Python 运行环境。它把依赖安装在当前项目目录下，避免污染系统 Python，也避免不同项目的包版本互相影响。
- pip：Python 包管理工具。常用来安装、升级、卸载依赖，例如 `pip install -r requirements-day0.txt`。
- PyTorch：深度学习框架。它提供 Tensor、自动求导、神经网络模块、优化器和 GPU/MPS 加速能力。
- Tensor：多维数组，是 PyTorch 里的基础数据结构。标量、向量、矩阵和更高维数据都可以表示为 Tensor。
- CPU / GPU：CPU 通用性强，适合控制逻辑和小规模计算；GPU 并行能力强，适合大规模矩阵运算和深度学习训练。
- CUDA：NVIDIA GPU 的并行计算平台。只有 NVIDIA GPU 和匹配的驱动 / PyTorch 版本可用时，PyTorch 才能使用 CUDA。
- MPS：Apple Silicon 上的 Metal Performance Shaders 后端。它让 PyTorch 在部分 macOS + Apple 芯片环境中使用 Apple GPU。
- Git commit：Git 中的一次版本快照。提交前先 `git add` 选择文件，再 `git commit` 记录变更。
- requirements.txt：Python 依赖清单。别人拿到项目后，可以用 `pip install -r requirements.txt` 安装相同依赖。
- .gitignore：告诉 Git 哪些文件不要追踪，例如虚拟环境、缓存、模型权重和本地密钥文件。

## 5. 遇到的问题

- 问题现象：使用 Homebrew Python 3.14 创建 `.venv` 时，`ensurepip` 失败，虚拟环境没有 pip。
- 报错信息：`ImportError: Symbol not found: _XML_SetAllocTrackerActivationThreshold`，出现在 `pyexpat` 加载 `/usr/lib/libexpat.1.dylib` 时。
- 初步判断：本机 Homebrew Python 的 `pyexpat` 与系统 `libexpat` 动态库存在兼容问题。Homebrew Python 3.11 也出现同类问题。
- 建议下一步：当前项目已改用系统 `/usr/bin/python3` 创建 `.venv` 并完成依赖安装。后续如果要修复 Homebrew Python，可考虑更新 Homebrew 及相关库，但这不是 Day 0 必须项。

- 问题现象：第一次执行 `pip install -r requirements-day0.txt` 失败。
- 报错信息：`Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known`。
- 初步判断：初次运行处于受限网络环境，pip 无法解析 PyPI。
- 建议下一步：已通过授权网络重试并安装成功。

- 问题现象：本机是 Apple M2，但 PyTorch 报告 MPS 不可用。
- 报错信息：无报错；`torch.backends.mps.is_built()` 为 True，`torch.backends.mps.is_available()` 为 False。
- 初步判断：当前 PyTorch 构建包含 MPS 后端，但运行时判定不可用。Day 0 不继续排查 GPU/MPS，当前使用 CPU 即可。
- 建议下一步：Day 1 先用 CPU 完成基础训练；需要 MPS 时再单独排查 macOS、Python 和 PyTorch 组合。

## 6. Day 0 验收清单

- [x] 项目目录已创建
- [x] Conda 环境说明已写入 README
- [x] requirements-day0.txt 已创建
- [x] check_env.py 已创建
- [x] check_env.py 已运行
- [x] notes/day0_setup.md 已完成
- [x] .gitignore 已创建
- [x] Git 仓库已初始化
- [x] Day 0 commit 已完成

## Conda Python 3.11 环境改造记录

本节记录后续增量改造结果。原 `.venv` 记录仅作为历史信息保留；从本节开始，本项目统一使用 Conda 环境。

- 我的系统 Python 是 3.9
- 本项目不使用系统 Python 3.9
- 本项目统一使用 Conda 环境 `llm-intern`
- `llm-intern` 使用 Python 3.11
- 后续所有命令必须先 `conda activate llm-intern`
- 如果 Codex 或终端不能保持激活状态，可以使用 `conda run -n llm-intern`

实际检查结果：

- conda 是否可用：可用
- conda 版本：conda 24.11.0
- llm-intern 环境是否存在：存在，路径为 `/opt/anaconda3/envs/llm-intern`
- llm-intern Python 版本：Python 3.11.15
- 当前 python 路径：`/opt/anaconda3/envs/llm-intern/bin/python`
- 当前 pip 路径：`/opt/anaconda3/envs/llm-intern/bin/pip`
- 是否误用系统 Python 3.9：没有，依赖安装和验证均使用 `conda run -n llm-intern`
- PyTorch 是否安装：已安装
- PyTorch 版本：2.12.0
- CUDA 是否可用：False
- MPS 是否可用：False
- 当前推荐 device：cpu
- Jupyter kernel 是否注册成功：成功，kernel 名为 `Python (llm-intern)`，安装位置为 `/Users/luoluoluo/Library/Jupyter/kernels/llm-intern`

环境创建和依赖安装记录：

- 首次执行 `conda create -n llm-intern python=3.11 -y` 失败，因为当前 Conda 配置里的 `https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free` 返回 HTTP 403。
- 未修改全局 Conda 配置，改用 `conda create -n llm-intern python=3.11 -y --override-channels -c defaults` 临时指定官方 `defaults` channel，创建成功。
- 已执行 `conda run -n llm-intern python -m pip install --upgrade pip`。
- 已执行 `conda run -n llm-intern python -m pip install -r requirements-day0.txt`。
- 已执行 `conda run -n llm-intern python -m ipykernel install --user --name llm-intern --display-name "Python (llm-intern)"`。

`conda run -n llm-intern python 00_setup/check_env.py` 输出摘要：

```text
Python executable: /opt/anaconda3/envs/llm-intern/bin/python
Python version: 3.11.15
Python is 3.11.x: True
Platform: macOS-26.1-arm64-arm-64bit
CONDA_DEFAULT_ENV: llm-intern
Running in llm-intern conda environment: True
PyTorch installed: yes
PyTorch version: 2.12.0
CUDA available: False
CUDA device count: 0
MPS available: False
Selected device: cpu
Tensor a shape: (2, 3)
Tensor b shape: (3, 4)
Matmul result shape: (2, 4)
```

Conda 常用命令：

```bash
conda info --envs
conda create -n llm-intern python=3.11 -y
conda activate llm-intern
conda deactivate
conda run -n llm-intern python --version
conda run -n llm-intern python 00_setup/check_env.py
conda env export > environment-full.yml
```
