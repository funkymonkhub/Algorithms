def insertion_sort(arr): 
  
    for i in range(1, len(arr)): 
  
        pivot = arr[i]  
        j = i-1
        while j >=0 and pivot < arr[j] : 
                arr[j+1]=arr[j] 
                j-=1
        arr[j+1]=pivot 
  
   
arr = [3, 31, 2, 6, 5] 
insertion_sort(arr) 
print ("Sorted array:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 