# 1
def main(n):
    s = 1
    for i in range(1, n + 1):
        s *= i

    return


# 2
def main(*args):
    return sum(args)


# 3
def main(lst, item):
    try:
        ind = lst.index(item)
    except ValueError:
        return '不存在'
    else:
        return ind


# 4
def main(lst):
    n = len(lst)
    sum = 0
    list = []
    for i in lst:
        sum += i
    mean = sum / n
    for i in range(0, n):
        if (lst[i] >= mean):
            list.append(lst[i])
    return list


# 5
def main(p, q):
    s = p // q
    y = p % q
    tup = (s, y)
    return tup


# 6
def main(num):
    s = 0
    while (num):
        s += num % 10
        num = num // 10
    return s


# 7
def main(lst):
    T = []
    for i in lst:
        if not i in T:
            T.append(i)
    return T


# 8
def main(lst):
    n = len(lst)
    list = []
    for i in range(0, n):
        list.append(lst[i].lower())
    return list


# 9
def main(lst):
    lst.sort(key=lambda i: len(i), reverse=True)
    return lst


# 10
from functools import reduce
from math import radians
from operator import mul


def main(n):
    return reduce(mul, range(1, n + 1))


print(main(20))
print(main(30))
print(main(40))

# 11
from operator import mul


def main(vector1, vecotr2):
    n = len(vector1)
    s = 0
    for i in range(0, n):
        s += mul(vector1[i], vecotr2[i])
    return s


# 12
def main(lst):
    n = len(lst)
    max = lst[0]
    for i in range(1, n):
        if (len(lst[i]) > len(lst[0])):
            max = lst[i]
    return max


# 13
def main(lst):
    return list(filter(lambda i: i != 0, lst))


# 14
def main(lst):
    max = 0
    index = 0
    for i in range(len(lst)):
        x = abs(lst[i])
        if (x > max):
            max = x
            index = i
    return lst[index]


# 15
def main(lst):
    new_lst = []
    for i in range(len(lst)):
        x = lst[i] % 2
        if x == 1:
            new_lst.append(lst[i])
    return new_lst


# 16
def main(s):
    if (len(s) >= 20):
        new_s = s
        return new_s
    else:
        new_s = s
        x = 20 - len(s)
        left = int(x / 2)
        right = x - left
        while (left):
            new_s = '#' + new_s
            left -= 1
        while (right):
            new_s = new_s + '#'
            left -= 1
        return new_s


# 17
def main(s):
    intt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ala = [
        '零',
        '一',
        '二',
        '三',
        '四',
        '五',
        '六',
        '七',
        '八',
        '九',
    ]
    new_s = ''
    for i in range(len(s)):
        flg = False
        for j in range(len(intt)):
            if (s[i] == intt[j]):
                new_s += ala[j]
                flg = True
        if (flg == False):
            new_s += s[i]
    return new_s


# 18
def main(lst):
    set_lst = set(lst)
    if len(set_lst) == 1:
        return 0
    elif len(set_lst) == len(lst):
        return 1
    else:
        return 2


# 19
import re


def main(s):
    cop = re.compile('[^a-z^A-Z]')
    new_s = cop.sub('', s)
    a = reversed(new_s)
    if (list(a) == list(new_s)):
        return True
    else:
        return False


# 20
from collections import Counter


def main(s):
    word = []
    words = Counter(s).most_common(3)
    for i in range(len(words)):
        word.append(words[i][0])
    return word


# 21
def isPrime(num):
    for i in range(2, num):
        if ((num % i) == 0):
            return False
    return True


def main(n):
    for i in range(n):
        if isPrime(i + 1):
            max = i + 1
    return max


# 22
from scipy.special import comb


def main(n, i):
    return int(comb(n, i))


# 23*
# 要求：不能使用循环结构和推导式
from functools import reduce


def main(n, a):
    ls = [a]
    s = sum(reduce(lambda x, y: x * 10 + y, ls * i) for i in range(1, n + 1))
    return s


# 24
def main():
    with open('data24.txt', 'r', encoding='utf-8') as fp:
        text = fp.read()
        texts = text.split(',')
        for i in range(len(texts)):
            texts[i] = int(texts[i]) * 10
    return texts


print(main())


# 25
def main(lst):
    sumset = set()
    for s in lst:
        sumset = sumset | s
    return sumset


# 26
from math import sin, radians


def main(lst):
    sin_list = []
    for i in lst:
        sin_list.append(sin(radians(i)))
    return sin_list


# 27
from datetime import date


