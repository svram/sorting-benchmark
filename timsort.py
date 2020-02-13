def merge_sorted_arrays(A, B):
  combined = []
  lenA = len(A)
  lenB = len(B)
  j, k = 0, 0
  while 1:
    if j == lenA:
      combined += B[k:]
      return combined
    elif k == lenB:
      combined += A[j:]
      return combined
    
    if A[j] <= B[k]:
      combined.append(A[j])
      j += 1
    elif B[k] <= A[j]:
      combined.append(B[k])
      k += 1
      
def timsort(A):
  to_be_merged = []
  subArray = [A[0]]
  N = len(A)
  for element in xrange(1, N):
    
    if A[element] >= subArray[-1]:
      subArray.append(A[element])
    else:
      to_be_merged.append(subArray)
      subArray = [A[element]]
      #print subArray, element
    if element >= N - 1:
      to_be_merged.append(subArray)

  if len(to_be_merged) == 1:
    return to_be_merged[0]

  #print to_be_merged
  combined = to_be_merged[0]
  #print to_be_merged
  for i in xrange(1, len(to_be_merged)):
    combined = merge_sorted_arrays(combined, to_be_merged[i])
  
  return combined

'''A = [-1, 9, 3, 4, 1, 0, -6, 7, 8, 5, 3, 6, 9, 1, 2, 3, 4, 9, 8, 4, 3, 1, 6, 3, 2, 6, 5, 2, 18, -12, -13, -4, 0, 5, 2, 5, 4, 3, 2, 1 , 4, -1, -2, -4, -6, -10, 21]
sortedA = timsort(A)
print len(A)
print len(sortedA)
print sortedA
print sorted(A)'''
    