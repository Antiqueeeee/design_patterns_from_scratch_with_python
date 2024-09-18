# from A01_SimpleFactoryPattern.component import add_operation
from component import add_operation, invalid_operation

operation_factory = dict()
operation_factory["+"] = add_operation

input_num_1 = [1, 3, 5]
input_num_2 = [2, 4, 6]
input_operator = ["+", "+" , "-"]

for num_1, num_2, op in zip(input_num_1, input_num_2, input_operator):
    method = operation_factory.get(op, invalid_operation)(num_1, num_2).calculating
    print(f"Caulating {num_1} {op} {num_2} : result is {method()}")

