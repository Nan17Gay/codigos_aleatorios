def escolher_tracos():
    tracos = {
        "1": "Corajoso",
        "2": "Inteligente",
        "3": "Leal",
        "4": "Ambicioso",
        "5": "Impulsivo",
        "6": "Criativo",
        "7": "Justo",
        "8": "Calmo",
        "9": "Orgulhoso",
        "0": "Animado"
    }

    print("\nEscolha 2 traços de personalidade do campista:")
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


def determinar_chale(tracos):
    if "Corajoso" in tracos and "Impulsivo" in tracos:
        return "Chalé 5 - Ares"
    elif "Inteligente" in tracos and "Criativo" in tracos:
        return "Chalé 6 - Atena"
    elif "Orgulhoso" in tracos and "Justo" in tracos:
        return "Chalé 10 - Afrodite"
    elif "Ambicioso" in tracos and "Orgulhoso" in tracos:
        return "Chalé 1 - Zeus"
    elif "Animado" in tracos and "Justo" in tracos:
        return "Chalé 11 - Hermes"
    elif "Animado" in tracos and "Criativo" in tracos:
        return "Chalé 7 - Apolo"
    elif "Impulsivo" in tracos and "Animado" in tracos:
        return "Chalé 12 - Dionisio"
    elif "Justo" in tracos and "Calmo" in tracos:
        return "Chalé 4 - Demeter"
    elif "Inteligente" in tracos and "Orgulhoso" in tracos:
        return "Chalé 10 - Hefesto"
    elif "Impulsivo" in tracos and "Orgulhoso" in tracos:
        return "Chalé 3 - Poseidon"
    else:
        return "Chalé 11 - Hermes (Campista Indefinido)"


def main():
    print("🌊 Bem-vindo ao teste do Acampamento Meio-Sangue 🌊")
    nome = input("Nome do campista: ")
    idade = input("Idade do campista: ")

    tracos_escolhidos = escolher_tracos()
    chale = determinar_chale(tracos_escolhidos)

    print("\n🏕️ Resultado:")
    print(f"Campista: {nome}, {idade} anos")
    print("Traços escolhidos:", ", ".join(tracos_escolhidos))
    print(f"Você foi designado para o {chale}!")


if __name__ == "__main__":
    main()