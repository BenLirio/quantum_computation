import math

PRECISION = 1e-5

class Qbit:
    def __init__(self):
        self.vals = [complex(math.sqrt(2)/2,0), complex(math.sqrt(2)/2,0)]
    def is_valid(self):
        if sum([abs(v)**2 for v in self.vals]) - 1.0 < PRECISION:
            return True
        else:
            print(sum([abs(v)**2 for v in self.vals]))
            return False
    def __str__(self):
        return '['+', '.join([f"({round(v.real,2)}, {round(v.imag,2)}j)" for v in self.vals])+']'

