import random

# Opções secretas com pontuação de sobrevivência associada
armas = {
    "B": ("Espingarda", 80),
    "C": ("Panela de pressão", 40),
    "D": ("Colher afiada", 20),
    "F": ("Taco de beisebol", 60),
    "G": ("Arco e flecha", 70)
}

abrigos = {
    "1": ("Shopping tomado", 30),
    "2": ("Casa na árvore", 60),
    "3": ("Ilha deserta", 50),
    "4": ("Escola vazia", 40),
    "5": ("Supermercado abandonado", 70)
}

companheiros = {
    "A": ("um zumbi amigo", 10),
    "E": ("um cientista maluco", 60),
    "I": ("sua avó armada", 50),
    "O": ("um bebê gênio", 40),
    "U": ("um cachorro treinado", 70)
}

# Escolhas misteriosas
print("Escolha seu destino aleatoriamente")
print("Escolha sua arma: B, C, D, F ou G")
arma_escolha = input("Escolha: ").strip().upper()

print("\nEscolha seu abrigo: 1, 2, 3, 4 ou 5")
abrigo_escolha = input("Escolha: ").strip()

print("\nEscolha seu companheiro: A, E, I, O ou U")
companheiro_escolha = input("Escolha: ").strip().upper()

# Revelações e pontuação
arma, arma_pts = armas.get(arma_escolha, ("nada", 0))
abrigo, abrigo_pts = abrigos.get(abrigo_escolha, ("um lugar perigoso", 0))
companheiro, companheiro_pts = companheiros.get(companheiro_escolha, ("ninguém", 0))

# Evento aleatório
eventos = [
    "Um zumbi gigante apareceu!",
    "Você encontrou um mapa secreto.",
    "Alguém do grupo te traiu.",
    "Descobriram uma cura!",
    "Você ganhou superpoderes por acidente."
]
evento = random.choice(eventos)

# Soma da pontuação
pontos_totais = arma_pts + abrigo_pts + companheiro_pts

# Converter em porcentagem (máximo possível é 80+70+70 = 220)
porcentagem = int((pontos_totais / 220) * 100)

# Resultado final
print("\n🧟 RESULTADO FINAL:")
print(f"🔫 Sua arma: {arma}")
print(f"🏠 Seu abrigo: {abrigo}")
print(f"👥 Seu companheiro: {companheiro}")
print(f"⚠️ Evento inesperado: {evento}")
print(f"\n📊 Sua chance de sobrevivência: {porcentagem}%")
