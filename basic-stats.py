def mean(l):
  return float(sum(l))/len(l)

def variance(l):
  m = mean(l);
  return sum([ (x-m)**2 for x in l])/len(l)

def factor(l):
  return 1.96

# returns the amount to be added and subtracted from sample
# estimate to compute a confidence interval
def plusMinusQty(l):
  return factor(l)*(( variance(l)/len(l) ) ** 0.5)

flatten = lambda l: [item for sublist in l for item in sublist]

def getComponent(l, index):
  return [ l[i][index] for i in range(len(l)) ]

def xValues(l):
  return getComponent(l, 0)

def yValues(l):
  return getComponent(l, 1)

def linRegSlope(l):
  xList = xValues(l)
  yList = yValues(l)
  meanX = mean(xList)
  meanY = mean(yList)  
  return sum( [ (xList[i] - meanX) * (yList[i] - meanY) for i in range(len(l))] ) / sum( [ (xList[i] - meanX)**2 for i in range(len(l)) ] )

def linRegIntercept(l):
  xList = xValues(l)
  yList = yValues(l)
  meanX = mean(xList)
  meanY = mean(yList)  
  return meanY - linRegSlope(l)*meanX

def correlation(l):
  xList = xValues(l)
  yList = yValues(l)
  meanX = mean(xList)
  meanY = mean(yList)  
  return sum( [ (xList[i] - meanX) * (yList[i] - meanY) for i in range(len(l))] ) / ( sum( [ (xList[i] - meanX)**2 for i in range(len(l)) ] ) * sum( [ (yList[i] - meanY)**2 for i in range(len(l)) ] )  )**0.5
