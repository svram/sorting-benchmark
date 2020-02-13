import random, time
from copy import deepcopy
import quicksort as qs
import mergesort as ms
import timsort as ts
from bubblesort import bubbleSort as bbs

def create_large_list(N, minimum, maximum):
  array = [random.randint(minimum, maximum) for _ in xrange(N)]
  return array

def time_comparision():
  A = create_large_list(10000, -10, 1000)
  B = deepcopy(A)
  C = deepcopy(A)
  D = deepcopy(A)
  E = deepcopy(A)
  F = deepcopy(A)
  L = len(A)

  '''print A
  print B
  print C'''
  
  ts1 = time.time()
  qs.quicksort(A, 0, L)
  te1 = time.time()
  print "Quicksort: Time taken if pivot is 1st element: " + str(te1 - ts1)
  
  ts2 = time.time()
  qs.quicksort_random(B, 0, L)
  te2 = time.time()
  print "Quicksort: Time taken if pivot is random: " + str(te2 - ts2)

  ts3 = time.time()
  C = ms.mergesort(C)
  te3= time.time()
  print "Mergesort: time taken: " + str(te3 - ts3)

  ts5 = time.time()
  E = ts.timsort(E)
  te5= time.time()
  print "Timsort: time taken: " + str(te5 - ts5)

  ts4 = time.time()
  D = sorted(D)
  te4= time.time()
  print "Python sort implementation: time taken: " + str(te4 - ts4)

  ts6 = time.time()
  F = bbs(F)
  te6= time.time()
  print "Bubble sort implementation: time taken: " + str(te6 - ts6)

  '''print A
  print B
  print C'''

  if A == B and A == C and A == D and A == E and A == F:
  	print "Sort Successful"

  if C == D and C == E:
  	print "Sort Successful"

  


time_comparision()
