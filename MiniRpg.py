import random
import os

def limpar_tela():
    os.system("clear")

limpar_tela()
print("Bem-vindo ao Mini RPG!")
nome = input("Digite o nome do seu personagem: ")

# Mapa simples com progresso
posicao = 0
mapa = ["Entrada", "Sala do Goblin", "Porta com Enigma", "Sala do Orc", "Tesouro"]

limpar_tela()
print("\nEscolha sua classe:")

print("1 - Guerreiro (Vida: 100, Ataque: 15, Armadura: 20%)")
print("2 - Mago     (Vida: 70, Ataque: 15, Armadura: 5%, Mana: 50)")
print("3 - Arqueiro (Vida: 80, Ataque: 10, Armadura: 10%)")

classe = ""
vida_max = 0
vida = 0
ataque = 0
defesa = 0
armadura = 0
mana_max = 0
mana = 0

while True:
    escolha = input("Digite o número da classe escolhida: ")
    if escolha == "1":
        classe = "Guerreiro"
        vida_max = 100
        ataque = 15
        defesa = 12
        armadura = 0.20
        mana_max = 0
        break
    elif escolha == "2":
        classe = "Mago"
        vida_max = 70
        ataque = 15
        defesa = 10
        armadura = 0.05
        mana_max = 30
        break
    elif escolha == "3":
        classe = "Arqueiro"
        vida_max = 80
        ataque = 25
        defesa = 13
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
    custo = 10
    if mana >= custo:
        return random.randint(10, 25), custo
    else:
        return 0, 0

def ataque_magia2():
    custo = 20
    if mana >= custo:
        return random.randint(20, 30), custo
    else:
        return 0, 0

def ataque_normal():
    return random.randint(5, 15)

def ataque_inimigo():
    return random.randint(5, inimigo1_ataque + 5)

def ataque_inimigo2():
    return random.randint(5, inimigo2_ataque + 5)

limpar_tela()
print(f"\n{nome} o {classe}, sua jornada começa!\n")

# --- Encontro 1: Goblin ---
posicao += 1
limpar_tela()
print(f"[Local: {mapa[posicao]}]")
print(f"-----------------------------------")
inimigo1_nome = "Goblin"
inimigo1_vida = 40
inimigo1_ataque = 10
defesa_inimigo1 = 12

