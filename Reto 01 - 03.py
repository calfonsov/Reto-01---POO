def Prime_Num():
    num_list = list(map(int, input("Ingrese números separados por espacios: ").split()))
    prime_list = []
    for num in num_list:
        prime = False
        if num > 1:
            prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime == True:
            prime_list.append(num)
    print(" ".join(map(str, prime_list)))

print(Prime_Num())
