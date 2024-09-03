def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_fibonacci_number(number):
   
    if number < 0:
        return False
    sequence = fibonacci_sequence(number + 1)
    return number in sequence

def check_fibonacci_numbers(numbers):
    
    results = []
    for number in numbers:
        if is_fibonacci_number(number):
            results.append(f"O número {number} pertence à sequência de Fibonacci.")
        else:
            results.append(f"O número {number} **não** pertence à sequência de Fibonacci.")
    return results


input_values = input("Informe um número ou uma sequência de números separados por espaço: ")

numbers = list(map(int, input_values.split()))


results = check_fibonacci_numbers(numbers)
for result in results:
    print(result)
