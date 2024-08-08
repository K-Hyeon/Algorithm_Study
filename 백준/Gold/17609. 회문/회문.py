for _ in range(int(input())):
    array = input().strip()
    left, right = 0, len(array) - 1
    
    check = 0
    for _ in range(len(array)):
        if left >= right: break
            
        if array[left] == array[right]:
            left += 1
            right -= 1
            continue

        if array[left] == array[right-1]:
            temp = array[left:right]
            if temp == temp[::-1]:
                check = 1
                break

        if array[left+1] == array[right]:
            temp = array[left+1:right+1]
            if temp == temp[::-1]:
                check = 1
                break

        check = 2
        break

    print(check)