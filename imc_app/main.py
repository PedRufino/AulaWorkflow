from core.imc import calcular, classificar

def main():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc_value = calcular(peso, altura)
    classificacao = classificar(imc_value)
    print(f"Seu IMC é: {imc_value:.2f} - {classificacao}")


if __name__ == "__main__":
    main()
