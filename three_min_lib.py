import torch

class three_min:
    @staticmethod
    def print_tensor(tensor):
        print("size:", tensor.size())
        print("shape:", tensor.shape)
        print("랭크(차원):", tensor.ndimension())
