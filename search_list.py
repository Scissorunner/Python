lst = [1, 2, 3, 4, 7, 6, 5, 8, 9, 10]
lst.sort()
print(lst)
first = 0
last = len(lst) - 1
mid = (first + last) // 2
print(f"List start:{first}  List middle:{mid}  List end:{last}")
item = int(input("Enter the number you're searching for: "))
found = False
while first <= last and not found:
    mid = (first + last) // 2
    if lst[mid] == item:
        print(f"Found at location: {mid}")
        found = True
    else:
        if item < lst[mid]:
            last = mid - 1
            print("last", last)
        else:
            first = mid + 1
            print("first", first)
if found == False:
    print("Number not found")