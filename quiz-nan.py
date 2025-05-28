def quiz():
    perguntas = [
        {
            "pergunta": "Qual a cor favorita de Nan?",
            "opcoes": {
                "A": "Preto",
                "B": "Vermelho",
                "C": "Azul",
                "D": "Roxo"
            },
            "resposta_certa": "C"
        },
        {
            "pergunta": "Qual matéria favorita de Nan?",
            "opcoes": {
                "A": "Biologia",
                "B": "Artes",
                "C": "Português",
                "D": "Química"
            },
            "resposta_certa": "D"  
        },
        {
            "pergunta": "Qual hobbie preferido de Nan?",
            "opcoes": {
                "A": "Cozinhar",
                "B": "Desenhar",
                "C": "Escrever",
                "D": "Ouvir música"
            },
            "resposta_certa": "A"   
        },
        {
            "pergunta": "Qual nome completo de Nan?",
            "opcoes": {
                "A": "Ana Clara Mendez Oliveira",
                "B": "Ana Clara Mendes Gonçalves",
                "C": "Ana Clara Mendes Oliveira",
                "D": "Ana Clara Mendes Oliviera"
            },
            "resposta_certa": "C" 
        },
        {
            "pergunta": "Qual universo fictício favorito de Nan?",
            "opcoes": {
                "A": "Harry Potter",
                "B": "Percy Jackson",
                "C": "Maze Runner",
                "D": "Crepúsculo"
            },
            "resposta_certa": "A" 
        },
        {
            "pergunta": "Qual a maior fobia de Nan?",
            "opcoes": {
                "A": "Aranhas",
                "B": "Palhaços",
                "C": "Altura",
                "D": "Sangue"
            },
            "resposta_certa": "B" 
        }
    ]

    acertos = 0
    erros = 0
    respostas_dadas = []

    for p in perguntas:
        print("\n" + p["pergunta"])
        for letra, opcao in p["opcoes"].items():
            print(f"  {letra}) {opcao}")
        
        resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()
        while resposta not in p["opcoes"]:
            resposta = input("Opção inválida. Tente novamente (A, B, C ou D): ").strip().upper()

        respostas_dadas.append({
            "pergunta": p["pergunta"],
            "resposta_usuario": resposta,
            "resposta_certa": p["resposta_certa"]
        })

        if resposta == p["resposta_certa"]:
            acertos += 1
        else:
            erros += 1

    # Exibir resultados
    print("\n--- RESULTADO FINAL ---")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")
    print("\n--- Detalhes ---")
    for r in respostas_dadas:
        status = "✔️ Correto" if r["resposta_usuario"] == r["resposta_certa"] else "❌ Errado"
        print(f"{r['pergunta']}\n  Sua resposta: {r['resposta_usuario']} | Correta: {r['resposta_certa']} → {status}")

# Executar o quiz
quiz()

