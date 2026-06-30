from collections import Counter

n = int(input())
a = [int(input()) for _ in range(n)]

cnt = Counter(a)
cnt_list = list(cnt.items())

if len(cnt_list) < 2:
    print("NO")
else:
    for i in range(len(cnt_list)):
        for j in range(i + 1, len(cnt_list)):
            if cnt_list[i][1] == cnt_list[j][1] and cnt_list[i][1] * 2 == n:
                print("YES")
                print(cnt_list[i][0], cnt_list[j][0])
                exit()
    print("NO")