def main(input: str) -> str:
    # Проверяем, что ввод не пустой
    if not input:
        raise Exception('throws Exception')


    # проверяем является ли математическим выражением!
    input_parts = input.split()
    if len(input_parts) < 3:
        raise Exception('throws Exception //т.к. строка не является математической операцией!')


    # Разделяем строку на числа и оператор
    input_parts = input.split()
    if len(input_parts) != 3:
        raise Exception('throws Exception //формат математической операции не удовлетворяет заданию - два числа и один оператор (+, -, /, *)')


    # Получаем числа и оператор
    try:
        operand1 = int(input_parts[0])
        operator = input_parts[1]
        operand2 = int(input_parts[2])
    except ValueError:
        raise Exception('throws Exception')


    # Числа должны быть от 1 до 10
    if operand1 < 1 or operand1 > 10 or operand2 < 1 or operand2 > 10:
        raise Exception('throws Exception //Числа должны быть от 1 до 10!')


    # Выполняем операцию и возвращаем результат
    if operator == "+":
        return str(operand1 + operand2)
    elif operator == "-":
        return str(operand1 - operand2)
    elif operator == "*":
        return str(operand1 * operand2)
    elif operator == "/":
        return str(operand1 // operand2)
    else:
        raise Exception('throws Exception')

while True:
# Пример использования
    try:
        input_str = input("Введите выражение: ")
        result = main(input_str)
        print(result)
    except Exception as e:
        print(e)
        break