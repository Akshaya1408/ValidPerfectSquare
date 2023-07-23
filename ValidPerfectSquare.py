def validSquare(num):
    square=int(num**0.5)
    if square*square==num:
        return True
    return False

num=int(input())
print(validSquare(num))