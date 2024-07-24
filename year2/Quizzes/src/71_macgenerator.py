# import random
#
# class Mac_address():
#     def ipv6machine(self, N:int):
#         chars = "0123456789ABCDEF"
#         address_list, mac, i = [],"", 0
#         while i<N:
#             for j in range(12):
#                 mac+=chars[random.randint(0,15)]
#                 if j%2==1:
#                     mac+=":"
#                 if mac in address_list == False:
#                     address_list.append(mac)
#                     i+=1
#                 mac=""
#         return address_list
#     #dxfgchjvg
#
# test = Mac_address()
# print(test.ipv6machine(1))

import random

class ipv6():
    def ipv6machine(N:int):
        i,chars,temp=0,'0123456789ABCDEF',""
        while i<N:
            for j in range(4):
                temp += f"{chars[random.randint(0,15)]}{chars[random.randint(0,15)]}{chars[random.randint(0,15)]}{chars[random.randint(0,15)]}"
        return temp
print(ipv6.ipv6machine(1))