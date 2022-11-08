#List3-9.py
#author:amy
#date:08.11.22

list = ["land of", "the", "the long white cloud"]

joined_list = " ".join(sorted(list, key=len))
print(joined_list)
