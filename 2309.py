height_list = []
total_height = 0

# 아이들의 키 입력받기
for _ in range(9):
    height = int(input())
    height_list.append(height)
    total_height += height

# 두 아이의 키 합이 total_height - 100이 되는 경우 찾기
found = False
for i in range(9):
    if found:
        break
    for j in range(i + 1, 9):
        temp_subheight = height_list[i] + height_list[j]
        if temp_subheight == total_height - 100:
            # 찾은 경우 두 아이의 키 삭제하고 반복문 종료
            height_list.remove(height_list[i])
            height_list.remove(height_list[j - 1])  # j가 더 큰 인덱스일 경우
            found = True
            break

sorted_height = sorted(height_list)

for height in sorted_height:
    print(height)