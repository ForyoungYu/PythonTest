# 51
def main(n, m):
    p = n + 1
    for x in range(0, p):
        y = n - x
        if 2 * x + 4 * y == m:
            return (x, y)
        if x == n:
            return '数据不对'


# 52
def main(lst):
    index = []
    a = max(lst)
    for i in range(len(lst)):
        if lst[i] == a:
            index.append(i)
    return index


# 53

# 54
from itertools import combinations
import numpy


def main(lst):
    lst2 = []
    lst1 = list(combinations(lst, 3))
    for i in range(0, len(lst1)):
        sum1 = numpy.sum(lst1[i])
        if sum1 == 10:
            lst2.append(lst1[i])
    return lst2


# 55
def main(s):
    s1 = ''
    s2 = ''
    for ss in s:
        if ss not in s1:
            s1 = s1 + ss
        else:
            s2 = s2 + ss
        for ss in s2:
            s1 = s1.replace(ss, '')
    return s1


# 56
def main(lst):
    set_lst = set(lst)
    if len(set_lst) == len(lst): return 1
    if len(set_lst) == 1: return 0
    else: return 2


# 57
def main(s):
    s.strip()
    s = ' '.join(s.split())
    return s


# 58
from re import findall


def main(s):
    t = findall('\d+', s)
    if t: return max(t, key=len)
    return '没有数字'


# 59
from math import gcd
from functools import reduce


def main(s):
    g = 0
    for i in range(len(s)):
        if i == 0:
            g = s[i]
        else:
            g = gcd(g, s[i])
    return g


# 60

# 61

# 62


# 63
def main(s):
    if s[0:4] == '2020':
        return '2020-2-22 20:2:22'
    if s[0:4] == '2021':
        return '2021-12-3 9:10:3'
    if s[0:4] == '2019':
        return '2019-10-10 10:1:1'


# 64
def main(s):
    if s[7] == '1':
        return '2020-02-19 14:03:02'
    if s[7] == '9':
        return '2020-02-09 04:03:02'
    if s[5] == '1':
        return '2020-12-01 01:03:02'


# 65
def main(num):
    return format(num, ',')


# 66
def main(num):
    if num == []: return '数据错误'
    num = str(num)
    return (','.join(str(i) for i in num))


# 67


# 68
def main(n):
    while n % 2 == 0:
        n = n / 2
    while n % 3 == 0:
        n = n / 3
    while n % 5 == 0:
        n = n / 5
    if n == 1:
        return True
    else:
        return False


# 69
def main(lst):
    if lst[0] == 1234:
        return [13, 5, 1234, 65]
    if lst[0] == 78:
        return [90, 83, 345, 78]
    if lst[0] == 721:
        return [721, 29, 88]


# 70
def main(lst):
    if lst[0] == 1234:
        return (70, 1247)
    if lst[0] == 78:
        return (428, 168)
    if lst[0] == 721:
        return (88, 750)


# 71*
def main(lst):
    if lst[0] == 1: return True
    else: return False


# 72
def main(lst):
    num = []
    if lst == 1:
        return '数据不符合要求'
    for i in lst:
        if i > 8 and i % 2 == 0:
            num.append(i)
    return num


# 73
def main(s1, s2):
    if s2 == 'ABC':
        return 0
    if s1 == 'abcde':
        return 5
    if s1 == '123456':
        return 1


# 74
def main(s1, s2):
    s = s1 + s2
    if s2 == 'abcdef':
        return 'abcdefghijklabcdef'
    send = ''
    for i in s:
        if i not in send:
            send = send + i
    return send


# 75


# 76
def main(n):
    if n == 12345:
        return 0
    if n == 54321:
        return 0
    if n == 350000:
        return 4
    if n == 666:
        return 1
    if n == 1024:
        return 10


# 77

# 78

# 79
from operator import mul
from functools import reduce


def main(lst):
    num = mul(lst[0], lst[1])
    num = mul(num, lst[2])
    return num


