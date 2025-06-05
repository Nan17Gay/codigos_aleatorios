import random

# Lista de Pokémons disponíveis com golpes
pokemons_disponiveis = [
    {
        "nome": "Pikachu",
        "vida": 100,
        "golpes": [
            {"nome": "Choque do Trovão", "dano": 20, "precisao": 80},
            {"nome": "Investida", "dano": 10, "precisao": 100}
        ]
    },
    {
        "nome": "Charmander",
        "vida": 90,
        "golpes": [
            {"nome": "Lança-Chamas", "dano": 25, "precisao": 70},
            {"nome": "Arranhão", "dano": 12, "precisao": 95}
        ]
    },
    {
        "nome": "Bulbasaur",
        "vida": 110,
        "golpes": [
            {"nome": "Folha Navalha", "dano": 20, "precisao": 80},
            {"nome": "Investida", "dano": 10, "precisao": 100}
        ]
    },
    {
        "nome": "Squirtle",
        "vida": 105,
        "golpes": [
            {"nome": "Jato d'Água", "dano": 18, "precisao": 85},
            {"nome": "Cabeçada", "dano": 15, "precisao": 90}
        ]
    },
    {
        "nome": "Pidgey",
        "vida": 85,
        "golpes": [
            {"nome": "Ataque de Areia", "dano": 10, "precisao": 95},
            {"nome": "Investida", "dano": 12, "precisao": 100}
        ]
    },
    {
        "nome": "Eevee",
        "vida": 95,
        "golpes": [
            {"nome": "Ataque Rápido", "dano": 15, "precisao": 100},
            {"nome": "Mordida", "dano": 18, "precisao": 85}
        ]
    }
]

# Lista de Pokémons capturados pelo jogador
pokemons_capturados = []

# Loop principal do jogo
while True:
    # Sorteia um novo Pokémon selvagem
    pokemon_selvagem = random.choice(pokemons_disponiveis)
    pokemon_selvagem = {
        "nome": pokemon_selvagem["nome"],
        "vida": pokemon_selvagem["vida"],
        "golpes": pokemon_selvagem["golpes"]
    }

    print(f"\n🌿 Um {pokemon_selvagem['nome']} selvagem apareceu!")

    # Menu de ações
    print("\nO que você quer fazer?")
    print("1 - Capturar")
    print("2 - Fugir")
    print("3 - Lutar")
    print("4 - Sair do jogo")

    escolha = input("Escolha uma opção (1/2/3/4): ")

    # ---------------- SAIR DO JOGO ---------------- #
    if escolha == "4":
        print("👋 Até a próxima, treinador!")
        break

    # ---------------- CAPTURAR ---------------- #
    elif escolha == "1":
        chance = random.randint(1, 100)
        if chance <= 50:
            print(f"🎉 Você capturou o {pokemon_selvagem['nome']}!")
            novo_pokemon = {
                "nome": pokemon_selvagem["nome"],
                "vida": pokemon_selvagem["vida"],
                "golpes": pokemon_selvagem["golpes"]
            }
            pokemons_capturados.append(novo_pokemon)
        else:
            print(f"😢 O {pokemon_selvagem['nome']} escapou da Pokébola!")

    # ---------------- FUGIR ---------------- #
    elif escolha == "2":
        chance = random.randint(1, 100)
        if chance <= 70:
            print("🏃‍♂️ Você fugiu com sucesso!")
        else:
            print("😬 Você não conseguiu fugir!")

    # ---------------- LUTAR ---------------- #
    elif escolha == "3":
        if len(pokemons_capturados) == 0:
            print("🚫 Você não tem nenhum Pokémon para lutar!")
            print(f"O {pokemon_selvagem['nome']} te atacou e você perdeu! 💥")
        else:
            # Usar o primeiro Pokémon capturado
            meu_pokemon = pokemons_capturados[0]
            print(f"\n⚔️ Você escolheu {meu_pokemon['nome']} para lutar!")

            # Resetar vida se já foi usado antes
            meu_pokemon["vida"] = next(p["vida"] for p in pokemons_disponiveis if p["nome"] == meu_pokemon["nome"])

            while meu_pokemon["vida"] > 0 and pokemon_selvagem["vida"] > 0:
                print("\nSeus golpes:")
                for i, golpe in enumerate(meu_pokemon["golpes"]):
                    print(f"{i + 1} - {golpe['nome']} (Dano: {golpe['dano']}, Precisão: {golpe['precisao']}%)")

                escolha_golpe = input("Escolha o número do golpe: ")
                if not escolha_golpe.isdigit() or int(escolha_golpe) not in range(1, len(meu_pokemon["golpes"]) + 1):
                    print("❌ Escolha inválida!")
                    continue

                golpe_usado = meu_pokemon["golpes"][int(escolha_golpe) - 1]
                chance = random.randint(1, 100)
                if chance <= golpe_usado["precisao"]:
                    pokemon_selvagem["vida"] -= golpe_usado["dano"]
                    print(f"{meu_pokemon['nome']} usou {golpe_usado['nome']} e causou {golpe_usado['dano']} de dano!")
                else:
                    print(f"{meu_pokemon['nome']} tentou usar {golpe_usado['nome']}, mas errou!")

                if pokemon_selvagem["vida"] <= 0:
                    print(f"🎉 Você derrotou o {pokemon_selvagem['nome']}!")
                    break

                golpe_inimigo = random.choice(pokemon_selvagem["golpes"])
                chance_inimigo = random.randint(1, 100)
                if chance_inimigo <= golpe_inimigo["precisao"]:
                    meu_pokemon["vida"] -= golpe_inimigo["dano"]
                    print(f"{pokemon_selvagem['nome']} usou {golpe_inimigo['nome']} e causou {golpe_inimigo['dano']} de dano!")
                else:
                    print(f"{pokemon_selvagem['nome']} tentou usar {golpe_inimigo['nome']}, mas errou!")

                print(f"❤️ Vida do seu {meu_pokemon['nome']}: {max(0, meu_pokemon['vida'])}")
                print(f"💢 Vida do {pokemon_selvagem['nome']}: {max(0, pokemon_selvagem['vida'])}")

            if meu_pokemon["vida"] <= 0:
                print(f"💀 Seu {meu_pokemon['nome']} foi derrotado!")

    # ---------------- OPÇÃO INVÁLIDA ---------------- #
    else:
        print("❌ Opção inválida!")

