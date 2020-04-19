list = [1,3,5,7,9,11,15]
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        midle = low + high
        guess = list[midle]
        if guess == list[midle]:
            return midle
        elif guess > item: # Значение больше 
            high = mid - 1
        else: # Значение меньше
            low = mid + 1
    return None # Значение не существует

print(binary_search(list,11))