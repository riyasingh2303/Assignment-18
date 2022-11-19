l1_keys = [11,12,13,14,15]
l2_values = ["SQL","javascript","C","C++","java"]
print("key list is :"+str(l1_keys))
print("value list is :"+str(l2_values))
res = dict(zip(l1_keys,l2_values))
print("result:"+str(res))