import random

print('0123456789ABCDEF'[random.randint(0,15)])

group+=get_rand_hex() for i in range(4)

def get_sixtect_hex():
    group=""
    for i in range(4):
        group+=get_rand_hex()
    return group

def get_ip_v6_address():
    ip=":".join([get_sixtect_hex() for _ in range(8)])
    return ip

def ipv6machine(N):
    output = []
    for i in range(N):
        output.append(get_ip_v6_address())
    return output

print(ipv6machine(2))