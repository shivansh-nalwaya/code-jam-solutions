for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    m = 0
    for i in range(n):
        m += a[i] * b[i]
    print("Case #%d: %d" % (_ + 1, m))
