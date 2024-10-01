"""Neural network architecture for multivariate sEMG timeseries learning."""


import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

from . import spdNN

class manifoldNet(nn.Module):
    def __init__(self, classifications):
        super(manifoldNet, self).__init__()
        
        self.re = spdNN.ReEig()
        self.bimap1 = spdNN.BiMap(1, 12, 12)
        self.bimap2 = spdNN.BiMap(1, 12, 11)

        self.logeig = spdNN.LogEig()

        self.linear1 = nn.Linear(11 * 11, classifications)

    def forward(self, x):
        
        x = self.re(self.bimap1(x))
        x = self.re(self.bimap2(x))
        x = self.logeig(x).view(x.shape[0], -1)
        x = self.linear1(x)
        return x


class learnSPDMatrices(nn.Module):
    def __init__(self, classifications):
        super(learnSPDMatrices, self).__init__()
        
        self.snn = manifoldNet(classifications)

    def forward(self, x):
        x = x.unsqueeze(1)
        
        x = self.snn(x)
        return x
