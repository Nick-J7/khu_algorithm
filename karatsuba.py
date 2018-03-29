""" Big Integer operation """


"""
def normalize(array):
    result = [0] * (len(array) + 1)
    for i, value in enumerate(array):
        while value >= 10:
            result[i + 1] += 1
            value -= 10
        result[i] += value
    return result


def add(a, b):
    result = [0] * (len())
    for i, value in enumerate():
        
    result = a + b
    return result


def multiply(a, b):
    result = a * b
    return result


def karatsuba(a, b):

    max_len = max(len(a), len(b))

    # Base case : threshold
    if max_len <= 50:
        return multiply(a, b)

    m = (max_len + 1) / 2

    # a = x * 10^m + y, b = w * 10^m + z
    # r_0 = (x + y)
    # r_1 = (w + z)
    # r = (x + y) * (w + z)
    # a * b = xw * 10^2m + (r - xw - yz) * 10^m + yz
    x = a[:m]
    y = a[m:]
    w = b[:m]
    z = b[m:]
    xw = karatsuba(x, w)
    yz = karatsuba(y, z)
"""

def prod2(a, b):
    threshold = 20
    n0 = len(str(a))
    n1 = len(str(b))
    n = max(n0, n1)

    if a == 0 or b == 0:
        return 0
    elif n < threshold:
        return a * b
    else:
        m = int(n / 2)
        x = int(a / (10 ** m))
        y = a % (10 ** m)
        w = int(b / (10 ** m))
        z = b % (10 ** m)
        #print(x, y, w, z)
        r = prod2(x + y, w + z)
        p = prod2(x, w)
        q = prod2(y, z)
        return p * 10 ** (2*m) + (r - p - q) * 10 ** m + q

    return 0


if __name__ == '__main__':
    import time

    a = 1234567812345678123456789123456712345678123456781234567891234567
    b = 2345678923456789234567892345678912345678123456781234567891234567
    start_time = time.time()
    print(prod2(a, b))
    print("Elapsed Time: ", time.time() - start_time)
    start_time = time.time()
    print(a * b)
    print("Elapsed Time: ", time.time() - start_time)
