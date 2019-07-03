import random
start = input('請決定上限值: ')
start = int(start)
end = input('請決定下限值: ')
end = int(end)
r = random.randint(start, end)
count = 0
while True:
    count = count + 1
    ans = input('請輸入您猜的數字: ')
    ans = int(ans)
    if ans == r:
        print('恭喜你猜對了，共猜了', count,'次')
        break
    else:
        print('猜錯囉')
        if ans > r:
            print(ans, '比答案大')
        else:
            print(ans, '比答案小')