print(f"Um {inimigo1_nome} aparece!")
while inimigo1_vida > 0 and vida > 0:
    limpar_tela()
    print(
        f"\nSua vida: {vida:.1f}/{vida_max:.1f} | Mana: {mana:.1f}/{mana_max:.1f} | Vida do {inimigo1_nome}: {inimigo1_vida:.1f}"
    )
    print(f"-----------------------------------")
    print(
        f"Poções de vida: {inventario['poçãoVida']} | Poções de mana: {inventario['poçãoMana']}"
    )

    if classe == "Mago":
        acao = input(
            "Digite:\n"
            "  'a'  para ataque normal\n"
            "  'm1' para usar magia de gelo\n"
            "  'm2' para usar magia de fogo\n"
            "  'p'  para poção de vida\n"
            "  'p2' para poção de mana\n"
            "  'f'  para fugir\n"
            "Escolha: "
        ).lower()
        print(f"-----------------------------------")
    else:
        acao = input(
            "Digite:\n"
            "  'a' para atacar\n"
            "  'p' para poção de vida\n"
            "  'f' para fugir\n"
            "Escolha: "
        ).lower()

    if acao == "a":
        ataque = random.randint(0, 20)
        if ataque < defesa_inimigo1:
            print(f"seu ataque é {ataque:.1f} defesa do inimigo é {defesa_inimigo1:.1f}")
            print(f"------------------------------------")
            print(f"Seu ataque falhou!")
            print(f"-----------------------------------")
            input("Pressione ENTER para continuar...")
        else:
            dano = ataque_normal()
            inimigo1_vida -= dano
            print(f"Você atacou o {inimigo1_nome} causando {dano:.1f} de dano.")
            print(f"-----------------------------------")
            if inimigo1_vida <= 0:
                print(f"Você derrotou o {inimigo1_nome}!")
                input("Pressione ENTER para continuar...")
                break

        inimigo_dano = ataque_inimigo()
        if inimigo_dano < defesa:
            print(f"Sua defesa é {defesa:.1f} ataque do inimigo é {inimigo_dano:.1f}")
            print(f"------------------------------------")
            print(f"Inimigo errou o ataque!")
            print(f"-----------------------------------")
            input("Pressione ENTER para continuar...")
        else:
            print(f"{inimigo_dano:.1f} de dano ")
            inimigo_dano_reduzido = inimigo_dano * (1 - armadura)
            print(f"-----------------------------------")
            print(
                f"{inimigo_dano:.1f} de dano foi reduzido para {inimigo_dano_reduzido:.1f} por causa da armadura "
            )
            print(f"-----------------------------------")
            vida -= inimigo_dano_reduzido
            print(
                f"O {inimigo1_nome} atacou e causou {inimigo_dano_reduzido:.1f} de dano."
            )
            input("Pressione ENTER para continuar...")

    elif acao == "m1" and classe == "Mago":
        dano_magia, custo = ataque_magia1()
        if custo > 0:
            rolagem = random.randint(0, 20)
            print(f"Rolagem do dado para magia: {rolagem} (defesa do inimigo: {defesa_inimigo1})")
            if rolagem < defesa_inimigo1:
                print("Sua magia falhou!")
                print(f"-----------------------------------")
                input("Pressione ENTER para continuar...")
            else:
                mana -= custo
                inimigo1_vida -= dano_magia
                print(
                    f"Você usou magia e causou {dano_magia:.1f} de dano ao {inimigo1_nome}!"
                )
                print(f"-----------------------------------")
                print(f"Mana atual: {mana:.1f}/{mana_max:.1f}")
                print(f"-----------------------------------")
                if inimigo1_vida <= 0:
                    print(f"Você derrotou o {inimigo1_nome}!")
                    input("Pressione ENTER para continuar...")
                    break
            inimigo_dano = ataque_inimigo()
            if inimigo_dano < defesa:
                print(f"Inimigo errou o ataque!")
                print(f"-----------------------------------")
                input("Pressione ENTER para continuar...")
            else:
                print(f"{inimigo_dano:.1f} de dano ")
                inimigo_dano_reduzido = inimigo_dano * (1 - armadura)
                print(f"-----------------------------------")
                print(
                    f"{inimigo_dano:.1f} de dano foi reduzido para {inimigo_dano_reduzido:.1f} por causa da armadura "
                )
                print(f"-----------------------------------")
                vida -= inimigo_dano_reduzido
                print(
                    f"O {inimigo1_nome} atacou e causou {inimigo_dano_reduzido:.1f} de dano."
                )
                input("Pressione ENTER para continuar...")
        else:
            print("Mana insuficiente!")
            input("Pressione ENTER para continuar...")

    elif acao == "m2" and classe == "Mago":
        dano_magia, custo = ataque_magia2()
        if custo > 0:
            rolagem = random.randint(0, 20)
            print(f"Rolagem do dado para magia: {rolagem} (defesa do inimigo: {defesa_inimigo1})")
            if rolagem < defesa_inimigo1:
                print("Sua magia falhou!")
                print(f"-----------------------------------")
                input("Pressione ENTER para continuar...")
            else:
                mana -= custo
                inimigo1_vida -= dano_magia
                print(
                    f"Você usou magia e causou {dano_magia:.1f} de dano ao {inimigo1_nome}!"
                )
                print(f"-----------------------------------")
                print(f"Mana atual: {mana:.1f}/{mana_max:.1f}")
                print(f"-----------------------------------")
                if inimigo1_vida <= 0:
                    print(f"Você derrotou o {inimigo1_nome}!")
                    input("Pressione ENTER para continuar...")
                    break
            inimigo_dano = ataque_inimigo()
            if inimigo_dano < defesa:
                print(f"Inimigo errou o ataque!")
                print(f"-----------------------------------")
                input("Pressione ENTER para continuar...")
            else:
                print(f"{inimigo_dano:.1f} de dano ")
                inimigo_dano_reduzido = inimigo_dano * (1 - armadura)
                print(f"-----------------------------------")
                print(
                    f"{inimigo_dano:.1f} de dano foi reduzido para {inimigo_dano_reduzido:.1f} por causa da armadura "
                )
                print(f"-----------------------------------")
                vida -= inimigo_dano_reduzido
                print(
                    f"O {inimigo1_nome} atacou e causou {inimigo_dano_reduzido:.1f} de dano."
                )
                input("Pressione ENTER para continuar...")
        else:
            print("Mana insuficiente!")
            input("Pressione ENTER para continuar...")

    elif acao == "p":
        if inventario.get("poçãoVida", 0) > 0:
            vida += cura_pocao
            if vida > vida_max:
                vida = vida_max
            inventario["poçãoVida"] -= 1
            print(
                f"Você usou uma poção de vida e recuperou {cura_pocao:.1f} de vida! Vida atual: {vida:.1f}/{vida_max:.1f}"
            )
            print(f"-----------------------------------")
        else:
            print("Você não tem mais poções de vida!")
        input("Pressione ENTER para continuar...")
    elif classe == "Mago" and acao == "p2":
        if inventario.get("poçãoMana", 0) > 0:
            mana += cura_pocao_mana
            if mana > mana_max:
                mana = mana_max
            inventario["poçãoMana"] -= 1
            print(
                f"Você usou uma poção de mana e recuperou {cura_pocao_mana:.1f} de mana! Mana atual: {mana:.1f}/{mana_max:.1f}"
            )
            print(f"-----------------------------------")
        else:
            print("Você não tem mais poções de mana!")
        input("Pressione ENTER para continuar...")
    elif acao == "f":
        fugir = random.randint(0, 20)
        if fugir < 18:
            print(f"Você não conseguiu fugir e o {inimigo1_nome} atacou!")
            print(f"-----------------------------------")
            inimigo_dano = ataque_inimigo()
            if inimigo_dano < defesa:
                print(f"Inimigo errou o ataque!")
                print(f"-----------------------------------")
            else:
                inimigo_dano_reduzido = inimigo_dano * (1 - armadura)
                vida -= inimigo_dano_reduzido
                print(
                    f"O {inimigo1_nome} atacou e causou {inimigo_dano_reduzido:.1f} de dano."
                )
        else:
            print("Você conseguiu fugir!")
            break
        input("Pressione ENTER para continuar...")
    else:
        print("Comando inválido.")
        input("Pressione ENTER para continuar...")

