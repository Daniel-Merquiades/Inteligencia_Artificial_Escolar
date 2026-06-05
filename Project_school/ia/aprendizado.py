import json
import os
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

class Aprendizado:
    def __init__(self):
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.caminho_exemplos= os.path.join(pasta_atual, "novos_exemplos.json")
        self.caminho_modelo = os.path.join(pasta_atual, "modelo.pkl")
        self.exemplos = self.carregar_exemplos()
    def carregar_exemplos(self):
        if os.path.exists(self.caminho_exemplos):
            with open(self.caminho_exemplos, "r", encoding = "utf-8") as f:
                return json.load(f)
        return[]
    def salvar_exemplo(self,frase, intencao):
        self.exemplos.append({"frase": frase, "intencao": intencao})
        with open(self.caminho_exemplos, "w", encoding="utf-8") as f:
            json.dump(self.exemplos, f, ensure_ascii=False, indent=2)
            print(f"[IA] Aprendi:'{frase}' -> '{intencao}'")
    def retreinar(self):
        from ia.treinamento import Dados as dados_base
        todos_exemplos = dados_base.copy()
        for ex in self.exemplos:
            todos_exemplos.append((ex["frase"], ex["intencao"]))
        frases = [item[0] for item in todos_exemplos]
        intencoes = [item[1] for item in todos_exemplos]
        modelo = Pipeline ([
            ("tfidf", TfidfVectorizer()),
            ("classificador", LogisticRegression())
        ])
        modelo.fit(frases, intencoes)
        with open(self.caminho_modelo, "wb") as f:
            pickle.dump(modelo,f)
        print(f"[IA] Modelo retreinado com {len(todos_exemplos)} exemplos!")
        return modelo