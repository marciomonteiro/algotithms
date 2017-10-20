from random import randint
import sys

def sanity_check(containers, container_size):
    if len([ x for x in containers if x > container_size]):
        print("Deu ruim / give bad")

def check_result(container, container_size):
    print("=====================")
    print("Number of used containers: ", len(container))
    occupied_space = 0
    total_space = len(container)*container_size
    occupied_space = sum(container)
    print("total - occupied/free (usage%): ", total_space," - ", occupied_space, "/",  total_space - occupied_space, " (", "%.2f" % (100*occupied_space/total_space) ,")" )
    print("=====================\n")

def first_fit(objects, container_size):
    containers = []
    for obj in objects:
        choosen_container_index = 0
        for c_index in range(0,len(containers)):
            if containers[c_index] + obj <= container_size:
                break
            else:
                choosen_container_index +=1
        if choosen_container_index < len(containers):
            containers[choosen_container_index] += obj
        else:
            containers.append(obj)
    return containers

def first_fit_ascending_sort(objects, container_size):
    objects.sort()
    return first_fit(objects, container_size)

def first_fit_descending_sort(objects, container_size):
    objects.sort(reverse=True)
    return first_fit(objects, container_size)


def biggest_n_smallest(objects, container_size):
    objects.sort()
    containers = []
    smallest_index = 0
    biggest_index = len(objects)-1

    while smallest_index <= biggest_index :
        container = 0
        while smallest_index <= biggest_index and objects[biggest_index] + container <= container_size :
            container += objects[biggest_index]
            biggest_index -= 1

        while smallest_index <= biggest_index and objects[smallest_index] + container <= container_size :
            container += objects[smallest_index]
            smallest_index += 1
        containers.append(container)
    return containers


n_objects = 100
container_size = 1000
objects = [ randint(1, container_size) for i in range(n_objects) ]

print("first_fit:")
ff_containers = first_fit(objects[:], container_size)
sanity_check(ff_containers, container_size)
check_result(ff_containers, container_size)

print("first_fit_ascending_sort:")
ff_as_ord_containers = first_fit_ascending_sort(objects[:], container_size)
sanity_check(ff_as_ord_containers, container_size)
check_result(ff_as_ord_containers, container_size)

print("first_fit_descending_sort:")
ff_des_ord_containers = first_fit_descending_sort(objects[:], container_size)
sanity_check(ff_des_ord_containers, container_size)
check_result(ff_des_ord_containers, container_size)

print("biggest_n_smallest:")
bs_containers = biggest_n_smallest(objects[:], container_size)
sanity_check(bs_containers, container_size)
check_result(bs_containers, container_size)
