import torch

if torch.cuda.is_available():
    print("CUDA is available. PyTorch can use the GPU!")
    print(f"Number of GPUs detected: {torch.cuda.device_count()}")
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")


    device = torch.device("cuda") 
    tensor = torch.rand(3, 3).to(device)  
    print("Tensor successfully created on GPU:")
    print(tensor)
else:
    print("CUDA is not available. PyTorch will use the CPU.")
