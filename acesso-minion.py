minions_autorizados = ["kevin", "stuart", "bob", "dave", "phil", "yuri", "priscila", "marcos", "rafa", "vitor", "nana"]

usuario = input("🔐 Digite seu nome para acessar o sistema minion: ").strip().lower()


if usuario in minions_autorizados:
   
    print("\n🎉 BEE-DO BEE-DO! 🎉")
    print("Minion identificado com sucesso!")
    print("Perfil amarelo, risada engraçada, amor por bananas... tudo confirmado!")
    print("✅ Acesso permitido")
    print(f"Bem-vindo, minion {usuario.capitalize()}! Prepare-se para a próxima missão com o Gru!")
else:
    # Acesso negado
    print("\n🚨 ALERTA! 🚨")
    print("Este sistema é exclusivo para MINIONS autênticos!")
    print("❌ Acesso negado")
    print("Motivo: Você não é um minion. Sem banana, sem entrada.")
