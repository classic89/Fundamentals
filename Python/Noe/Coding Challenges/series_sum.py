from fractions import Fraction
a = float('1') / float('4')
b = '1/4'.split('/')


def series_sum(n):
    if n == 0:
        return "0.00"
    else:
        series = [Fraction(float(1) / float((3 * x) - 2)) for x in range(1, n+1)]
        total = round(0, 2)
        for item in series:
            total += float(item)
        return "{0:.2f}".format(total)


fractions = [Fraction(float(1) / float((3 * x) - 2)) for x in range(1, 10)]

series_sum(98)
# print(fractions)
# print("{0:.2f}".format(float(fractions[2])))
