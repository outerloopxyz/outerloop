import torch

class CDist1d(torch.nn.Module):
    def forward(self, x):
        assert isinstance(x, tuple)
        x1, x2 = x
        d = x2.unsqueeze(-3) - x1.unsqueeze(-2)
        return d.abs_()


__all__ = [
    "CDist1d",
]
