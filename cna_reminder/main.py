# main.py
from cna_reminder.excel import carregar_turmas, registrar_envio
from cna_reminder.whatsapp import send_message

def main():
    # Carrega dados do Excel
    df = carregar_turmas()

    # Perguntas iniciais
    teacher = input("Digite seu nome (para aparecer depois de 'Teacher'): ")

    # Listar turmas disponíveis
    print("\nTurmas disponíveis:")
    for _, row in df.drop_duplicates("turma_id").iterrows():
        print(f"{row['turma_id']}. {row['turma_nome']}   ({row['livro_nome']})")

    turma_id = int(input("\nDigite o ID da turma: "))
    unidade = int(input("Digite a unidade encerrada: "))
    data_entrega = input("Digite a data de entrega (ex: 25/8/2025): ")

    # Seleciona linha correspondente no Excel
    linha = df[(df["turma_id"] == turma_id) & (df["unidade"] == unidade)].iloc[0]
    turma_nome = linha["turma_nome"]
    livro_nome = linha["livro_nome"]
    paginas = linha["paginas"]

    # Monta mensagem principal
    msg = (
        f"Olá, queridos alunos e responsáveis da turma {turma_nome},\n\n"
        f"Para a aula do dia {data_entrega}, os alunos deverão entregar as atividades de casa "
        f"das páginas {paginas} da Unit {unidade}.\n"
        "Não esqueçam de também fazer as Web Lessons!\n"
        "Atenciosamente,\n\n"
        f"Teacher {teacher}"
    )

    print("\n--- Mensagem ---\n")
    print(msg)
    print("\n----------------\n")

    # Enviar mensagem via WhatsApp Desktop
    send_message(msg, turma_nome, livro_nome)

    # Marca no Excel que a mensagem foi enviada
    registrar_envio(df, turma_id, unidade)


if __name__ == "__main__":
    main()
