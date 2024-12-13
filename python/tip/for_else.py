# for - else
# 중간에 break 없으면 else 문 실행
# 중간에 멈춘다면 else 문 실행 X

for i in [1,2,3,4]:
    print(i)
    if(i == 4):
        break 
    
else: print("loop 완료")

