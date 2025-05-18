def covariance(x,y,m_x, m_y):
  cov = 0
  for i in range(len(x)):
    cov += ((x[i]-m_x)*(y[i]-m_y))
  return cov/(len(x)-1)

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
  # Your code here
  Means = []
  temp = 0
  for i in range(len(vectors)):
    for j in range(len(vectors[0])):
        temp += vectors[i][j]
    Means.append(temp/len(vectors[0]))
    temp = 0

  temp = []
  cov_m = []
  for i in range(len(vectors)):
    for j in range(len(vectors)):
      temp.append(0)
    cov_m.append(temp)
    temp = []
  for i in range(len(vectors)):
    for j in range(len(vectors)):
        cov_m[i][j]= covariance(vectors[i],vectors[j],Means[i],Means[j])
  return cov_m