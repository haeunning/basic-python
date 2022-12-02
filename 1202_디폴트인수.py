def calc(x,y,z=30): #z는 디폴트 인수. 
    return(x+y)*z

result1 = calc(10,20) #z는 지정하지않으면 디폴트값으로 대입됨
print("result1", ":", result1) 
 
result2 = calc(1,2,3) #z가 디폴트인수여도 다른값으로 지정할 수 있음
print("result2", ":", result2) 
