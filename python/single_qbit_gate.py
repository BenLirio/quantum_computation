import numpy as np
import math
class Gate():
    def __init__(self):
        self.vals = (1/math.sqrt(2))*np.array([
            [complex(1,0), complex(1,0)],
            [complex(1,0), complex(-1,0)]
        ])
    def is_valid(self):
        identity = np.matmul(np.transpose(self.vals), self.vals)
        # TODO check use PRECISION
        if identity[0][0] != complex(1,0) or identity[0][1] != complex(0,0) or \
            identity[1][0] != complex(0,0) or identity[1][1] != complex(1,0):
            return False
        else:
            return True

print(Gate().is_valid())
