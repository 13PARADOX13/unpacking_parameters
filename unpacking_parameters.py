def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(3, 'УПС')
print_params(5, 'неверно', False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [[13, 'try', True], 999, 'hello']
values_dict = {'a' : 100, 'b' : 'STRONG', 'c' : False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [{1, 2}, ('male', 'famale')]
print_params(*values_list_2, 42)
