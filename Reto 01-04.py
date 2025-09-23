def Sum_Par():
    list_num = list(map(int, input("Ingrese números: ").split()))
    result = 0
    if len(list_num) < 2:
        return False
    for i in range(len(list_num) - 1):
        current_sum = list_num[i] + list_num[i + 1]
        if current_sum > result:
            result = current_sum
    return result

print(Sum_Par())
