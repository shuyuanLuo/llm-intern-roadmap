import os
import platform
import sys


EXPECTED_CONDA_ENV = "llm-intern"
EXPECTED_PYTHON_MAJOR = 3
EXPECTED_PYTHON_MINOR = 11


def choose_device(torch):
    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def main():
    is_python_311 = (
        sys.version_info.major == EXPECTED_PYTHON_MAJOR
        and sys.version_info.minor == EXPECTED_PYTHON_MINOR
    )
    conda_env = os.environ.get("CONDA_DEFAULT_ENV", "")
    in_expected_conda_env = conda_env == EXPECTED_CONDA_ENV

    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    print(f"Python is 3.11.x: {is_python_311}")
    if not is_python_311:
        print(
            "WARNING: Current Python version is not 3.11.x. "
            "This project expects Python 3.11."
        )

    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")
    print(f"CONDA_DEFAULT_ENV: {conda_env or '(not set)'}")
    print(f"Running in llm-intern conda environment: {in_expected_conda_env}")
    if not in_expected_conda_env:
        print(
            "WARNING: Current conda environment is not llm-intern. "
            "Please run: conda activate llm-intern"
        )

    try:
        import torch
    except ImportError:
        print("PyTorch installed: no")
        print(
            "PyTorch is not installed. Please activate llm-intern and install "
            "dependencies from requirements-day0.txt, or use the official PyTorch "
            "installation command."
        )
        return

    print("PyTorch installed: yes")
    print(f"PyTorch version: {torch.__version__}")

    cuda_available = torch.cuda.is_available()
    print(f"CUDA available: {cuda_available}")
    print(f"CUDA device count: {torch.cuda.device_count()}")
    if cuda_available:
        print(f"CUDA device 0: {torch.cuda.get_device_name(0)}")

    mps_available = (
        torch.backends.mps.is_available() if hasattr(torch.backends, "mps") else False
    )
    print(f"MPS available: {mps_available}")

    device = choose_device(torch)
    print(f"Selected device: {device}")

    a = torch.randn(2, 3, device=device)
    b = torch.randn(3, 4, device=device)
    c = a @ b

    print(f"Tensor a shape: {tuple(a.shape)}")
    print(f"Tensor b shape: {tuple(b.shape)}")
    print(f"Matmul result shape: {tuple(c.shape)}")
    print("Matmul result:")
    print(c)


if __name__ == "__main__":
    main()
