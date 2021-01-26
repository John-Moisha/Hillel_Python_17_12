def integer_as_roman(integer: int) -> str:
    i = integer
    i = "I" * i

    i = i.replace("I" * 5, "V") # 5
    i = i.replace("V" * 2, "X") # 10
    i = i.replace("X" * 5, "L") # 50
    i = i.replace("L" * 2, "C") # 100
    i = i.replace("C" * 5, "D") # 500
    i = i.replace("D" * 2, "M") # 1000

    i = i.replace("DCCCC", "CM")
    i = i.replace("CCCC", "CD")
    i = i.replace("LXXXX", "XC")
    i = i.replace("XXXX", "XL")
    i = i.replace("VIIII", "IX") #9
    i = i.replace("IIII", "IV")

    return i

print(integer_as_roman(199))