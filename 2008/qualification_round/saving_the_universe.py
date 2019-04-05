for _ in range(int(input())):
    e = int(input())
    engines = [input() for _ in range(e)]
    q = int(input())
    queries = [input() for _ in range(q)]
    searches = set()
    switch_count = 0
    for i in queries:
        searches.add(i)
        if len(searches) == e:
            switch_count += 1
            searches.clear()
            searches.add(i)
    print("Case #", _ + 1, ": ", switch_count, sep="")
