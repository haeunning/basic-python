# 문자열 개수
# 문장에서 대소문자를 구분하고 않고 사용된 python 문자열의 개수를 출력하는 프로그램을 작성하시오.

st = "Python is widely used high-level language and python was conceieved in the late 1980s"
st = st.lower() # 대소문자 구분 X

cnt = st.count('python')
print("python 개수: ", cnt)


