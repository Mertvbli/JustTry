def get_middle(s):
    dlina = len(s)
    if dlina % 2 == 0:
        dlina = len(s) // 2
        return s[dlina - 1:dlina + 1]
    if dlina % 2 != 0:
        dlina = len(s) // 2
        return s[dlina:dlina + 1]

# another method
# return s[(len(s)-1)/2:len(s)/2+1]


print(get_middle("test"))
print(get_middle("pelokpina"))
