import numpy as np
import pdb

int_inf = 987654321

n = 5
W = np.array(
  [
    [int_inf, int_inf, int_inf, int_inf, int_inf, int_inf],
    [int_inf, int_inf, 7, 4, 6, 1],
    [int_inf, int_inf, int_inf, int_inf, int_inf, int_inf],
    [int_inf, int_inf, 2, int_inf, 4, int_inf],
    [int_inf, int_inf, 3, int_inf, int_inf, int_inf],
    [int_inf, int_inf, int_inf, int_inf, 1, int_inf]
  ], dtype=np.int32)
  
def dijkstra():
  length = np.zeros(n, dtype=np.int32) 
  nearest = np.zeros(n, dtype=np.int32)
  shortest_distance = np.zeros(n, dtype=np.int32)
  F = set()
  pdb.set_trace()
  
  # Initialize length
  length[1] = -1
  for i in range(2, n+1):
    length[i] = W[1][i]
    nearest[i] = 1
    
  for i in range(n-1):
    # Find shortest vertex.
    vnear = None
    min_length = int_inf
    for v_index in range(2, n+1):
      if length >= 0 and length[i] < min_length:
        min_length = length[v_index]
        vnear = v_index
    
    # Add nearest vertex to F.
    print("vnear: ", vnear)
    F.add((nearest[vnear], vnear))
    shortest_distance[vnear] = min_length
    
    for v_index in range(2, n+1):
      if length[vnear] + W[vnear][v_index] < length[v_index]:
        length[v_index] = length[vnear] + W[vnear][v_index]
        nearest[v_index] = vnear
    length[vnear] = -1
    
    print(F)
    print(shortest_distance)
    
    
if __name__=='__main__':
  print("Start")
  dijkstra()
  print("End")