def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1    
            else:
                arr[k]=right[j]
                j+=1
            k+=1     
        while i<len(left):
            arr[k]=left[i];
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j];
            j+=1;k+=1
#Driver Code 
arr = [23,4,26,21,10,58,62,19,32,5,47,3]
mergeSort(arr)
print(arr)