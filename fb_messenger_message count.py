import json
from Tkinter import filedialog
from filedialog import askopenfilename
import matplotlib.pyplot as plt

# change file name

filepath = askopenfilename()

with open(filepath) as f:
    data = json.load(f)

sender_list = []
for each in data['messages']:
    sender_list.append(each['sender_name'])

name_list = []
for each in data['participants']:
    name_list.append(each['name'])

first_name_list =[]
for each in name_list:
    first_name_list.append(each[:each.find(" ")])
    
count_list = []
for each in name_list:
    s = 0
    s=sender_list.count(each)
    count_list.append(s)

name_count = dict(zip(first_name_list,count_list))

plt.figure(figsize=(20, 10))
plt.bar(name_count.keys(),name_count.values(), align = 'center')
plt.xlabel('User')
plt.ylabel('Number of messages')
plt.title('Number of messages over downloaded period')
