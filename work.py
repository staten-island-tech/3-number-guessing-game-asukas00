list_ofnum = [1,10,5,3]
def sportball(numbers):
    min = 0
    max = 0
    minnum = numbers[0]
    maxnum = numbers[0]
    for i in (numbers):
        if i > maxnum:
            max += 1
            maxnum = i
        elif i < minnum:
            min += 1
            minnum = i
    print(min)
    print(max)
sportball(list_ofnum)