import torch
import torch.nn as nn
import torchvision.models as models

class UNetLike(nn.Module):
    def __init__(self, n_classes=1):
        super().__init__()
        base = models.resnet18(pretrained=True)
        # quick encoder-decoder placeholder
        self.enc = nn.Sequential(*list(base.children())[:-2])
        self.head = nn.Sequential(
            nn.Conv2d(512, 256, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(256, n_classes, 1)
        )

    def forward(self, x):
        x = self.enc(x)
        x = self.head(x)
        return x
