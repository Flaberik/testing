

def Buddy(start: int, limit: int):
    for i in range(start, limit):
        sum_n = get_sum_div(i)
        sum_m = None
        sum_z = None
        if sum_n > 1:
            sum_m = get_sum_div(sum_n-1)
            sum_z = get_sum_div(sum_m-1)
            if sum_n == sum_z:
                return [sum_m, sum_n]

    return None


def get_sum_div(number: int):
    sum_div = 0
    for div in range(1, int(number/2) + 1):
        if number % div == 0:
            sum_div += div
    return sum_div


if __name__ == "__main__":

    while True:
        start = input('start: ')
        limit = input('limit: ')

        try:
            start = int(start)
            limit = int(limit)

            if start > 0 and limit > start:
                print(Buddy(start, limit))

        except Exception as ex:
            print(ex)
