# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():

    num = int(input('Please enter a number => '))
    sum = 0

    while num != 0:
        sum += num
        if sum >= 1000:
            break

        num = int(input('Please enter a number => '))

    print(sum +sum)
    return sum


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
