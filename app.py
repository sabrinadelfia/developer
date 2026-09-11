from query import consultar
## ALTEREO E AGORA QUERO UM MERGE
print("=" * 60)
print("RAG LOCAL")
print("=" * 60)

while True:

    pergunta = input(
        "\nPergunta: "
    )

    if pergunta.lower() in [
        "sair",
        "exit",
        "quit"
    ]:

        break

    resposta = consultar(
        pergunta
    )

    print(
        "\nResposta:\n"
    )

    print(
        resposta
    )

    print("forçandoalteracao")