def countSwaps(a):
    # Write your code here
    swap_count = 0
    swaped = False
    length = len(a) - 1
    while swaped==False:
        swaped = True
        for i in range(0,length):
            if a[i] > a[i+1]:
                swaped = False
                a[i], a[i+1] = a[i+1], a[i]
                swap_count+=1
    print(
        f"Array is sorted in {swap_count} swaps.\n"
        f"First Element: {a[0]}\n"
        f"Last Element: {a[-1]}\n"
    )
    

nums = [33,4,5,66,7]
countSwaps(nums)
