import random
import time

# Classe Genérica: Personagem

class Personagem:
    def __init__(self, nome, vida, ataque_base, defesa_base):
        self.nome = nome
        self.vida = vida
        self.ataque_base = ataque_base
        self.defesa_base = defesa_base

    def atacar(self, outro):
        raise NotImplementedError

    def defender(self, dano):
        raise NotImplementedError

    def esta_vivo(self):
        return self.vida > 0

# Subclasses de Heróis

class Guerreiro(Personagem):
    def atacar(self, outro):
        dano = self.ataque_base + random.randint(8, 14)
        print(f"{self.nome} - A lâmina cumpre seu destino! e dá {dano} de dano!")
        outro.defender(dano)

    def defender(self, dano):
        reducao = self.defesa_base + random.randint(0, 10)
        dano_final = max(0, dano - reducao)
        self.vida -= dano_final
        print(f"{self.nome} - Defende com seu escudo {reducao} e perde {dano_final} de vida (vida atual: {self.vida}).")

class Mago(Personagem):
    def atacar(self, outro):
        dano = self.ataque_base + random.randint(8, 15)
        print(f"{self.nome} - O feitiço toma forma! e dá {dano} de dano!")
        outro.defender(dano)

    def defender(self, dano):
        reducao = random.randint(0, self.defesa_base)
        dano_final = max(0, dano - reducao)
        self.vida -= dano_final
        print(f"{self.nome} - Barreira, erga-se! {dano_final} de vida (vida atual: {self.vida}).")

# Subclasses de Inimigos

class Goblin(Personagem):
    def atacar(self, outro):
        dano = self.ataque_base + random.randint(2, 8)
        print(f"{self.nome} - Corta, corta! e dá {dano} de dano!")
        outro.defender(dano)

    def defender(self, dano):
        reducao = random.randint(0, self.defesa_base)
        dano_final = max(0, dano - reducao)
        self.vida -= dano_final
        print(f"{self.nome} - Haha, errou! {dano_final} de vida (vida atual: {self.vida}).")

class Dragao(Personagem):
    def atacar(self, outro):
        dano = self.ataque_base + random.randint(8, 15)
        print(f"{self.nome} - Chama mortal! e dá {dano} de dano!")
        outro.defender(dano)

    def defender(self, dano):
        reducao = self.defesa_base + random.randint(5, 10)
        dano_final = max(0, dano - reducao)
        self.vida -= dano_final
        print(f"{self.nome} - Escamas impenetráveis! {dano_final} de vida (vida atual: {self.vida}).")

# Função de Batalha

def batalha(herois, inimigos):
    print("\n=== SIMULADOR DE BATALHA ===\n")
    round_num = 1

    while any(h.esta_vivo() for h in herois) and any(i.esta_vivo() for i in inimigos):
        print(f"\n⚔️ ROUND {round_num} ⚔️")
        time.sleep(0.5)

        heroi = random.choice([h for h in herois if h.esta_vivo()])
        inimigo = random.choice([i for i in inimigos if i.esta_vivo()])

        atacante, defensor = random.choice([(heroi, inimigo), (inimigo, heroi)])
        print(f"\n{atacante.nome} ataca {defensor.nome}!")
        atacante.atacar(defensor)

        round_num += 1
        time.sleep(0.5)

    print("\n=== FIM DA BATALHA ===")
    if any(h.esta_vivo() for h in herois):
        print("🏆 Os heróis venceram!")
    else:
        print("💀 Os inimigos dominaram!")

# Execução principal

if __name__ == "__main__":
    herois = [
        Guerreiro("Guerreiro", 100, 15, 10),
        Mago("Mago", 120, 18, 5)
    ]

    inimigos = [
        Goblin("Goblin", 80, 10, 5),
        Dragao("Dragao", 150, 20, 10)
    ]

    batalha(herois, inimigos)
