largest = i 
        left = 2 * i + 1 
        right = 2 * i + 2 

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 

            self.heapify(arr, n, largest)
