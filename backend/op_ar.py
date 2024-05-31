def soma(num1, num2, base_final):
    num1_decimal = int(num1, base_final)
    num2_decimal = int(num2, base_final)
    resultado_decimal = num1_decimal + num2_decimal
    return converter_decimal_para_base(resultado_decimal, base_final)

def subtracao(num1, num2, base_final):
    num1_decimal = int(num1, base_final)
    num2_decimal = int(num2, base_final)
    resultado_decimal = num1_decimal - num2_decimal
    return converter_decimal_para_base(resultado_decimal, base_final)

def converter_decimal_para_base(numero, base):
    if base == 10:
        return str(numero)

    resultado = ""
    while numero > 0:
        resto = numero % base
        if resto < 10:
            resultado = chr(resto + ord('0')) + resultado
        else:
            resultado = chr(resto - 10 + ord('A')) + resultado
        numero //= base

    return resultado or "0"
