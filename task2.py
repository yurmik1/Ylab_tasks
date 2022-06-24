def int32_to_ip(int32):
    ip = []
    for i in range(3, -1, -1):
        n_ip = int32 // 256**i
        ip.append(n_ip)
        int32 %= 256**i
    return f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}'


