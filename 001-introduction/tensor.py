from cgi import test
from heapq import heapify
import numpy as np

class Tensor:
    
    @classmethod
    def zeros(cls, *args: int) -> np.ndarray:
        return np.zeros(args, dtype=np.float32)
    
    @classmethod
    def ones(cls, *args: int) -> np.ndarray:
        return np.ones(args, dtype=np.float32)
    
    @classmethod
    def empty(cls, *args: int) -> np.ndarray:
        return np.empty(args, dtype=np.float32)
