# Compact version
# ---------------
rule = (('0'*8 + bin(30)[2:])[-8:])[::-1]
cells = list('0'*40 + '1' + '0'*40)
for epoch in range(40):
    print(''.join(cells).replace("0"," ").replace("1","█"))
    cells = [cells[0]] + [rule[eval('0b' + cells[i-1]+cells[i]+cells[i+1])]
                          for i in range(1,len(cells)-1)] + [cells[-1]]

"""
# Readable version
# ----------------
# Rule transformation into ascii/binary representation
rule = 30
rule = ('0'*8 + bin(rule)[2:])[-8:]
rule = rule[::-1]

# Cells
p = 40
cells = '0'*p + '1' + '0'*p

# Iteration over epoch
n = 40
for epoch in range(n):
    # Display
    t = ''.join(cells)
    t = t.replace("0", " ")
    t = t.replace("1", "█")
    print(t)

    # Iteration over local neighborood
    _cells = []
    for i in range(1,len(cells)-1):
        code = cells[i-1]+cells[i]+cells[i+1]
        code = eval('0b' + code)
        _cells.append(rule[code])
    cells = [cells[0]] + _cells + [cells[-1]]
"""
