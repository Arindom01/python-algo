list = [1,8,89,6,3,5,9]

def merge(arr, L, R):
  i = j = k= 0
  while (i < len(L) and j < len(R)):
    # for k in range(0, len(arr) - 1 ):
      if L[i] < R[j]:
        arr[k] = L[i]
        i = i +1
      else:
        arr[k] = R[j]
        j = j + 1
      k = k + 1
    
  while i < len(L):
    arr[k] = L[i]
    i = i + 1
    k = k + 1
  
  while j < len(R):
    arr[k] = R[j]
    j = j + 1
    k = k + 1
  print("--",L, arr)
  return arr



def mergeSort(arr):
  # k = 0
  # print(list)
  N = len(arr)
  if N < 2:
    return
  
  mid=N//2

  leftArr=arr[:mid]
  rightArr=arr[mid:]

  
  mergeSort(leftArr)

  mergeSort(rightArr)
  print(arr, leftArr, rightArr)
  merge(arr, leftArr, rightArr)

  return arr

print(mergeSort(list)  )
