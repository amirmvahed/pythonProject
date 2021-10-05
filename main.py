# Lists
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# zeros = [0] * 5
# matrix = [[1, 2], [0, 5]]
# numbers = list(range(20))
# combine = zeros + letters
# chars = list('Hello World')
# print(chars)
# print(letters[2])
# print(letters[0:1])
# print(letters[0:4])
# print(letters[0:7:2])
# print(letters[::2])
# print(letters[1:])
# print(letters[:3])

# numbers = [0, 1, 2]
# first, second, third = numbers
# instead of
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# first, second, *others = numbers
# print(first)
# print(others)

# letters = ['a', 'b', 'c']
#
# for index, letter in enumerate(letters):
#     print(index, letter)


# Add or Remove in list

# letters = ['a', 'b', 'c']
# # Add
# letters.append('d')
# letters.insert(1, '-')
#
# # Delete
# letters.pop(3)
# # first b, if you need to delete all b use for loop
# letters.remove('b')
# del letters[0:2]
# print(letters)

# Finding an items
# letters = ['a', 'b', 'c']
# print(letters.count('b'))
#
# if 'd' in letters:
#     print(letters.index('d'))

# Sorting List
# numbers = [1, 10, 68, 4, 51]
# numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

# Sorting items
# items = [
#     ('card1', 16),
#     ('card2', 10),
#     ('card3', 13),
# ]
#
# # lambda function
# # lambda parameters:expression
# items.sort(key=lambda item: item[1])
#
#
# # instead
# def item_sort(item):
#     return item[1]
#
#
# items.sort(key=item_sort, reverse=True)
# print(items)

# Map function
# items = [
#     ('card1', 16),
#     ('card2', 10),
#     ('card3', 13),
# ]
# prices = list(map(lambda item: item[1], items))
# print(prices)

# filter function
# items = [
#     ('card1', 16),
#     ('card2', 10),
#     ('card3', 13),
# ]
# prices = list(filter(lambda item: item[1] > 11, items))
# print(prices)

# List comprehension
# items = [
#     ('card1', 16),
#     ('card2', 10),
#     ('card3', 13),
# ]
# # [expression for item in items]
# print([item[1] for item in items])
# # instead map
#
# print([item for item in items if item[1] > 11])
# # instead filter

# zip function
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# print(list(zip('abc', list1, list2)))
#
# # instead
# list3 = [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]

# Stack lifo(last in first out)
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.pop()
# if not browsing_session:
#     browsing_session[-1]

# Queue fifo(first in first out)
# from collections import deque
#
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print('Empty')
