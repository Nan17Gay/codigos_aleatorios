def escolher_tracos():
    tracos = {
        "1": "Corajoso",
        "2": "Inteligente",
        "3": "Leal",
        "4": "Ambicioso",
        "5": "Impulsivo",
        "6": "Criativo",
        "7": "Justo",
        "8": "Orgulhoso"
    }

    print("\nEscolha 2 traços de personalidade do estudante:")
    for chave, valor in tracos.items():
        print(f"{chave}. {valor}")

    escolhas = []
    while len(escolhas) < 2:
        escolha = input(f"Traço {len(escolhas)+1}: ")
        if escolha in tracos and escolha not in escolhas:
            escolhas.append(escolha)
        else:
            print("Escolha inválida ou repetida. Tente novamente.")

    return [tracos[e] for e in escolhas]

def determinar_casa(tracos):
    if "Inteligente" in tracos and "Criativo" in tracos:
        return "Corvinal - casa dos inteligentes e criativos"
    elif "Ambicioso" in tracos and "Orgulhoso" in tracos:
        return "Sonserina - casa dos ambiciosos e astutos"
    elif "Leal" in tracos and "Impulsivo" in tracos:
        return "Grifinória - casa dos bravos e corajosos"
    else:
        return "Lufa-Lufa - casa dos leais e trabalhadores"

def main():
    print("Bem-vindo à Escola de Magia e Bruxaria de Hogwarts!")
    nome = input("Nome do estudante: ")
    sobrenome = input("Sobrenome do estudante: ")
    idade = input("Idade do estudante: ")

    tracos_escolhidos = escolher_tracos()
    casa = determinar_casa(tracos_escolhidos)

    print("\n🏕️ Resultado:")
    print(f"Estudante: {nome} {sobrenome}, {idade} anos")
    print("Traços escolhidos:", ", ".join(tracos_escolhidos))
    print(f"Você foi designado para a {casa}!")

if __name__ == "__main__":
    main()
