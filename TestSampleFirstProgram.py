# print("Hello")
# a=10
# b=10
# print(a+b)

# for i in range(1, 6):
#
#     if i == 3:
#
#         continue
#
#     print(i)

# def greet(name="Guest"):
#
#     print("Hello,", name)
#
# greet()

# def multiply(a, b=2):
#
#     return a * b
#
# print(multiply(3))
# def square(x):
#
#     return x ** 2
#
# numbers = [1, 2, 3, 4, 5]
#
# squared_numbers = map(square, numbers)
#
# print(list(squared_numbers))
# def greet():
#
#     print("Hello")
#
# greet

# def multiply(a, b):
#
#     return a * b
#
# result = multiply(3, 4)
# def modify_list(lst):
#
#     lst.append(4)
#
# numbers = [1, 2, 3]
#
# modify_list(numbers)
#
# print(len(numbers))
def mystery(x):

    if x == 0:

        return 1

    return x * mystery(x - 1)

print(mystery(5))