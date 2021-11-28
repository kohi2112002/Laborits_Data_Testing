import json
import random

base = '01c619b13901cb61619c901cb619c7523901c619b13901cb61619c901cb619b61619c901cb619c7523901c619b13901cb61619c901cb619c7523901c619b13901cbc7523901c619b13901cb619c901cb619c7523901cb6199019c901cb619c7523901cb619901cb619c901cb619c752390c901cb61256edd'
base_lst = [x for x in base]
check_lst = []
cate_lst = ['Sales & Marketing', 'UI-UX', 'Cybersecurity', 'Data Collecting and Researching', 'Software Development']
count = 0

with open("D:/Laborits_Data_Testing/Data Gen Test/task_gen_test_300.json", 'r') as file:
    data = json.load(file)

for x in data:
    count += 1
    random.shuffle(base_lst)
    x['_id']['$oid'] = ''.join(base_lst[:24])

print(count)
count = 0

with open('D:/Laborits_Data_Testing/Data Gen Test/task_gen_test_3000_new.json', 'w') as f:
    json.dump(data, f)


# with open("D:/Laborits_Data_Testing/Skills_PC.json", 'r') as file:
#     data = json.load(file)

# for x in data:
#     count += 1
#     random.shuffle(base_lst)
#     x['_id']['$oid'] = ''.join(base_lst[:24])
#     x['Category'] = cate_lst[random.randint(0,4)]

# with open('Partner_FN.json', 'w') as f:
#     json.dump(data, f)

# print(count)
