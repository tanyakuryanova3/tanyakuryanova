# -- coding: utf-8 --
def lnght(a, b, l, N):
    return ((2 * l + (2 * N - 1) * a) + (2 * (N - 1) * b))
print("Длина шнурка:", lnght(4, 2, 7, 5))