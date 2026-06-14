import platform
import sys


def choose_device(torch):
    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def main():
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")

    try:
        import torch
    except ImportError:
        print("PyTorch installed: no")
        print(
            "PyTorch is not installed. Please install dependencies from "
            "requirements-day0.txt or use the official PyTorch installation command."
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
