import heapq
import numpy as np
from collections import defaultdict

    
def encode(frequency):
  heap = [ [weight, [symbol, '']] for weight, symbol in frequency.items() ]
  print(heap)
  heapq.heapify(heap)
  while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)
    print(heap)
    print(type(lo[1]))
    lo[1][1] = '0' + lo[1][1]
    hi[1][1] = '1' + hi[1][1]
    
    #for pair in lo[1]:
    #  pair[1] = '0' + pair[1]
    #for pair in hi[1]:
    #  pair[1] = '1' + pair[1]
      
    print('hello')
    heapq.heappush(heap, [lo[0] + hi[0], lo[1] + hi[1]])
    
data = "The frog at the bottom of the well drifts off into the great ocean"
frequency = defaultdict(int)

for symbol in data:
  frequency[symbol] += 1

print("frequency: ", frequency)
huff = encode(frequency)


#if __name__=='__main__':