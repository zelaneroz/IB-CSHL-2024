class ipv4():
    def ipv4machine():
        for i in range(256):
            for j in range(256):
                for k in range(256):
                    for l in range(256):
                        print(f'{i}.{j}.{k}.{l}')




#ONE LINE ANSWER
#print(ipv4machine())

# import itertools
#
# for address in itertools.product(range(256), repeat=4):
#     print(".".join(map(str, address)))
# for i in range(256**4):
#     print(".".join(map(str, [i >> 24, (i >> 16) & 255, (i >> 8) & 255, i & 255])))



print(ipv4.ipv4machine())