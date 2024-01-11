def primer(num=50):
    prime_list, non_prime_list = [], []
    for a in range(2, num+1):
        c = 0
        for b in range(1, a+1):
            if c >= 3:
                non_prime_list.append(a)
                break
            if a % b == 0:
                c += 1
    prime_list = [num for num in range(1, num+1) if num not in non_prime_list]
    print(prime_list)
    return prime_list

primer(10000)


