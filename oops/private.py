class Account:
    def __init__(self, acc, passw):
        self.acc = acc
        self.__passw = passw    #private scope
s1 = Account("12345", "1vdds")
print(s1.acc)
print(s1.__passw)