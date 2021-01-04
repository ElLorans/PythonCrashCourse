def get_div(integer):
    """
    Return list of divisors of integer.
    :param integer: int
    :return: list
    """
    divisors = [num for num in range(2, int(integer**0.5)+1) if integer % num == 0]
    rem_divisors = [int(integer/num) for num in divisors]
    divisors += rem_divisors
    divisors.append(integer)
    res = list(set(divisors))       # remove duplicates
    res.sort()
    return res

print("WATCH OUT!!!")

#if __name__ == "__main__":
    #print(get_div(100))