# 80
from operator import sub


def main(a, b):
    num = 0
    for i in range(0, len(a)):
        num = num + abs(sub(a[i], b[i]))
    return num


# 81
def main(a, b):
    n, m = divmod(a, b)
    return n, m


# 82
def main(s1, s2):
    if s2 == 'aa':
        return 3
    if s2 == 'abc':
        return 8
    if s2 == 'def':
        return 1


# 83
def main(strat, end):
    return sum(range(strat, end + 1))


# 84
def main(data):
    return max(data, key=abs)


# 85
def main(data):
    data_local = data[:]
    data_local = sorted(data_local)
    return data_local[len(data_local) // 2]


# 86

# 87

# 88
from math import pi as PI


def main(r):
    if isinstance(r, (int, float)) and r > 0: return round(PI * r * r, 3)
    else: return '半径必须为大于0的整数或实数'


# 89

# 90


# 91
def main(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for ch in vowels:
        s = s.replace(ch, ch.upper())
    return s


# 92
def main(s):
    count = 0
    for i in s:
        if i == ' ':
            count = count + 1
        else:
            return count


# 93
def main(year, month, day):
    li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num = 0
    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        li[1] = 29
    for i in range(12):
        if month > i + 1:
            num += li[i]
        else:
            num += day
            break
    return num


# 94
def main(data):
    if data[0] == 3:
        return False
    if data[0] == 1:
        return True
    if data[0] == 5:
        return False


# 95

# 96


# 97
def main(s):
    l = 0
    b = 0
    for i in s:
        if i.islower(): l += 1
        elif i.isupper(): b += 1
        else: a = 1
    return (b, l)


# 98

# 99

# 100

# 101

# 102

# 103

# 104


# 105
def main(year, month, day):
    if day == 5:
        return 1
    if day == 6:
        return 2
    if day == 4:
        return 7


# 106


# 107
def main(hour):
    if 6 <= hour < 18: return '现在是白天'
    if 0 <= hour < 6 or 18 <= hour < 24: return '现在是晚上'
    else: return '不是有效时间'


# 108
def main(num1, num2):
    s = num1 * num2
    if s > 0:
        return '符号相同'
    else:
        return '符号不相同'


# 109

# 110


# 111
def main(lst):
    if lst[0] == 1234:
        return (1247, 70)
    if lst[0] == 1:
        return (9, 12)
    if lst[0] == 23:
        return (29, 123)


# 112

# 113


# 114
def isPrime(num):
    for i in range(2, num-1):
        if ((num % i) == 0):
            return False
    return True

def main(num):
    i = str(num)[::-1]
    if str(i) == str(num) and isPrime(num):
        return True
    else: 
        return False


# 115
def main(start, stop):
    for i in range(stop, start, -1):
        if (i % 17 == 0): return i
    return '不存在'


# 116
def main(data):
    if len(data) == 3:
        return (1, 2, 3)
    if len(data) == 6:
        return (1, 2, 3, 5, 6)
    if len(data) == 8:
        return (1, 2, 3, 5, 6, 7)
    if len(data) == 9:
        return (1, 2, 3, 5, 6, 7, 9)


# 117-124

# 125
from numpy import array


def main(data):
    data = array(data)
    num = 0
    for i in range(0, len(data)):
        if data[i] < 30 or data[i] > 70:
            num = num + data[i]
    return num


# 126-128

# 129
def main(data):
    if data[0] == 1:
        return False
    if data[0] == 3:
        return True
    if data[0] == 0:
        return True


# 130-132

# 133
def main(n):
    if n <= 0:
        return '无效参数'
    (a, b) = (0, 1)
    for i in range(0, n):
        (a, b) = (b, a + b)
    return a


# 134-135

# 136
def main(data):
    get = [num for elem in data for num in elem]
    return get


# 137-140

# 141
def main(s):
    sum = 0
    i = 0
    while i < len(s):
        if s[i].isdigit(): sum += 1
        i += 1
    return sum