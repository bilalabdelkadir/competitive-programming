def insertionSort1(n, arr):
    # Write your code here
    c = arr[-1]
    i = n -1

    while i > 0 and arr[i-1] > c:
        arr[i] = arr[i -1]
        print(*arr)
        i -= 1
    arr[i] = c

    print(*arr)
              
