def find_list(x, box, val):
    if x == box[x]:
        return x, val[x]
    box[x], mmm = find_list(box[x], box, val)
    val[x] = (val[x] + mmm) % 2
    return box[x], val[x]


box_num = 20
ask_num = 7

aaa= [
[1,8,1],
[2,6,1],
[3,7,1],
[1,3,0],
[3,5,1],
[1,11,0],
[5,11,0],
[],
]
result = 'm'
box = [i for i in range(box_num + 1)]
val = [0 for i in range(box_num + 1)]
for i in range(ask_num):
    a, b, ans = aaa[i]
    print(a, b, ans)
    fa, va = find_list(a, box, val)
    fb, vb = find_list(b, box, val)
    if fa != fb:
        box[fa] = fb
        val[fa] = (va + vb + ans) % 2
    elif (val[a] + val[b]) % 2 != ans:
        result = i
        break
print(box)
print(val)
print(result)



"""
3 2 5 4 5 6 7 8 9
0 0 0 0 0 0 0 0 0

"""
