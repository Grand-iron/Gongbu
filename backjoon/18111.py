import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = []
for i in range(N) :
    ground.extend(list(map(int, input().split())))
T = N * M
height_cnt = {}
height = []
for k in range(T) :
        h = ground[k]
        try :
            height_cnt[h] += 1
        except :
            height.append(h)
            height_cnt[h] = 1
height.sort()
lp = 0
rp = len(height) - 1
is_up_to_down = True
is_rock_needed = False
need_rocks = 0
cost = 0
if (lp == rp) : print(0, height[0])
while lp < rp :
    if is_up_to_down :
        cur = height[rp]
        area = height_cnt[cur]
        rest = T - area
        nex = height[rp-1]
        gab = cur - nex
        if 2*area < rest :
            total_rock = area * gab
            cost += 2 * total_rock
            height_cnt[nex] += area
            if height_cnt[nex] == T :
                print(cost, nex)
                break
            del height_cnt[cur]
            B += total_rock
            rp -= 1
        elif is_rock_needed :
            down = 0
            while down < gab and B < need_rocks :
                cost += 2 * area
                B += area
                down += 1
            if down == gab :
                height_cnt[nex] += area
                if height_cnt[nex] == T :
                    print(cost, nex)
                    break
                del height_cnt[cur]
                rp -= 1
            elif down :
                new = cur - down
                height_cnt[new] = height_cnt[cur]
                del height_cnt[cur]
                height[rp] = new
            if B >= need_rocks :
                is_up_to_down = False
                is_rock_needed = False
        else :
            is_up_to_down = False
    else :
        cur = height[lp]
        area = height_cnt[cur]
        rest = T - area
        nex = height[lp+1]
        if area <= 2*rest :
            total_rock = area * (nex - cur)
            if B >= total_rock :
                cost += total_rock
                height_cnt[nex] += area
                if height_cnt[nex] == T :
                    print(cost, nex)
                    break
                del height_cnt[cur]
                B -= total_rock
                lp += 1
            else :
                up = 0
                while B >= area :
                    B -= area
                    cost += area
                    up += 1
                if up :
                    new = cur + up
                    height_cnt[new] = height_cnt[cur]
                    del height_cnt[cur]
                    height[lp] = new
                need_rocks = area
                is_rock_needed = True
                is_up_to_down = True
        else :
            is_up_to_down = True