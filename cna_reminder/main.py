import pandas as pd
from . import excel, message, whatsapp

def main():
    teacher = input("Digite seu nome (para aparecer depois de 'Teacher'): ").strip()
    if not teacher:
        teacher = "Lucas"

    df = excel.load_data()
    turmas = df[["turma_id", "turma_nome", "livro_nome"]].drop_duplicates()

    print("\nTurmas disponíveis:")
    for i, row in turmas.iterrows():
        print(f"{row['turma_id']}. {row['turma_nome']} ({row['livro_nome']})")

    turma_id = int(input("\nDigite o ID da turma: "))
    unidade = int(input("Digite a unidade encerrada: "))
    data_entrega = input("Digite a data de entrega (ex: 13/8/2025): ")

    row = df[(df["turma_id"] == turma_id) & (df["unidade"] == unidade)]
    if row.empty:
        print("[ERRO] Não encontrei essa turma/unidade na planilha.")
        return

    turma_nome = row.iloc[0]["turma_nome"]
    paginas = row.iloc[0]["paginas"]

    msg = message.generate_message(teacher, turma_nome, paginas, unidade, data_entrega)
    print("\n--- Mensagem ---\n")
    print(msg)
    print("\n----------------\n")

    # Enviar no WhatsApp
    whatsapp.send_message(msg)

    # Marcar no Excel
    excel.mark_sent(df, turma_id, unidade)

if __name__ == "__main__":
    main()
