import csv
from itertools import accumulate
from itertools import takewhile


max_weight = 400
itemlist = []

with open('items.csv') as csvfile:
    csvfile.readline()
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        itemlist.append(row)

sorted_list = list(reversed(sorted(itemlist,
                            key=(lambda item:
                                 int(item[2]) / int(item[1])))))
running_add = takewhile(lambda z: z < max_weight,
                        (accumulate([int(i[1]) for i in sorted_list])))
print(sorted_list[0: len(list(running_add))])
