class Calculator:
    firstnum = None
    znak = None
    secondnum = None

    def set_data(self, firstcommand, firstnum,secondcommand, znak,thirdcommand, secondnum):
        self.firstnum = firstnum
        self.znak = znak
        self.secondnum = secondnum
calculator1 = Calculator()
calculator1.set_data(print("введите первое число:"),int(input()),print("введите знак (возможно:+ - / *):"),str(input()),print("введите второе число:"),int(input()))
def calcu(firstnum,znak,secondnum):
    if znak=="+": return firstnum+secondnum
    if znak == "-": return firstnum - secondnum
    if znak == "*": return firstnum * secondnum
    if znak == "/":
        if secondnum!=0: return firstnum / secondnum
        return "ERROR (делить на ноль нельзя)"
    return "ERROR (неверно введен знак)"
print(calcu(calculator1.firstnum,calculator1.znak,calculator1.secondnum))