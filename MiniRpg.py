import random

print("Bem-vindo ao Mini RPG!")
nome = input("Digite o nome do seu personagem: ")

# Mapa simples com progresso
posicao = 0
mapa = ["Entrada", "Sala do Goblin", "Porta com Enigma", "Sala do Orc", "Tesouro"]

print("\nEscolha sua classe:")


print("1 - Guerreiro (Vida: 100, Ataque: 15, Armadura: 20%)")
print(
    r"""
      ,   A           {}
     / \, | ,        .--.
    |    =|= >      /.--.\
     \ /` | `       |====|
      `   |         |`::`|
          |     .-;`\..../`;_.-^-._
         /\\/  /  |...::..|`   :   `|
         |:'\ |   /'''::''|   .:.   |
          \ /\;-,/\   ::  |..:::::..|
          | `""`  /   ^^  |   ':'   |
          |       |        \   :   /
          |       |___/\___|`-.:.-`
          |        \_ || _/    `
          |        <_ >< _>
          |        |  ||  |
          |       _\.:||:./_
          |      /____/\____\
"""
)

print("2 - Mago     (Vida: 70, Ataque: 15, Armadura: 5%, Mana: 50)")
print("\n'''ss'''")

print("3 - Arqueiro (Vida: 80, Ataque: 10, Armadura: 10%)")
print("\n'''ss'''")


classe = ""
vida_max = 0
vida = 0
ataque = 0
armadura = 0
mana_max = 0
mana = 0

while True:
    escolha = input("Digite o número da classe escolhida: ")
    if escolha == "1":
        classe = "Guerreiro"
        vida_max = 100
        ataque = 15
        armadura = 0.20
        mana_max = 0
        break
    elif escolha == "2":
        classe = "Mago"
        vida_max = 70
        ataque = 15
        armadura = 0.05
        mana_max = 30
        break
    elif escolha == "3":
        classe = "Arqueiro"
        vida_max = 80
        ataque = 25
        armadura = 0.10
        mana_max = 0
        break
    else:
        print("Escolha inválida.")

vida = vida_max
mana = mana_max

# Inventário e poções
inventario = {
    "poçãoVida": 2,
    "poçãoMana": 2,
}
cura_pocao = 15
cura_pocao_mana = 15


def ataque_magia1():
    # Magia custa 10 mana e causa dano maior
    custo = 10
    if mana >= custo:
        return random.randint(10, 25), custo
    else:
        return 0, 0


def ataque_magia2():
    # Magia de fogo custa 20 mana e causa dano maior
    custo = 20
    if mana >= custo:
        return random.randint(20, 30), custo
    else:
        return 0, 0


def ataque_normal():
    # Ataque normal causa dano entre 5 e 10
    return random.randint(5, 15)


def ataque_inimigo():
    # Ataque do inimigo causa dano entre 5 e 10
    return random.randint(5, inimigo1_ataque + 5)


def ataque_inimigo2():
    # Ataque do inimigo causa dano entre 5 e 10
    return random.randint(5, inimigo2_ataque + 5)


print(f"\n{nome} o {classe}, sua jornada começa!\n")

# --- Encontro 1: Goblin ---
posicao += 1
print(f"[Local: {mapa[posicao]}]")
print(f"-----------------------------------")
inimigo1_nome = "Goblin"
inimigo1_vida = 40
inimigo1_ataque = 10

