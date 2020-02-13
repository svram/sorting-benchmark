def bubbleSort(A):
  indexOfLast = len(A) - 1
  for i in xrange(len(A) - 1):
    for j in xrange(indexOfLast):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]
    indexOfLast -= 1
  return A