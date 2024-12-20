#%% binary_search function
def binary_search(item_list, item):
    '''binary_search(item_list, item) expects as list of integers
    as item_list and a number as item which needs to be guessed.'''
    item_list.sort()
    low = 0
    high = len(item_list)-1

    guess_count = 0
    while low <= high:
        mid = (low + high) // 2
        guess = item_list[mid]
        guess_count += 1
        if guess == item:
            return guess, guess_count
        if guess > item:
            # subtract one from mid to not check it again
            high = mid -1
        else:
            # add one from mid to not check it again
            low = mid +1
    return None

#%% test binary_search()
from random import randrange

item_list = [i for i in range(8,601)]
item = randrange(8, 600)
guess, guess_count = binary_search(item_list, item)
print(guess, guess_count, item)
