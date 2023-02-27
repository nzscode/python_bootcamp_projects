def parity_analysis(num):
    new_num = num
    num = str(num)
    total = 0
    for n in num:
        total += int(n)
        print(total)

    total_is = ""
    num_is = ""
    if total % 2 == 0:
        total_is = "even"
    else:
        total_is = "odd"

    if new_num % 2 == 0:
        num_is = "even"
    else:
        num_is = "odd"

    if total_is == num_is:
        print("True")
    else:
        print("False")

    # if new_num % 2 == 0 & total % 2 == 0:
    #     print("Parity")
    # elif new_num % 2 != 0 & total % 2 != 0:
    #     print("Parity")
    # elif new_num % 2 == 0 & total % 2 != 0:
    #     print("Nope")
    # elif new_num % 2 != 0 & total % 2 == 0:
    #     print("Nope")

parity_analysis(243)