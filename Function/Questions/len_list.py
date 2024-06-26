#function to calculate the length of the list

#first way
def calc_len(a,b,c,d,e):
    li = [a,b,c,d,e]
    count = 0
    for i in li:
        count += 1
    return count

print(calc_len(1,2,3,4,5)) #5

print()





#second way
#defining list
lis = ["Aditya", "Mahir", 8, 3]

#defining function
def len_li(lis):
    counts = 0
    for i in lis:
        counts += 1
    return counts
print(len_li(lis)) #4





#third way
#defining function and passing list as parameter
def length(lt):
    count = 0
    for i in lt:
        count += 1
    return count

print(length([1,2,3,4,5])) #5





#fourth way
def lg(list = []):
    count = 0
    for i in list:
        count += 1
    return count

print(lg([1,2,3,4,5,8])) #5