import numpy as np
import math

tolerance = 1e-5

class Qbit():
    def __init__(self, a, b):
        self.state = np.matrix([a, b], dtype=complex).H
        if self._is_valid() == False:
            print(f"The state \n{self.state}\n is invalid for a qbit")
            assert(False)

    def _is_valid(self):
        mag = abs(np.matmul(self.state.H, self.state).item(0))
        if mag - 1 > tolerance:
            return False
        else:
            return True

q0 = Qbit(1,0)
q1 = Qbit(1/math.sqrt(2),1/math.sqrt(2))
q2 = Qbit(0,1)

class ClosedSystem():
    def __init__(self):
