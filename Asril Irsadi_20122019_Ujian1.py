# print('#-#-# No. 1 #-#-#')
# def Hashtag(string):
#     result = "#"
#     if string != "":
#         for item in string.split():
#             result += item.title()
#         if len(result)>0 and len(result)<140:
#             pass
#         else:
#             result = False
#     else:
#         result = False
#     print(result)

# Hashtag("nkqsqhiwnldmwmwmljwndwlmlmwlsmlwmswmslwjsoisjmlmslmwiswldlwdnwndnwldm;wmopqjq99228nm/.M,LX WX X SX K WK XJWKNSKJBlsmlwmswmslwjsoisjmlmslmwiswldlwdnwndnwldm;wmopqjq99228nm/.M,LX WX X SX K WK XJWKNSKJB")
# Hashtag(" Hello there how are you doing")
# Hashtag("  Hello  World  ")
# Hashtag("")

# print('#-#-# No. 2 #-#-#')
# def create_phone_number(number):
#     result = '('
#     if len(number) == 10:
#         # result = True
#         for idx,num in enumerate(number):
#             if idx>= 0 and idx<2:
#                 result += str(num)
#             elif idx == 2:
#                 result += '{}) '.format(num)
#             elif idx>2 and idx<5:
#                 result += str(num)
#             elif idx == 5:
#                 result += '{}-'.format(num)
#             else:
#                 result += str(num)
#     else:
#         result = False
#     print(result)

# create_phone_number([1,2,3,4,5,6,7,8,9,0])
# create_phone_number([0,2,1,3,6,5,8,9,4,7])
# create_phone_number([1,2,3,4,5,6,7,9,0])
# create_phone_number([0,2,3,4,5,6,7,8,9,1,3])

# print('#-#-# No. 3 #-#-#')
# def sort_odd_even(num):
#     # print(num)
#     result = []
#     odd_dict = {}
#     odd_list = []
#     idx_odd = []
#     even_dict = {}
#     even_list = []
#     idx_even = []

#     for idx,item in enumerate(num):
#         if item%2 != 0:
#             odd_list.append(item)
#             idx_odd.append(idx)
#         else:
#             even_list.append(item)
#             idx_even.append(idx)

#     odd_list = sortAscending(odd_list)
#     even_list = sortDescending(even_list)

#     for i,idx in enumerate(idx_odd):
#         for j,num in enumerate(odd_list) :
#             if i == j:
#                 odd_dict[num] = idx
#     for i,idx in enumerate(idx_even):
#         for j,num in enumerate(even_list) :
#             if i == j:
#                 even_dict[num] = idx

#     odd_dict.update(even_dict)

#     for i in range(len(odd_list)+len(even_list)):
#         for num,idx in zip(odd_dict.keys(), odd_dict.values()):
#             if i == idx:
#                 result.append(num)
#     print(result)

# def sortAscending(num1):
#     for i in range(len(num1)):
#         for j in range(i+1, len(num1)):
#             if num1[i] > num1[j]:
#                 num1[i], num1[j] = num1[j], num1[i]
#     return num1

# def sortDescending(num2):
#     for i in range(len(num2)):
#         for j in range(i+1, len(num2)):
#             if num2[i] < num2[j]:
#                 num2[i], num2[j] = num2[j], num2[i]
#     return num2

# sort_odd_even([5,3,2,8,1,4])

print('#-#-# No. 4 #-#-#')
def hollowTriangle(n):
    z=''
    if n > 1:
        for i in range(n):
            if i>=0 and i<n-1:
                for j in range(n-i-1):
                    z += '_'
            if i == 0:
                z += '#'
            elif i > 0 and i < n-1: 
                z += '#'
                for k in range(2*(i-1)+1):
                    z += '_' 
                z += '#'
            elif i < n:
                for j in range(n-i-1):
                    z += ' '
                for l in range(2*(n-1)+1):
                    z += '#'
            if i>=0 and i<n-1:
                for j in range(n-i-1):
                    z += '_'
            z += '\n'
    else:
        z += '#'
    print(z)

hollowTriangle(1)
hollowTriangle(2)
hollowTriangle(3)
hollowTriangle(4)
hollowTriangle(5)
hollowTriangle(6)
