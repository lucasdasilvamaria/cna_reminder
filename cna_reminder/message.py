def generate_message(teacher, turma_nome, paginas, unidade, data_entrega):
    return (
        f"Olá, queridos alunos e responsáveis da turma {turma_nome}\n\n"
        f"Para a aula do dia {data_entrega}, os alunos deverão entregar as atividades de casa das páginas {paginas} da Unit {unidade}.\n"
        "Não esqueçam de também fazer as Web Lessons!\n"
        "Atenciosamente,\n\n"
        f"Teacher {teacher}"
    )
