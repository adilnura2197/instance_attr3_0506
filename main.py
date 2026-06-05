class Oydin:
    def __init__(self, qiymat):
        self.qiymat = qiymat

a = Oydin(10)
b = Oydin(10)
a.qiymat = 99
print(a.qiymat, b.qiymat)
