Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name=input("이름을 입력하세요: ")
이름을 입력하세요: 김하은
>>> print("만나서 반갑습니다.", name, "씨!")
만나서 반갑습니다. 김하은 씨!
>>> age=int(input("나이를 입력하세요: "))
나이를 입력하세요: 22
>>> print("네, %s씨 당신의 나이는 %d살이군요," %name,age)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("네, %s씨 당신의 나이는 %d살이군요," %name,age)
TypeError: not enough arguments for format string
>>> print("네, %s씨 당신의 나이는 %d살이군요," %(name,age))
네, 김하은씨 당신의 나이는 22살이군요,
>>> 