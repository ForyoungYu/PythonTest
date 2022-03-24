# class Number:
#     def __init__(self, value: int):
#         self.num =  value
#     def __add__(self, another: object) -> object:
#         return Number(self.num + another.num)
#     def __str__(self):
#         return "对象加法"

# def main(x, y):
#     return x+y
# a = Number(3)
# b = Number(5)
# print(main(a, b))

def main(lst):
    sumset = set()
    for s in lst:
        sumset = sumset | s
    return sumset


a = {1, 2}
b = {2, 3}
list = [a, b]
print(main(list))
