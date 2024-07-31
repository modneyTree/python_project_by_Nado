numbers = [1, 3, 5, 7, 9]
target = 4

for number in numbers:
    if number == target:
        print(f"{target}을(를) 찾았습니다.")
        break
else:
    print(f"{target}을(를) 찾지 못했습니다.")
