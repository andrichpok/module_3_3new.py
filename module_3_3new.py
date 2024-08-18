#1.Функция с параметрами по умолчанию:
def print_params(a = 10, b = 'string', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров:

values_list = [8, True, 'Hello']
values_dict = {'a' : 28, 'b' : 'phone', 'c' : False}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = [50, 'string']
print_params(*values_list_2, 42)