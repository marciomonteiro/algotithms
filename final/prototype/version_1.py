from random import randint
import sys

def check_result(container, container_size):
    print("=====================")
    print("Number of used containers: ", len(container))
    occupied_space = 0
    total_space = len(container)*container_size
    occupied_space = sum(container)
    print("total - occupied/free (usage%): ", total_space," - ", occupied_space, "/",  total_space - occupied_space, " (", "%.2f" % (100*occupied_space/total_space) ,")" )
    print("=====================\n")


def first_fit_unordered(obects, container, container_size):
    container.insert(len(container), 0)
    bottom = 0
    top = 0
    for obj in objects[:]:
        fit_container = bottom 
        for cont in container[bottom:top+1]:
            if cont + obj > container_size:
                fit_container+=1
            else:
                break

        if fit_container == len(container):
            container.insert(len(container), 0)
            top+=1

        container[fit_container] += obj

        if container[fit_container] == container_size :
            container[bottom], container[fit_container] = container[fit_container], container[bottom]
            bottom+=1

def first_fit_ordered(obects, container, container_size):
    container.insert(len(container), 0)
    for obj in objects[:]:
        if container[len(container)-1] + obj > container_size:
            container.insert(len(container), 0)
        
        container[len(container)-1] += obj
        
def biggest_n_smallest(obects, container, container_size):
    smallest = 0
    biggest = len(objects)-1

    while smallest <= biggest :
        container.insert(len(container), 0)
        while smallest <= biggest and objects[biggest] + container[len(container)-1] <= container_size :
            container[len(container)-1] += objects[biggest]
            biggest-=1

        while smallest <= biggest and objects[smallest] + container[len(container)-1] <= container_size :
            container[len(container)-1] += objects[smallest]
            smallest+=1
            
# = first_fit_ordered
# def smallest_n_biggest(obects, container, container_size):
#   smallest = 0
#   biggest = len(objects)-1

#   while smallest <= biggest :
#     container.insert(len(container), 0)

#     while smallest <= biggest and objects[smallest] + container[len(container)-1] <= container_size :
#       container[len(container)-1] += objects[smallest]
#       smallest+=1

#     while smallest <= biggest and objects[biggest] + container[len(container)-1] <= container_size :
#       container[len(container)-1] += objects[biggest]
#       biggest-=1


n = 1000
container_size = 256
container = []
objects = [ randint(1, container_size) for i in range(n) ]
print("Cargo size: ", sum(objects), "\n")
print("first_fit_unordered")
first_fit_unordered(objects, container, container_size)
check_result(container, container_size)

container = []
objects.sort()
print("first_fit_ordered")
first_fit_ordered(objects, container, container_size)
check_result(container, container_size)

container = []
print("biggest_n_smallest")
biggest_n_smallest(objects, container, container_size)
check_result(container, container_size)

# container = []
# print("smallest_n_biggest")
# smallest_n_biggest(objects, container, container_size)
# check_result(container, container_size)