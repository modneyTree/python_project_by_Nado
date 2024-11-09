numbers = [1, 3, 5, 7, 9]
target = 4

for number in numbers:
    if number == target:
        print(f"{target}을(를) 찾았습니다.")
        break
else:
    print(f"{target}을(를) 찾지 못했습니다.")

# ----------------------------------------------------------------


numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
    if num == 3:
        break
else:
    print("루프가 정상적으로 완료되었습니다.")

# 출력:
# 1
# 2
# 3


# Python의 for 루프에는 else 절을 함께 사용할 수 있습니다. 
# 이때 else는 루프가 정상적으로 완료되었을 때(즉, break 문으로 인해 중단되지 않았을 때) 실행됩니다