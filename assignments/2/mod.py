a = int(input('a'))
q = int(input('q'))
mod = int(input('mod'))

counter = 1
res = a


def cut(num , mod):
    if num >= mod:
        num -= mod
        return cut(num, mod)
    else:
        return num

def mod_calc(num, power, mod):
    res = 1
    for _ in range(power):
        res *= num
        res = cut(res, mod)

    return res

# while True:
#     print('counter rn:', counter)
#     if mod_calc(a, counter, q) == mod:
#         print('result is:', counter)
#         break
#     else:
#         counter = counter + 1

print(mod_calc(2, 48, 11))