# --- Enigma antes do Orc ---
if vida > 0:
    posicao += 1
    limpar_tela()
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
    input("Pressione ENTER para continuar...")

# --- Encontro 2: Orc ---
if vida > 0:
    posicao += 1
    limpar_tela()
    print(f"[Local: {mapa[posicao]}]")
    inimigo2_nome = "Orc"
    inimigo2_vida = 90
    inimigo2_ataque = 15
    defesa_inimigo2 = 12

    print(f"Um {inimigo2_nome} enorme bloqueia seu caminho!")
    print(f"-----------------------------------")
    while inimigo2_vida > 0 and vida > 0:
        limpar_tela()
        print(
            f"\nSua vida: {vida:.1f}/{vida_max:.1f} | Mana: {mana:.1f}/{mana_max:.1f} | Vida do {inimigo2_nome}: {inimigo2_vida:.1f}"
        )
        print(f"-----------------------------------")
        print(
            f"Poções de vida: {inventario['poçãoVida']} | Poções de mana: {inventario['poçãoMana']}"
        )

        if classe == "Mago":
            acao = input(
                "Digite:\n"
                "  'a'  para ataque normal\n"
                "  'm1' para usar magia\n"
                "  'm2' para magia de fogo\n"
                "  'p'  para poção de vida\n"
                "  'p2' para poção de mana\n"
                "  'f'  para fugir\n"
                "Escolha: "
            ).lower()
        else:
            acao = input(
                "Digite:\n"
                "  'a' para atacar\n"
                "  'p' para poção\n"
                "  'f' para fugir\n"
                "Escolha: "
            ).lower()

        if acao == "a":
            ataque = random.randint(0, 20)
            print(f"Rolagem do dado para ataque: {ataque} (defesa do inimigo: {defesa_inimigo2})")
            print(f"-----------------------------------")
            if ataque < defesa_inimigo2:
                print(f"Seu ataque falhou!")
                print(f"-----------------------------------")
                input("Pressione ENTER para continuar...")
            else:
                dano = random.randint(ataque, ataque + 5)
                inimigo2_vida -= dano
                print(f"Você atacou o {inimigo2_nome} causando {dano:.1f} de dano.")
                print(f"-----------------------------------")
                if inimigo2_vida <= 0:
                    print(f"Você derrotou o {inimigo2_nome}! Vitória!")
                    input("Pressione ENTER para continuar...")
                    break
            inimigo_dano = random.randint(0, 20)
            if inimigo_dano < defesa:
                print(f"Sua defesa é {defesa:.1f} ataque do inimigo é {inimigo_dano:.1f}")
                print(f"------------------------------------")
                print(f"Inimigo errou o ataque!")
                print(f"-----------------------------------")
                input("Pressione ENTER para continuar...")
            else:
                print(f"{inimigo_dano:.1f} de dano ")
                inimigo_dano_reduzido = inimigo_dano * (1 - armadura)
                print(f"-----------------------------------")
                print(
                    f"{inimigo_dano:.1f} de dano foi reduzido para {inimigo_dano_reduzido:.1f} por causa da armadura "
                )
                print(f"-----------------------------------")
                vida -= inimigo_dano_reduzido
                print(
                    f"O {inimigo2_nome} atacou e causou {inimigo_dano_reduzido:.1f} de dano."
                )
                input("Pressione ENTER para continuar...")

        elif acao == "m1" and classe == "Mago":
            dano_magia, custo = ataque_magia1()
            if custo > 0:
                rolagem = random.randint(0, 20)
                print(f"Rolagem do dado para magia: {rolagem} (defesa do inimigo: {defesa_inimigo2})")
                if rolagem < defesa_inimigo2:
                    print("Sua magia falhou!")
                    print(f"-----------------------------------")
                    input("Pressione ENTER para continuar...")
                else:
                    mana -= custo
                    inimigo2_vida -= dano_magia
                    print(
                        f"Você usou magia e causou {dano_magia:.1f} de dano ao {inimigo2_nome}!"
                    )
                    print(f"-----------------------------------")
                    print(f"Mana atual: {mana:.1f}/{mana_max:.1f}")
                    print(f"-----------------------------------")
                    if inimigo2_vida <= 0:
                        print(f"Você derrotou o {inimigo2_nome}! Vitória!")
                        input("Pressione ENTER para continuar...")
                        break
                inimigo_dano = random.randint(inimigo2_ataque, inimigo2_ataque + 3)
                if inimigo_dano < defesa:
                    print(f"Inimigo errou o ataque!")
                    print(f"-----------------------------------")
                    input("Pressione ENTER para continuar...")
                else:
                    print(f"{inimigo_dano:.1f} de dano ")
                    inimigo_dano_reduzido = inimigo_dano * (1 - armadura)
                    print(f"-----------------------------------")
                    print(
                        f"{inimigo_dano:.1f} de dano foi reduzido para {inimigo_dano_reduzido:.1f} por causa da armadura "
                    )
                    print(f"-----------------------------------")
                    vida -= inimigo_dano_reduzido
                    print(
                        f"O {inimigo2_nome} atacou e causou {inimigo_dano_reduzido:.1f} de dano."
                    )
                    input("Pressione ENTER para continuar...")
            else:
                print("Mana insuficiente!")
                input("Pressione ENTER para continuar...")

        elif acao == "m2" and classe == "Mago":
            dano_magia, custo = ataque_magia2()
            if custo > 0:
                rolagem = random.randint(0, 20)
                print(f"Rolagem do dado para magia: {rolagem} (defesa do inimigo: {defesa_inimigo2})")
                if rolagem < defesa_inimigo2:
                    print("Sua magia falhou!")
                    print(f"-----------------------------------")
                    input("Pressione ENTER para continuar...")
                else:
                    mana -= custo
                    inimigo2_vida -= dano_magia
                    print(
                        f"Você usou magia e causou {dano_magia:.1f} de dano ao {inimigo2_nome}!"
                    )
                    print(f"-----------------------------------")
                    print(f"Mana atual: {mana:.1f}/{mana_max:.1f}")
                    print(f"-----------------------------------")
                    if inimigo2_vida <= 0:
                        print(f"Você derrotou o {inimigo2_nome}! Vitória!")
                        input("Pressione ENTER para continuar...")
                        break
                inimigo_dano = random.randint(inimigo2_ataque, inimigo2_ataque + 3)
                if inimigo_dano < defesa:
                    print(f"Inimigo errou o ataque!")
                    print(f"-----------------------------------")
                    input("Pressione ENTER para continuar...")
                else:
                    print(f"{inimigo_dano:.1f} de dano ")
                    inimigo_dano_reduzido = inimigo_dano * (1 - armadura)
                    print(f"-----------------------------------")
                    print(
                        f"{inimigo_dano:.1f} de dano foi reduzido para {inimigo_dano_reduzido:.1f} por causa da armadura "
                    )
                    print(f"-----------------------------------")
                    vida -= inimigo_dano_reduzido
                    print(
                        f"O {inimigo2_nome} atacou e causou {inimigo_dano_reduzido:.1f} de dano."
                    )
                    input("Pressione ENTER para continuar...")
            else:
                print("Mana insuficiente!")
                input("Pressione ENTER para continuar...")

        elif acao == "p":
            if inventario["poçãoVida"] > 0:
                vida += cura_pocao
                if vida > vida_max:
                    vida = vida_max
                inventario["poçãoVida"] -= 1
                print(
                    f"Você usou uma poção e recuperou {cura_pocao:.1f} de vida! Vida atual: {vida:.1f}/{vida_max:.1f}"
                )
                print(f"-----------------------------------")
            else:
                print("Você não tem mais poções!")
            input("Pressione ENTER para continuar...")
        elif classe == "Mago" and acao == "p2":
            if inventario["poçãoMana"] > 0:
                mana += cura_pocao_mana
                if mana > mana_max:
                    mana = mana_max
                inventario["poçãoMana"] -= 1
                print(
                    f"Você usou uma poção de mana e recuperou {cura_pocao_mana:.1f} de mana! Mana atual: {mana:.1f}/{mana_max:.1f}"
                )
                print(f"-----------------------------------")
            else:
                print("Você não tem mais poções de mana!")
            input("Pressione ENTER para continuar...")

        elif acao == "f":
            fugir = random.randint(0, 20)
            if fugir < 18:
                print(f"Você não conseguiu fugir e o {inimigo2_nome} atacou!")
                print(f"-----------------------------------")
                inimigo_dano = random.randint(inimigo2_ataque, inimigo2_ataque + 3)
                if inimigo_dano < defesa:
                    print(f"Inimigo errou o ataque!")
                    print(f"-----------------------------------")
                else:
                    inimigo_dano_reduzido = inimigo_dano * (1 - armadura)
                    vida -= inimigo_dano_reduzido
                    print(
                        f"O {inimigo2_nome} atacou e causou {inimigo_dano_reduzido:.1f} de dano."
                    )
            else:
                print("Você conseguiu fugir!")
                break
            input("Pressione ENTER para continuar...")
        else:
            print("Comando inválido.")
            input("Pressione ENTER para continuar...")

# --- Fim do jogo ---
if vida > 0 and inimigo2_vida <= 0:
    posicao += 1
    limpar_tela()
    print(f"\n[Local: {mapa[posicao]}]")
    print(f"-----------------------------------")
    print(
        f"Parabéns, {nome} o {classe}! Você encontrou o tesouro e completou sua jornada com sucesso!"
    )
else:
    limpar_tela()
    print(f"\n{nome} foi derrotado em batalha. Fim de jogo.")

print("Obrigado por jogar!")