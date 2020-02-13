def partition(A, p, r):
  pivot = A[p]
  i = p
  j = i+1
  
  for k in xrange(j, r):
    if A[k] <= pivot:
      A[i+1], A[k] = A[k], A[i+1]
      i += 1
  A[p], A[i] = A[i], A[p]
  
  return i

def quicksort(A, p, r):
  if p < r:
    i = partition(A, p, r)
    quicksort(A, p, i)
    quicksort(A, i + 1, r)
    
    
    
def partition_random(A, p, r):
  #pivot = random.randint(p, r-1)
  pivot = int((r-p)/2)
  for k in xrange(p, r):
    if A[k] >= A[pivot] and k < pivot:
      pivot = k
      A[k], A[pivot] = A[pivot], A[k]
    elif k > pivot and A[k] <= A[pivot]:
      A[pivot + 1], A[k] = A[k], A[pivot + 1]
      A[pivot], A[pivot + 1] = A[pivot + 1], A[pivot]
      pivot += 1
  return pivot
      

def quicksort_random(A, p, r):
  if p < r:
    i = partition_random(A, p, r)
    quicksort(A, i + 1, r)
    quicksort(A, p, i)
