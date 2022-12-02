def modify1(s):
    s = "Welcome!"
msg = "Hello!"
print(msg)
modify1(msg)
print(msg)

def modify1(L):
    L=['a','b','c'] #전체 리스트를 대상으로 함수를 적용하면 안바뀐다
lst=[1,2,3]
print(lst)
modify1(lst) 
print(lst)

def modify1(L):
    L[0]='a' #인덱스로 함수를 적용하면 바뀐다
lst = [1,2,3]
print(lst)
modify1(lst) 
print(lst)