print(f"Um {inimigo1_nome} aparece!")
while inimigo1_vida > 0 and vida > 0:
    print(
        f"\nSua vida: {vida}/{vida_max} | Mana: {mana}/{mana_max} | Vida do {inimigo1_nome}: {inimigo1_vida}"
    )

    print(f"-----------------------------------")
    print(
        f"Poções de vida: {inventario['poçãoVida']} | Poções de mana: {inventario['poçãoMana']}"
    )

    if classe == "Mago":
        acao = input(
            "Digite 'a' para ataque normal, 'm1' para usar magia de gelo, 'm2' para usar magia de fogo 'p' para poção, 'p2' para poção de mana ou 'f' para fugir: "
        ).lower()
        print(f"-----------------------------------")
    else:
        acao = input(
            "Digite 'a' para atacar, 'p' para poção de vida, 'f' para fugir: "
        ).lower()

    if acao == "a":
        dano = ataque_normal()
        inimigo1_vida -= dano
        print(f"Você atacou o {inimigo1_nome} causando {dano} de dano.")
        print(f"-----------------------------------")
        if inimigo1_vida <= 0:
            print(f"Você derrotou o {inimigo1_nome}!")
            break
        inimigo_dano = ataque_inimigo()
        print(f"{inimigo_dano} de dano ")
        inimigo_dano = inimigo_dano * (1 - armadura)
        print(f"-----------------------------------")
        print(
            f"{inimigo_dano} de danofoi reduzido para {inimigo_dano} por causa da armadura "
        )
        print(f"-----------------------------------")
        vida -= inimigo_dano
        print(f"O {inimigo1_nome} atacou e causou {inimigo_dano} de dano.")

    elif acao == "m1" and classe == "Mago":
        dano_magia, custo = ataque_magia1()
        if custo > 0:
            mana -= custo
            inimigo1_vida -= dano_magia
            print(f"Você usou magia e causou {dano_magia} de dano ao {inimigo1_nome}!")
            print(f"-----------------------------------")
            print(f"Mana atual: {mana}/{mana_max}")
            print(f"-----------------------------------")
            if inimigo1_vida <= 0:
                print(f"Você derrotou o {inimigo1_nome}!")
                break
            inimigo_dano = ataque_inimigo()
            inimigo_dano = inimigo_dano * (1 - armadura)
            vida -= inimigo_dano
            print(f"O {inimigo1_nome} atacou e causou {inimigo_dano} de dano.")
    elif acao == "m2" and classe == "Mago":
        dano_magia, custo = ataque_magia2()
        if custo > 0:
            mana -= custo
            inimigo1_vida -= dano_magia
            print(f"Você usou magia e causou {dano_magia} de dano ao {inimigo1_nome}!")
            print(f"-----------------------------------")
            print(f"Mana atual: {mana}/{mana_max}")
            print(f"-----------------------------------")
            if inimigo1_vida <= 0:
                print(f"Você derrotou o {inimigo1_nome}!")
                break
            inimigo_dano = ataque_inimigo()
            inimigo_dano = inimigo_dano * (1 - armadura)
            vida -= inimigo_dano
            print(f"O {inimigo1_nome} atacou e causou {inimigo_dano} de dano.")
            print(f"-----------------------------------")
        else:
            print("Mana insuficiente!")
    elif acao == "p":
        if inventario.get("poçãoVida", 0) > 0:
            vida += cura_pocao
            if vida > vida_max:
                vida = vida_max
            inventario["poçãoVida"] -= 1
            print(
                f"Você usou uma poção de vida e recuperou {cura_pocao} de vida! Vida atual: {vida}/{vida_max}"
            )
            print(f"-----------------------------------")
        else:
            print("Você não tem mais poções de vida!")
    elif classe == "Mago" and acao == "p2":
        if inventario.get("poçãoMana", 0) > 0:
            mana += cura_pocao_mana
            if mana > mana_max:
                mana = mana_max
            inventario["poçãoMana"] -= 1
            print(
                f"Você usou uma poção de mana e recuperou {cura_pocao_mana} de mana! Mana atual: {mana}/{mana_max}"
            )
            print(f"-----------------------------------")
        else:
            print("Você não tem mais poções de mana!")
    elif acao == "f":
        fugir = random.randint(0, 20)
        if fugir < 18:
            print(f"Você não conseguiu fugir e o {inimigo1_nome} atacou!")
            print(f"-----------------------------------")
            inimigo_dano = ataque_inimigo()
            inimigo_dano = inimigo_dano * (1 - armadura)
            vida -= inimigo_dano
        else:
            print("Você conseguiu fugir!")
            break
    else:
        print("Comando inválido.")


# --- Enigma antes do Orc ---
if vida > 0:
    posicao += 1
    print(f"\n[Local: {mapa[posicao]}]")
    print(f"-----------------------------------")
    print("Você encontra uma porta com uma escrita misteriosa:")
    print(f"-----------------------------------")
    print(
        "O que é o que é: clara e salgada, cabe em um olho e pesa mais de uma tonelada?"
    )
    resposta = input("Digite sua resposta: ")

    while resposta.lower().strip() != "lagrima":
        resposta = input("Resposta incorreta. Tente novamente: ")

    print("A porta se abre lentamente...\n")


