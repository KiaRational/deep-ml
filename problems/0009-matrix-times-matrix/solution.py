def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

  if len(a[0]) != len(b):
      return -1

  m_a = len(a)
  n_a = len(a[0])
  m_b = len(b)
  n_b = len(b[0])
  
  temp = []
  c = []
  for i in range(len(a)):
    for j in range(len(b[0])):
      temp.append(0)
    c.append(temp)
    temp = []

  for i in range(m_a):
      for j in range(n_b):
          for k in range(n_a):
              c[i][j] += a[i][k] * b[k][j]

  return c