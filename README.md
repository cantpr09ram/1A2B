# 1A2B

## tool

* random
--------

## random number generator

```python
import random
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
password = ''
for i in range(4):
    password+=str(items[i])   
print("start")

```
## input number

```python
while True:
    type_in = []
    tp = input()
    type_in = list(tp)
```

### Confirm input is conform to the format or not 
```python  
    see=0
    if len(type_in)!=4:
        see+=1
    for y in range(4):
        try:
            int(type_in[y])
        except(ValueError,TypeError,IndexError):
            see+=1
    if see>0:
         print("無效輸入")
         continue
    for u in range (4):
        d=int(type_in.count(type_in[u]))
        if d>=2:
            see+=1
    if see>0:
         print("無效輸入")
         continue
```
### Confirm how much is correct
```python
 a = 0
    b = 0
    ''''告訴玩家所輸入的數字是否為正確答案'''
    for j in range(4):
        if password[j] == type_in[j]:
            a+=1
        for k in range(4):
            if password[j] == type_in[k] and j != k:
                b+=1

    if a == 0 and b == 0:
        print("C")
        n+=1
    elif a == 4:
        n += 1
        print("you win")
        break
    else:
        print("%da%db"%(a,b))
        n+=1
print("you spend %d times"%n)
```
