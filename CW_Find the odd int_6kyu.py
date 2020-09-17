def find_it(seq):
    slovar = {}
    for value in seq:
        if value not in slovar:
            slovar[value] = 0
        slovar[value] += 1
    for odd in slovar:
        if slovar[odd] % 2 != 0:
            return odd


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))
print(find_it([10]))
