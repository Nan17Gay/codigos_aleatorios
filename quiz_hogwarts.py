def quiz():
    print("🧙‍♂️ Bem-vindo ao Quiz: Você seria aceito em Hogwarts?")
    print("Responda sinceramente e descubra seu destino...\n")

    pontos = 0

    perguntas = [
        {
            "pergunta": "Você prefere estudar qual matéria?",
            "opcoes": {
                "a": ("Poções", 1),
                "b": ("Defesa Contra as Artes das Trevas", 2),
                "c": ("Trato das Criaturas Mágicas", 1),
                "d": ("História da Magia", 0)
            }
        },
        {
            "pergunta": "Qual animal mágico você escolheria como mascote?",
            "opcoes": {
                "a": ("Coruja", 2),
                "b": ("Gato", 1),
                "c": ("Sapo", 0),
                "d": ("Dragão (caso pudesse)", 3)
            }
        },
        {
            "pergunta": "Qual dessas qualidades você mais valoriza?",
            "opcoes": {
                "a": ("Coragem", 2),
                "b": ("Inteligência", 1),
                "c": ("Lealdade", 1),
                "d": ("Ambição", 2)
            }
        },
        {
            "pergunta": "Se você pudesse aprender um feitiço agora, qual seria?",
            "opcoes": {
                "a": ("Expelliarmus: desarmar inimigos", 2),
                "b": ("Alohomora: abrir portas trancadas", 1),
                "c": ("Wingardium Leviosa: levitar objetos", 1),
                "d": ("Avada Kedavra: derrotar qualquer ameaça", 3)
            }
        },
        {
            "pergunta": "Qual dessas criaturas mágicas você gostaria de encontrar?",
            "opcoes": {
                "a": ("Hipogrifo", 2),
                "b": ("Trasgo", 0),
                "c": ("Fênix", 2),
                "d": ("Dementador", 1)
            }
        }
    ]

    for p in perguntas:
        print("\n" + p["pergunta"])
        for letra, (texto, _) in p["opcoes"].items():
            print(f"  {letra}) {texto}")

        resposta = input("Escolha uma opção: ").lower()

        if resposta in p["opcoes"]:
            pontos += p["opcoes"][resposta][1]
        else:
            print("Opção inválida. Nenhum ponto ganho.")

    print("\n✨ Resultado ✨")
    if pontos >= 9:
        print("🪄 Você com certeza seria aceito em Hogwarts! Sua carta está a caminho!")
    elif pontos >= 5:
        print("🤔 Você talvez precise provar seu valor mágico... mas tem potencial!")
    else:
        print("🙁 Infelizmente, o mundo trouxa parece ser seu destino. Tente de novo!")

# Executa o quiz se o script for rodado diretamente
if __name__ == "__main__":
    quiz()

