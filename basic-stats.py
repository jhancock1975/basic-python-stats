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
