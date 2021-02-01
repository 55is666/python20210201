#檔名:1-5
point=int(input("學生分數:"))
if point>100 or point<0:
    print("你在打甚麼鬼")
elif point>=60:
    print("及格")
else:
    print("不及格")