# --- Encontro 2: Orc ---
if vida > 0:
    posicao += 1
    print(f"[Local: {mapa[posicao]}]")
    inimigo2_nome = "Orc"
    inimigo2_vida = 90
    inimigo2_ataque = 15

    print(f"Um {inimigo2_nome} enorme bloqueia seu caminho!")
    print(f"-----------------------------------")
    while inimigo2_vida > 0 and vida > 0:
        print(
            f"\nSua vida: {vida}/{vida_max} | Mana: {mana}/{mana_max} | Vida do {inimigo2_nome}: {inimigo2_vida}"
        )
        print(f"-----------------------------------")
        print(
            f"Poções de vida: {inventario['poçãoVida']} | Poções de mana: {inventario['poçãoMana']}"
        )

        if classe == "Mago":
            acao = input(
                "Digite 'a' para ataque normal, 'm1' para usar magia, 'm2' para magia de fogo, 'p' para poção, 'p2' para poção de mana ou 'f' para fugir: "
            ).lower()
        else:
            acao = input(
                "Digite 'a' para atacar, 'p' para poção ou 'f' para fugir: "
            ).lower()

        if acao == "a":
            dano = random.randint(ataque, ataque + 5)
            inimigo2_vida -= dano
            print(f"Você atacou o {inimigo2_nome} causando {dano} de dano.")
            print(f"-----------------------------------")
            if inimigo2_vida <= 0:
                print(f"Você derrotou o {inimigo2_nome}! Vitória!")
                break
            inimigo_dano = random.randint(inimigo2_ataque, inimigo2_ataque + 3)
            inimigo_dano = inimigo_dano * (1 - armadura)
            vida -= inimigo_dano
            print(f"O {inimigo2_nome} atacou e causou {inimigo_dano} de dano.")

        elif acao == "m1" and classe == "Mago":
            dano_magia, custo = ataque_magia1()
            if custo > 0:
                mana -= custo
                inimigo2_vida -= dano_magia
                print(
                    f"Você usou magia e causou {dano_magia} de dano ao {inimigo2_nome}!"
                )
                print(f"-----------------------------------")
                print(f"Mana atual: {mana}/{mana_max}")
                print(f"-----------------------------------")
                if inimigo2_vida <= 0:
                    print(f"Você derrotou o {inimigo2_nome}! Vitória!")
                    break
                inimigo_dano = random.randint(inimigo2_ataque, inimigo2_ataque + 3)
                inimigo_dano = inimigo_dano * (1 - armadura)
                vida -= inimigo_dano
                print(f"O {inimigo2_nome} atacou e causou {inimigo_dano} de dano.")
            else:
                print("Mana insuficiente!")

        elif acao == "m2" and classe == "Mago":
            dano_magia, custo = ataque_magia2()
            if custo > 0:
                mana -= custo
                inimigo2_vida -= dano_magia
                print(
                    f"Você usou magia e causou {dano_magia} de dano ao {inimigo2_nome}!"
                )
                print(f"-----------------------------------")
                print(f"Mana atual: {mana}/{mana_max}")
                print(f"-----------------------------------")
                if inimigo2_vida <= 0:
                    print(f"Você derrotou o {inimigo2_nome}! Vitória!")
                    break
                inimigo_dano = random.randint(inimigo2_ataque, inimigo2_ataque + 3)
                inimigo_dano = inimigo_dano * (1 - armadura)
                vida -= inimigo_dano
                print(f"O {inimigo2_nome} atacou e causou {inimigo_dano} de dano.")
            else:
                print("Mana insuficiente!")

        elif acao == "p":
            if inventario["poçãoVida"] > 0:
                vida += cura_pocao
                if vida > vida_max:
                    vida = vida_max
                inventario["poçãoVida"] -= 1
                print(
                    f"Você usou uma poção e recuperou {cura_pocao} de vida! Vida atual: {vida}/{vida_max}"
                )
                print(f"-----------------------------------")
            else:
                print("Você não tem mais poções!")
        elif classe == "Mago" and acao == "p2":
            if inventario["poçãoMana"] > 0:
                mana += cura_pocao_mana
                if mana > mana_max:
                    mana = mana_max
                inventario["poçãoMana"] -= 1
                print(
                    f"Você usou uma poção de mana e recuperou {cura_pocao_mana} de mana! Mana atual: {mana}/{mana_max}"
                )
                print(f"-----------------------------------")
            else:
                print("Você não tem mais poções de mana!")

        elif acao == "f":
            fugir = random.randint(0, 20)
            if fugir < 18:
                print(f"Você não conseguiu fugir e o {inimigo2_nome} atacou!")
                print(f"-----------------------------------")
                inimigo_dano = random.randint(inimigo2_ataque, inimigo2_ataque + 3)
                inimigo_dano = inimigo_dano * (1 - armadura)
                vida -= inimigo_dano
                print(f"O {inimigo2_nome} atacou e causou {inimigo_dano} de dano.")
            else:
                print("Você conseguiu fugir!")
                break
        else:
            print("Comando inválido.")

# --- Fim do jogo ---
if vida > 0 and inimigo2_vida <= 0:
    posicao += 1
    print(f"\n[Local: {mapa[posicao]}]")
    print(f"-----------------------------------")
    print(
        f"Parabéns, {nome} o {classe}! Você encontrou o tesouro e completou sua jornada com sucesso!"
    )
else:
    print(f"\n{nome} foi derrotado em batalha. Fim de jogo.")

print("Obrigado por jogar!")
