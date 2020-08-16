def filter_list(l):
    new_list = []
    for number in l:
        if str(number).isdigit() and str(number) != number:
            new_list.append(number)
    return new_list  # or [number for number in l if isinstance(number, int)


print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))
