class sorting:
    def __init__(self):
        pass

    def BubbleSort(self, arr):
        for i in range(len(arr)):
            for j in range(1, len(arr)):
                if arr[j] < arr[j - 1]:
                    self.swap(arr, j, j - 1)
        return arr

    def SelectionSort(self, arr):
        for i in range(len(arr)):
            minimumIndex = i
            for j in range(i, len(arr)):
                if arr[j] < arr[minimumIndex]:
                    minimumIndex = j
            self.swap(arr, minimumIndex, i)
        return arr

    def InsertionSort(self, arr):
        for i in range(1, len(arr)):
            current = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > current:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current
        return arr

    def MergeSort(self, arr):
        if len(arr) < 2:
            return arr  # Return the array itself if it's already sorted

        middle = len(arr) // 2
        left = arr[:middle]  # Use slicing to create the left part
        right = arr[middle:]  # Use slicing to create the right part

        # Recursive sort of left and right
        left = self.MergeSort(left)
        right = self.MergeSort(right)

        # Merge the sorted halves
        return self.MergeArrays(left, right)

    def MergeArrays(self, leftarr, rightarr):
        result = []
        i = 0
        j = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] <= rightarr[j]:
                result.append(leftarr[i])
                i += 1
            else:
                result.append(rightarr[j])
                j += 1

        # Append remaining elements
        result.extend(leftarr[i:])
        result.extend(rightarr[j:])

        return result

    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