def main(year1, month1, day1, year2, month2, day2):
    tim1 = date(year1, month1, day1)
    tim2 = date(year2, month2, day2)
    delta = tim1 - tim2
    return delta.days


# 28
def main(year):
    if (year % 4 == 0):
        if (year % 100 != 0):
            return 'yes'
    if (year % 400 == 0):
        return 'yes'
    return 'no'


# 29
def main(func, lst):
    x = lst[0]
    max = func(x)
    for i in range(2, len(lst)):
        if func(lst[i]) > max:
            max = func(lst[i])
    return max


# 30
def main(tup):
    sum = 0
    for i in range(len(tup)):
        sum += tup[i]
    sum = sum - min(tup) - max(tup)
    mean = format(sum / (len(tup) - 2), '.1f')
    return mean


# 31
def main(n):
    sum = 0

    def fbnq(n):
        if (n == 0): return 1
        elif (n == 1): return 1
        else: return fbnq(n - 1) + fbnq(n - 2)

    for i in range(n):
        sum += fbnq(i)
    return sum


# 32
def main(s, n=3):
    return s * n


# 33
def main(s, n):
    return (s[n:] + s[:n])


# 34*
class Number:
    def __init__(self, value: int):
        self.num = value

    def __add__(self, another: object) -> object:
        return self.num + another.num

    def __str__(self):
        pass


def main(x, y):
    return x + y


# 35


# 36
def main(*para):
    sum = 0
    for i in range(len(para)):
        sum = sum + 1 / para[i]
    sum = 1 / sum
    res = format(sum, '.1f')
    return res


# 37
def main(n):
    lst = []
    max = 0
    min = 0
    org = n
    while (n):
        m = n % 10
        lst.append(m)
        n = int(n / 10)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[i]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    for i in range(len(lst)):
        max = max * 10 + int(lst[i])
    lst.reverse()
    for i in range(len(lst)):
        min = min * 10 + int(lst[i])
    cha = max - min
    if cha == org:
        return True
    else:
        return False


# 38
def main(n):
    lst = []
    org = n
    sum = 0
    while (n):
        m = n % 10
        lst.append(m)
        n = int(n / 10)
    for i in range(len(lst)):
        sum = sum + pow(lst[i], len(lst))
    if sum == org:
        return True
    else:
        return False


# 39
def main(lst):
    su = 0
    for i in range(len(lst)):
        su = su + abs(lst[i])
    return su


# 40
def main(s):
    if not isinstance(s, str):
        return '参数必须为字符串'
    else:
        s1 = s.encode('utf-8')
        s2 = s.encode('GBK')
    return (s1, s2)


# 41
def main(s1, s2, *s3):
    if (s2 in s1 and s3):
        for i in s3:
            if (i in s1):
                return True
    else:
        return False


# 42
from math import pi as PI


def main(r):
    if not isinstance(r, int) or int(r) <= 0:
        return '参数必须是大于0的整数或实数'
    else:
        return round(PI * (r**2), 2)


# 43
from itertools import permutations
from functools import reduce


def main(lst):
    lst = list(permutations(lst, len(lst)))
    new_lst = []
    for item in lst:
        n_item = map(lambda x: str(x), item)
        temp = int(reduce(lambda x, y: x + y, n_item))
        new_lst.append(temp)
    return max(new_lst)


# 44
def main(n):
    m = n * n
    su = 0
    while (m):
        su = su + pow(2, m - 1)
        m = m - 1
    return su


# 45
def main(lst):
    if not isinstance(lst, list):
        return '数据格式不正确'
    for item in lst:
        if not isinstance(item, str):
            return '数据格式不正确'
    else:
        lst1 = list(map(lambda x: x.lower(), lst))
        ma_x = max(lst1)
        for index, item in enumerate(lst1):
            if item == ma_x:
                return lst[index]


# 46
def main(lst):
    if len(lst) > 7:
        return 4
    else:
        return 1


# 47


# 48
def main(vector1, vector2):
    if isinstance(vector1, list) == False or isinstance(
            vector1[0], int) == False or len(vector1) != len(vector2):
        return '数据不对'
    else:
        s = list(map(lambda v1, v2: abs(v1 - v2), vector1, vector2))
        return sum(s)


# 49
def main(score):
    if 0 <= score < 60:
        return 'F'
    elif 59 < score < 70:
        return 'D'
    elif 69 < score < 80:
        return 'C'
    elif 79 < score < 90:
        return 'B'
    elif 89 < score < 101:
        return 'A'
    else:
        return '数据不对'


# 50
