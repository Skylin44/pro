def calculate_structure_sum(var):
    global summa
    if isinstance(var, int):
        summa += var
    elif isinstance(var, str):
        summa += len(var)
    elif isinstance(var, (list, tuple, set)):
        for i in var:
            calculate_structure_sum(i)
    elif isinstance(var, dict):
        for key, value in var.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = 0
calculate_structure_sum(data_structure)
print(summa)
