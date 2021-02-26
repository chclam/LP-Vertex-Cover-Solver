from scipy.optimize import linprog
import numpy as np

def getConstraints(vertices, edges):
  # edges must be in tuples
  ri = np.ones(len(edges)) * -1
  le = []
  for e in edges:
    c = np.zeros(len(vertices))
    c[e[0]] = -1
    c[e[1]] = -1
    le.append(c)
  return le, ri 
    
def getVertexCover(vertices, edges):
  '''
  Get vertex cover using linear programming
  '''
  # Create objective function:
  # Minimize: 1*x_v1 + 1*x_v2 ... 1*x_vn
  obj = np.ones(len(vertices))
  # Create bounds: 
  # for each v: (0 <= x_v <= 1)
  bnd = [(0, 1) for i in range(len(vertices))]
  l, r = getConstraints(vertices, edges)
  sol = linprog(c=obj, A_ub=l, b_ub=r, bounds=bnd, method="revised simplex")
  return sol

if __name__ == "__main__":
  # insert number of vertices here
  numOfVertices = 14 
  # create vertices from 0 - n
  vertices = np.arange(numOfVertices)
  # insert undirected edges here in tuples
  edges = [
    (0, 1),
    (1, 2),
    (2, 5),
    (4, 5),
    (3, 4),
    (0, 3),
    (4, 6),
    (6, 7),
    (7, 8),
    (8, 11),
    (11, 12),
    (12, 13),
    (13, 10),
    (9, 10),
    (8, 9),
    (7, 10)
  ]
  opt = getVertexCover(vertices, edges)
  print(opt)

