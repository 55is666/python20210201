point=int(input('學生分數'))
if point>100 or point<0:
    print("別亂打行不行")
elif point>=90:
    print("A?你作弊!!")
elif point>=80:
    print("B?你抄錯了吧?(答案)")
elif point>=70:
    print("C!笑你")
elif point>=60:
    print("D!你有臉看我嗎?")
else:
    print("E!重新投胎分數比較高啦!")
    
