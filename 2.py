def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_fibonacci_number(number):
    sequence = fibonacci_sequence(number)
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} **não** pertence à sequência de Fibonacci."


num = int(input("Informe um número: "))
resultado = is_fibonacci_number(num)
print(resultado)
