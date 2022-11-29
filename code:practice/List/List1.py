

sample_list = [1,4,5,2,9,12]
for item in sample_list:
    print(item)
    
for index in range(len(sample_list)):
    print(index)

i = iter(sample_list)
item = i.__next__()
print(item)
item = i.__next__()
print(item)

list_sum = sum(sample_list)
print(list_sum)

subtotal = 23
total = sum(sample_list,subtotal)
print(total)

average = float(sum(sample_list))/len(sample_list)
print(average)

haka_list = ["Taringa", "whakarongo!", "Kia", "rite!", "Kia", "rite!"]
joined_list = ' '.join(haka_list)
print(joined_list)


list_time = len(sample_list)*sample_list[-1]
print(list_time)

sample_list.append(17)
print(sample_list)

sample_word = ["Hello", "Python"]
total_sample=sample_list+sample_word
print(total_sample)

