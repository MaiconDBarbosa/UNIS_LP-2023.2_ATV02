def calcular_area_triangulo(a, b, c):
    # Verifica se os lados formam um triângulo
    if a < b + c and b < a + c and c < a + b:
        # Calcula o semiperímetro
        s = (a + b + c) / 2
        # Calcula a área usando a fórmula de Herão
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    else:
        return None

def main():
    # Solicita os valores dos lados do triângulo
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    # Verifica se os valores formam um triângulo
    area_tri = calcular_area_triangulo(a, b, c)

    if area_tri is not None:
        print(f"Os valores formam um triângulo. A área é: {area_tri:.2f}")
    else:
        print(f"Os valores {a}, {b} e {c} não formam um triângulo.")

if __name__ == "__main__":
    main()
