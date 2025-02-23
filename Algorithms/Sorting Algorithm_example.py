# #Bubble sort
def buuble_sort(arr):
  for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr
  
arr= [5,9,3,1,2,8,4,7,6]
print(buuble_sort(arr))

# #Time complexity: O(n^2)
# #Space COmplexity: O(1)
# # =====================================================================================
# #Selection sort
def selection(arr):
  for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
      if arr[min_index] > arr[j]:
        min_index= j
    arr[i],arr[min_index]= arr[min_index],arr[i]
  return arr

arr= [5,7,4,3,8,6,1,9,2]
print(selection(arr))

# #Time complexity: O(n^2)
# #Space COmplexity: O(1)
# # =====================================================================================
# #Insertion sort
def insertion_sort(arr):
  for i in range(len(arr)):
    first_index= i
    for j in range(i+1,len(arr)):
      if arr[first_index] > arr[j]:
        arr[first_index],arr[j]= arr[j],arr[first_index]
  return arr 


arr= [5,3,4,7,2,8,6,9,1]
print(insertion_sort(arr))

# #Time complexity: O(n^2)
# #Space COmplexity: O(1)
# =====================================================================================
#Bubble sort
import math

#bubble sorrt
def bubble_sort(arr):
  no_buckets= round(math.sqrt(len(arr)))
  maxVal= max(arr)
  ans=[]
  for i in range(no_buckets):
    ans.append([])
  for val in arr:
    bucket_index= math.ceil(val*no_buckets/maxVal)
    ans[bucket_index-1].append(val)
  for i in range(no_buckets):
    ans[i]= insertion_sort(ans[i])
  
  k= 0
  for i in range(no_buckets):
    for j in range(len(ans[i])):
      arr[k]= ans[i][j]
      k += 1
  return arr


arr= [5,3,4,7,2,8,6,9,1]
print(bubble_sort(arr))

#Time complexity: O(n^2)
#Space COmplexity: O(N)
# =====================================================================================
#merge sort
def merge(arr,l,m,r):
  n1= m - l +1
  n2= r -m
  L= [0]*(n1)
  R= [0]*(n2)

  for i in range(0,n1):
    L[i]= arr[l+i] 
  for j in range(0,n2):
    R[j]= arr[m+1+j] 
  
  i= 0    #index of firstsubarray
  j= 0    #index of second subarray
  k= l    #index of merge subarray

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k]= L[i]
      i += 1
    else:
      arr[k]= R[j]
      j += 1
    k += 1
  
  while i < n1:
    arr[k]= L[i]
    i += 1
    k += 1
  
  while j < n2:
    arr[k]= R[j]
    j += 1
    k += 1
  

def merge_sort(arr,l,r):
  if l < r:
    m = (l + (r-1))//2
    merge_sort(arr,l,m)
    merge_sort(arr,m+1,r)
    merge(arr,l,m,r)
  return arr


arr= [6,4,3,7,5,1,2]
print(merge_sort(arr,0,len(arr)-1))

#Time complexity: O(nlogn)
#Space complexity: O(n)
# =====================================================================================
#quick sort
def swap(arr,index1,index2):
  arr[index1],arr[index2]= arr[index2],arr[index1]

def pivot(arr,pivot_index,end_index):
  swap_index= pivot_index
  for i in range(pivot_index+1,end_index+1):
    if arr[i] < arr[pivot_index]:
       swap_index += 1
       swap(arr,swap_index,i)
  swap(arr,pivot_index,swap_index)
  return swap_index  

def quick_sort(arr,left,right):
  if left < right:
    pivot_index= pivot(arr,left,right)
    quick_sort(arr,left,pivot_index-1)
    quick_sort(arr,pivot_index+1,right)
  return arr
  


arr= [3,5,0,6,2,1,4]
print(pivot(arr,0,len(arr)-1))
print(arr)
print(quick_sort(arr,0,len(arr)-1))
# =====================================================================================
#heap sort
def heapify(arr,n,i):
  small_no= i
  l= 2*i + 1
  r= 2*i + 2
  if l < n and arr[l] < arr[small_no]:
    small_no = l
  if r < n and arr[r] < arr[small_no]:
    small_no = r
  if small_no != i:
    arr[i],arr[small_no]= arr[small_no],arr[i]
    heapify(arr,n,small_no)

def heap_sort(arr):
  n = len(arr)
  for i in range(int(n//2)-1,-1,-1):
    heapify(arr,n,i)
  
  for i in range(n-1,0,-1):
    arr[i],arr[0]= arr[0],arr[i]
    heapify(arr,i,0)
  arr.reverse()
  return arr


arr= [15,10,40,20,50,10,30,45,5]
print(heap_sort(arr))

# Time COmplexity: O(nLogN)
#Space complexity: O(1)