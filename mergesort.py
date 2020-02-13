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

def mergesort(A):
  
  if len(A) > 1:
    mid = int((len(A) - 1)/2)
    return merge_sorted_arrays(mergesort(A[:mid+1]), mergesort(A[mid+1:]))
  else:
    return A
  


