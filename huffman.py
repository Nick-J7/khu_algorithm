import heapq
import numpy as np
from collections import defaultdict

import pdb

def encode(frequency):
  heap = [ [weight, [symbol, '']] for symbol, weight in frequency.items() ]
  heapq.heapify(heap)
  while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)

    for pair in lo[1:]:
      pair[1] = '0' + pair[1]
    for pair in hi[1:]:
      pair[1] = '1' + pair[1]

    lo[0] = lo[0] + hi[0]
    for pair in hi[1:]:
        lo.append(pair)
    heapq.heappush(heap, lo)

  return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1])))
    
if __name__=='__main__':

    data = "The frog at the bottom of the well drifts off into the great ocean"
    frequency = defaultdict(int)
    print(frequency)

    for symbol in data:
      frequency[symbol] += 1

    huff = encode(frequency)
    print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
    for p in huff:
        print(p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
