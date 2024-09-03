
string = input("Escreva o que quer inverter: \n")


def inverter_string(s):

    string_invertida = ""
    

    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida


string_invertida = inverter_string(string)
print("String original: ", string)
print("String invertida: ", string_invertida)
