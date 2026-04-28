#range fuction 

# for number in range(1, 11,3):
#     print(number)
    
#gaus challange

total = 0

gaus = list(range(1, 101))


total = len(gaus) * (len(gaus) +1) / 2
print(total)

for number in gaus:
    total += number
    
print(total/2)
