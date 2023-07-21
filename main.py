def lastman(n, k):
    if n == 1:
        return 0
    else:
        return (lastman(n - 1, k) + k) % n

# 輸入的n 值為0到100
n = int(input("請輸入同事數量（0-100）："))
# 報到3退出，故k 值為 3
k = 3
position = lastman(n, k) + 1
print("最後留下的同事是所有同事裡面的第 {} 位".format(position))