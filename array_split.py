#Need to write function to split array into diff chunk sizes
#Write custom implementation of list function.
#HOW THO


#amount - how many terms you want after the list has been split
#arr - the list to be split
def split(arr: list, amount:int) -> list:
    new_arr = []
    n = len(arr)
    chunk_size = n//amount
    for x in range (0,amount):
        new_arr.append(arr[x*chunk_size:(x+1)*chunk_size])
    return new_arr

names = ["Turner", "Jack", "Alex", "Babatunde", "Tyrone", "Taqauvion Johnson", "Baracuda", "David Goggins"]
print(split(names, 4))