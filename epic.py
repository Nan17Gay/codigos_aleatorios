from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Abrir o navegador com ChromeDriverManager
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.get("https://store.epicgames.com/pt-BR/collection/top-sellers")

# Esperar até os jogos carregarem
WebDriverWait(navegador, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-rgqwpc"))
)

# Pegar títulos e preços
jogos = navegador.find_elements(By.CSS_SELECTOR, ".css-rgqwpc")
precos = navegador.find_elements(By.CSS_SELECTOR, "span.eds_1ypbntd0.eds_1ypbntdc.eds_1ypbntdk.css-12s1vua")

dados = []
for i in range(min(20, len(jogos), len(precos))):
    nome_jogo = jogos[i].text.strip()
    preco_jogo = precos[i].text.strip()
    print(f"Top {i+1} - {nome_jogo} - {preco_jogo}")
    
    dados.append({
        "ranking": f"Top {i+1}",
        "nome": nome_jogo,
        "preco": preco_jogo
    })

# Salvar em JSON
with open("jogos_epic.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("\n✔️ Arquivo 'jogos_epic.json' criado com sucesso!")

navegador.quit()