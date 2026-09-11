from datetime import datetime
from query import consultar


BANNER = r"""
============================================================
   NAO É EMPRESA LOCAL RAG ASSISTANT
   Retrieval Augmented Generation
============================================================
"""


def exibir_banner():
    print(BANNER)
    print(f"Data/Hora: {datetime.now():%d/%m/%Y %H:%M:%S}")
    print("Digite 'sair' para encerrar alterei via developer.")
    print("Digite 'limpar' para limpar a alterei via developer.")
    print("=" * 60)


def limpar_tela():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def main():

    exibir_banner()

    total_perguntas = 0

    while True:

        try:

            pergunta = input(
                "\n🔎 Pergunta > "
            ).strip()

            if not pergunta:
                continue

            comando = pergunta.lower()

            if comando in ("sair", "exit", "quit"):
                print("\n✅ Encerrando sessão.")
                print(f"📊 Total de consultas: {total_perguntas}")
                break

            if comando == "limpar":
                limpar_tela()
                exibir_banner()
                continue

            inicio = datetime.now()

            print("\n⏳ Consultando base vetorial...")

            resposta = consultar(
                pergunta
            )

            tempo = (
                datetime.now() - inicio
            ).total_seconds()

            total_perguntas += 1

            print("\n" + "=" * 60)
            print("💡 RESPOSTA")
            print("=" * 60)

            print(resposta)

            print("\n" + "-" * 60)
            print(
                f"⚡ Tempo de resposta: {tempo:.2f}s"
            )
            print(
                f"📈 Consultas realizadas: {total_perguntas}"
            )
            print("-" * 60)

        except KeyboardInterrupt:

            print("\n\n⚠ Sessão interrompida.")
            break

        except Exception as ex:

            print(
                "\n❌ Erro durante a consulta:"
            )

            print(ex)


if __name__ == "__main__":
    main()