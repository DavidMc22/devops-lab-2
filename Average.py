list = [4,6,2,9,2]
largest=0
smallest=1000000000

for num in list:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num

total=sum(list)
average= total/len(list)

print("The average is", average)
print("Largrest: ",largest)
print("Smallest: ",smallest)