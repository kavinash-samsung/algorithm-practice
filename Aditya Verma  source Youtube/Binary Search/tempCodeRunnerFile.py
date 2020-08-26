if array[mid]<= array[prev] and array[mid]<=array[nex]:
            return mid
        elif array[mid] >= array[start]:
            start = mid+1
        elif array[mid] <= array[end]:
            end = mid-1