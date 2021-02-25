from scipy.optimize import linprog

def getObj(vertices):
  return [1 for i in range(len(vertices))]

def getBounds(vertices):
  return [(0, 1) for i in range(len(vertices))]

def getConstraints(vertices, edges):
  # edges must be in tuples
  ri = [[-1] for i in range(len(edges))]
  le = []
  for e in edges:
    c = [0 for i in range(len(vertices))]
    c[e[0]] = -1
    c[e[1]] = -1
    le.append(c)
  return le, ri 
    
def getVertexCover(vertices, edges):
  '''
  Get vertex cover using linear programming
  '''
  obj = getObj(vertices)
  bnd = getBounds(vertices)
  l, r = getConstraints(vertices, edges)
  sol = linprog(c=obj, A_ub=l, b_ub=r, bounds=bnd, method="revised simplex")
  return sol

if __name__ == "__main__":
  numOfVertices = 14 
  vertices = [i for i in range(numOfVertices)]
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
  
