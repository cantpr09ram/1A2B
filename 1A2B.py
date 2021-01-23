'''亂數生成'''
import random
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
password = ''
for i in range(4):
    password+=str(items[i])   
print("start")

n= 0
'''用while達到無限輸入 '''
while True:
    type_in = []
    tp = input()
    type_in = list(tp)

    #檢查是否符合輸入格式
    see=0
    if len(type_in)!=4:#是否事由是個東西組成
        see+=1
    for y in range(4):#檢查是否為數字
        try:
            int(type_in[y])
        except(ValueError,TypeError,IndexError):
            see+=1
    if see>0:
         print("無效輸入")
         continue
    for u in range (4):#檢查是否有重複的數字
        d=int(type_in.count(type_in[u]))
        if d>=2:
            see+=1
    if see>0:
         print("無效輸入")
         continue

    a = 0
    b = 0
    ''''告訴玩家所輸入的數字是否為正確答案'''
    for j in range(4):
        if password[j] == type_in[j]:
            a+=1
        for k in range(4):
            if password[j] == type_in[k] and j != k:
                b+=1

    if a == 0 and b == 0:#全錯
        print("C")
        n+=1
    elif a == 4:#全對
        n += 1
        print("you win")
        break
    else:#有對有錯
        print("%da%db"%(a,b))
        n+=1
print("you spend %d times"%n)#結算花費多少次
