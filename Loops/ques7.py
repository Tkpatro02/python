items=["apple" , "banana","orange","mango"]

unique_item=set()

for item in items:
    if item in unique_item:
        print("duplicate")
        break
    unique_item.add(item)