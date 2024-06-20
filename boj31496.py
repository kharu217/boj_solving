count, del_item = input().split()
count = int(count)

result = 0

for i in range(count) :
    item, item_cnt = input().split()
    item = item.split('_')
    item_cnt = int(item_cnt)

    if del_item in item :
        result += item_cnt


print(result)
