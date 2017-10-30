import os

my_path = '/home/hasnat/caffe/'

print(my_path)

list_dirs = mydirs = filter(os.path.isdir, os.listdir(my_path))

list_dirs_2 = [ x for x in os.listdir(my_path) if os.path.isdir(x) ]

print(list_dirs)
print(list_dirs_2)
