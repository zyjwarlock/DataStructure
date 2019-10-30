class mySort:

    def __init__(self, arr):
        self.arr = arr
        self.len = len(arr)

    def __quicksort_rec(self, l):
        if len(l)<=1: return l
        mid = l[-1]
        left = []
        right = []
        for e in l[:-1]:
            if e > left: left.append(e)
            else: right.append(e)
        return left+[mid]+right

    def __heapify(self, tree, s_Index, e_Index):
        root = s_Index
        max_child = root*2+1

        while max_child<=e_Index:
            if max_child+1 <= e_Index and  tree[max_child] < tree[max_child+1]:
                max_child += 1
            if tree[root] < tree[max_child]:
                tree[root], tree[max_child] = tree[max_child], tree[root]
                root = max_child
                max_child  = root*2+1
            else: break

    def __build_heap(self, n):
        for i in range(n//2-1, -1, -1):
            self.__heapify(self.arr, i, n-1)

    def __merge_rec(self, l):
        if len(l)<=1:
            return l
        mid = len(l)//2
        left = self.__merge_rec(l[0:mid])
        right = self.__merge_rec(l[mid:])
        sortedList = []
        while left and right:
            if left[0] < right[0]:
                sortedList.append(left.pop(0))
            else: sortedList.append(right.pop(0))
        if left:
            return  sortedList+left
        else: return sortedList+right


    def quicksort(self):
        self.__quicksort_rec(self.arr)

    def heapsort(self):
        self.__build_heap(self.len)
        for e in range(self.len-1, -1, -1):
            self.arr[0], self.arr[e] = self.arr[e], self.arr[0]
            self.__heapify(self.arr, 0, e-1)

    def mergesort(self):
        self.arr = self.__merge_rec(self.arr)


def main():
    arr = mySort([9, 4, 6, 7, 2, 3, 5, 8, 0, 1])
    arr.mergesort()
    print(arr.arr)

if __name__=="__main__":
    main()

