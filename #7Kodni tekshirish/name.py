
def get_full_name(ism,familiya,otasi=""):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

def get_big(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


def list_title(values):
    names=[]
    for value in values:
        names.append(value.title())
    return names

def  couple_number(numbers):
    couple=[]
    for n in numbers:
        if n%2==0:
            couple.append(n)
    return couple
            
# def fibonacci(number):
#     fibon=[]
#     numbers=list(range(number+2))
#     for num in numbers:
#         if num==0:
#             fibon.append(num)
#         elif num>0 and num<2:
#             fibon.append(num)
#         else:
#             fibon.append(fibon[-1]+fibon[-2])
#             if fibon[-1]>number:
#                 break
#     return number in fibon

def fibonacci(number):
    fibon = [0, 1]
    while True:
        next_fib = fibon[-1] + fibon[-2]
        if next_fib > number:
            break
        fibon.append(next_fib)
    return number in fibon

print(fibonacci(2))


     

