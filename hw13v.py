"""Напишите функцию, которая переводит значения показаний
температуры из Цельсия в Фаренгейт и наоборот."""
def C_to_F(Tc):
    return (round(9/5*Tc+32, 2))
def F_to_C(Tf):
    return (round(5/9*(Tf-32),2))

print(C_to_F(1))
print(F_to_C(1))