class sorting:
    def __init__(self):
        pass

    def bubbleSort(self, arr):
        for i in range(len(arr)):
            for j in range(1, len(arr)):
                if arr[j] < arr[j - 1]:
                    self.swap(arr, j, j - 1)
        return arr

    def selectionSort(self, arr):
        for i in range(len(arr)):
            minimumIndex = i
            for j in range(i, len(arr)):
                if arr[j] < arr[minimumIndex]:
                    minimumIndex = j
            self.swap(arr, minimumIndex, i)
        return arr

    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
