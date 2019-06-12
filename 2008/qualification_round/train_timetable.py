def parsetimetable(n, t):
    departure = []
    ready = []
    for _ in range(n):
        sp = input().split()
        departure.append(60 * int(sp[0][0:2]) + int(sp[0][3:5]))
        ready.append(60 * int(sp[1][0:2]) + int(sp[1][3:5]) + t)
    departure.sort()
    ready.sort()
    return departure, ready


def solve(departure, ready):
    n = 0
    r = 0
    for t in departure:
        if r < len(ready) and ready[r] <= t:
            r += 1
        else:
            n += 1
    return n


for _ in range(int(input())):
    turn_around_time = int(input())
    na, nb = map(int, input().split())
    departureA, readyB = parsetimetable(na, turn_around_time)
    departureB, readyA = parsetimetable(nb, turn_around_time)

    print("Case", "#" + str(_+1) + ":",
          solve(departureA, readyA), solve(departureB, readyB))
