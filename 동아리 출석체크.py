# 동아리 출석체크
total = 0
group = []

# 이름을 입력하고 ENTER 키
while 1:
    member = input()
    if member == '':  
        break
    group.append(member)

for member in group:
    if member in ['박영수', '이연웅', '임수홍', '전민서']:
        total += 1

print(f"금일 동아리 참석자는 총 {total}명 입니다.\n \n참석자 명단 : {','.join(group)}")

