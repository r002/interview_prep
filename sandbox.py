count = 999

def hello_world():
    # count += 1
    print(f"Hello Universe! {count}")

hello_world()


plus_count = 0
neg_count = 0
zero_count = 0

def categorize(x):
    global plus_count
    global neg_count
    global zero_count

    if x > 0:
        plus_count += 1
        return 1
    elif x < 0:
        neg_count += 1
        return -1
    else:
        zero_count += 1
        return 0

alist = [-2, 3, 0, 5, 10, -99, 72]
rs = list(map(categorize, alist))

print(alist)
print(rs)
print(f"Plus count: {plus_count}")
print(f"Neg count: {neg_count}")
print(f"Zero count: {zero_count}")
print()
print()

alist = [-2, 3, 0, 5, 10, -99, 72]
plus_list = list(filter(lambda x : x > 0, alist))
neg_list = list(filter(lambda x : x < 0, alist))
zero_list = list(filter(lambda x : x == 0, alist))

print(f"plus_list: {plus_list} | {len(plus_list)}")
print(f"neg_list: {neg_list} | {len(neg_list)}")
print(f"plus_list: {zero_list} | {len(zero_list)}")
