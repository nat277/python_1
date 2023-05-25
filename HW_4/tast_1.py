# Задача 36: 

def print_operation_table(operation, num_rows=6, num_columns=6):
    x = [a + 1 for a in range(num_rows)]
    y = [b + 1 for b in range(num_columns)]

    for a_x in x:
       
     print(*(list(map(operation, [a_x] * num_columns, y))), sep='\t')

print_operation_table(lambda x, y: x * y) 