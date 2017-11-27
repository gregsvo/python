
"""
The prime factors of 65,436 are 2, 3, 7, 19, and 41.

What is the largest prime factor of the number 802,871,435,163?

"""
def get_largest_factor(input_num):
    factor = 2
    while factor * factor <= input_num:
        if input_num % factor:
            factor += 1
        else:
            input_num //= factor
    print("LARGEST FACTOR FOUND: {}".format(input_num))
    return input_num


if __name__ == "__main__":
    input_num = 802871435163
    get_largest_factor(input_num)
