from numpy.random import uniform, normal, triangular
import random

import matplotlib.pyplot as plt

def sanity_check(containers, max_size):
    if len([ x for x in containers if x > max_size]):
        print("Deu ruim / give bad")

def rand(dist, max_size):
    if(dist == "uniform"):
        return int(uniform(1, max_size))
    elif(dist == "normal"):
        return abs(int(normal(max_size/2, max_size/5))) % 1000
    elif(dist == "linear_dec"):
        return int(triangular(1, 1, max_size))
    elif(dist == "linear_inc"):
        return int(triangular(1, max_size, max_size))

def generate_solution(num_container, max_size, dist):
    objects = []
    for i in range(num_container):
        current_size = max_size;
        while current_size >= 1:
            object_size = rand(dist, max_size)
            if((current_size - object_size)>=0):
                objects.append(object_size)
                current_size = current_size - object_size
            else:
                break
        if current_size!=0 :
            objects.append(current_size)
    return objects

def check_result(container, max_size):
    print("=====================")
    print("Number of used containers: ", len(container))
    occupied_space = 0
    total_space = len(container)*max_size
    occupied_space = sum(container)
    print("total - occupied/free (usage%): ", total_space," - ", occupied_space, "/",  total_space - occupied_space, " (", "%.2f" % (100*occupied_space/total_space) ,")" )
    print("=====================\n")

def first_fit(objects, max_size):
    containers = []
    for obj in objects:
        choosen_container_index = 0
        for c_index in range(0,len(containers)):
            if containers[c_index] + obj <= max_size:
                break
            else:
                choosen_container_index +=1
        if choosen_container_index < len(containers):
            containers[choosen_container_index] += obj
        else:
            containers.append(obj)
    return containers

def first_fit_ascending_sort(objects, max_size):
    objects.sort()
    return first_fit(objects, max_size)

def first_fit_descending_sort(objects, max_size):
    objects.sort(reverse=True)
    return first_fit(objects, max_size)

def biggest_n_smallest(objects, max_size):
    objects.sort()
    containers = []
    smallest_index = 0
    biggest_index = len(objects)-1

    while smallest_index <= biggest_index :
        container = 0
        while smallest_index <= biggest_index and objects[biggest_index] + container <= max_size :
            container += objects[biggest_index]
            biggest_index -= 1

        while smallest_index <= biggest_index and objects[smallest_index] + container <= max_size :
            container += objects[smallest_index]
            smallest_index += 1
        containers.append(container)
    return containers

def experiment(objects, max_size):
    print("first_fit:")
    ff_containers = first_fit(objects[:], max_size)
    sanity_check(ff_containers, max_size)
    check_result(ff_containers, max_size)

    print("first_fit_ascending_sort:")
    ff_as_ord_containers = first_fit_ascending_sort(objects[:], max_size)
    sanity_check(ff_as_ord_containers, max_size)
    check_result(ff_as_ord_containers, max_size)

    print("first_fit_descending_sort:")
    ff_des_ord_containers = first_fit_descending_sort(objects[:], max_size)
    sanity_check(ff_des_ord_containers, max_size)
    check_result(ff_des_ord_containers, max_size)

    print("biggest_n_smallest:")
    bs_containers = biggest_n_smallest(objects[:], max_size)
    sanity_check(bs_containers, max_size)
    check_result(bs_containers, max_size)

n_objects = 1000
max_size = 1000
n_containers = 500

print("uniform ==============================")
# objects = [ int(uniform(1, max_size)) for i in range(n_objects) ]
objects = generate_solution(n_containers, max_size, "uniform")
random.shuffle(objects)
# print(objects)
# plt.hist(objects, bins = 150, normed=True)
# plt.show()
experiment(objects, max_size)

print("normal ==============================")
# objects = [ abs(int(normal(max_size/2, max_size/5))) % 1000 for i in range(n_objects) ]
objects = generate_solution(n_containers, max_size, "normal")
random.shuffle(objects)
# print(objects)
# plt.hist(objects, bins = 150, normed=True)
# plt.show()
experiment(objects, max_size)

print("linear_dec ==============================")
# objects = [ int(triangular(1, 1, max_size)) for i in range(n_objects) ]
objects = generate_solution(n_containers, max_size, "linear_dec")
random.shuffle(objects)
# print(objects)
# plt.hist(objects, bins = 150, normed=True)
# plt.show()
experiment(objects, max_size)


print("linear_inc ==============================")
# objects = [ int(triangular(1, max_size, max_size)) for i in range(n_objects) ]
objects = generate_solution(n_containers, max_size, "linear_inc")
random.shuffle(objects)
# print(objects)
# plt.hist(objects, bins = 150, normed=True)
# plt.show()
experiment(objects, max_size)
