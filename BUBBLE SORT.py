#BUBBLE SORT
print(">>> BUBBLE SORT")
print("")#....space
print("This sorts the list using bubble sort technique")
print("")#...space

def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range (len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j] , lst[j+1] = lst[j + 1], lst[j]
            return lst

list1 = [5,3,8,6,7,6]
print("---The unsorted list is:", list1)
print("---The sorted list is",bubble_sort(list1))
