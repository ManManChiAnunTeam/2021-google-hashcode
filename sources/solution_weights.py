import sys

for f_name in ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']:
    sys.stdin = open(f_name, 'r')
    sys.stdout = open(f_name + "_output.txt", 'w')

    if __name__ == "__main__":
        # constants
        unit_duration = 4
        waiting_time = 1000

        # input
        # points : (duration - T) + bonus
        duration, inter_n, street_n, car_n, bonus = map(int, input().split())
        adj = [list() for _ in range(inter_n)]
        adj2 = [list() for _ in range(inter_n)]
        name_to_street = {}
        cars = []
        for _ in range(street_n):
            s, e, name, L = input().split()
            s, e, L = int(s), int(e), int(L)
            adj[s].append((e, name, L))
            adj2[e].append((s, name, L))
            name_to_street[name] = (s, e, L)
        for _ in range(car_n):
            path = input().split()
            cars.append(path[1:])

        # solution

        # compute streets' weights
        st_weights = {}
        for car in cars:
            remaining_time = 0
            for st in car:
                remaining_time += name_to_street[st][2] + waiting_time

            for st in car:
                if st in st_weights:
                    st_weights[st] += remaining_time
                    remaining_time -= name_to_street[st][2] + waiting_time
                else:
                    st_weights[st] = remaining_time

            # print(car, remaining_time)
        # print(st_weights)

        # output
        # A : the number of intersections for which you specify the schedule
        printing = []
        A = inter_n
        answer = [[] for _ in range(A)]
        for i in range(A):
            # total = 0
            # for s, name, L in adj2[i]:
            #     total += st_weights[name] if name in st_weights else 0
            # if total == 0:
            #     continue

            sts = []
            times = {}
            for s, name, L in adj2[i]:
                if name in st_weights:
                    sts.append((i, name, st_weights[name]))

            # st_weights 내림차순
            sts = sorted(sts, key=lambda x: x[2], reverse=True)

            for st in sts[:len(sts)//13]:
                answer[st[0]].append((st[1], 3))
            for st in sts[len(sts)//13:]:
                answer[st[0]].append((st[1], 1))

            # print(answer)

            # for e, name, L in adj[i]:
            #     if name in times:
            #         answer[e].append((name, times[name]))

        for i in range(A):
            # i : id
            # E : number of incoming
            # E lines : street name , duration
            if len(answer[i]) == 0:
                continue
            # print(i)
            # print(len(answer[i]))
            name_d = []
            for name, d in answer[i]:
                name_d.append((name, d))
                # print(name, d)
            printing.append((i, len(answer[i]), name_d))

        print(len(printing))
        for p in printing:
            print(p[0])
            print(p[1])
            for name, d in p[2]:
                print(name, d)
