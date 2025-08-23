████████████████████████████████████████████████████████
             CNA REMINDER BOT
Ferramenta para professores do CNA enviarem lembretes 
automáticos no grupo de coordenação do WhatsApp Desktop
████████████████████████████████████████████████████████

🚀 COMO USAR:

1️⃣ Abra o WhatsApp Desktop no seu PC e deixe a janela
   visível e logada.

2️⃣ Abra o terminal (ou PowerShell) na pasta do projeto:
   > python -m cna_reminder.main

3️⃣ Responda às perguntas do programa:
   - Seu nome (aparecerá como "Teacher XXX")
   - Turma (escolha pelo ID)
   - Unidade encerrada
   - Data de entrega

4️⃣ O programa vai gerar a mensagem automaticamente e
   copiar para a área de transferência. Ele vai avisar:
   "Você tem 15 segundos para colocar o cursor na caixa
   de mensagem do grupo".

5️⃣ Após os 15 segundos, a mensagem será colada no
   grupo. Você deve pressionar Enter manualmente para
   enviar.

💡 DICAS IMPORTANTES:

- O nome do grupo no `config.py` deve ser exatamente
  igual ao do WhatsApp Desktop:
  COORDINATION_GROUP = "R.I. - LUCAS MARIA"
- Certifique-se de que a janela do WhatsApp Desktop
  está em foco e visível antes de rodar o script.
- O programa registra automaticamente a data/hora do
  envio na coluna `enviado_em` do Excel.

📊 ESTRUTURA DO EXCEL:

Arquivo: data/cna_livros.xlsx

Colunas obrigatórias:
- turma_id      : número único da turma
- turma_nome    : nome completo da turma
- livro_nome    : nome do livro
- unidade       : número da unidade
- paginas       : páginas da lição de casa
- enviado_em    : preenchido automaticamente após envio

Exemplo:

ID | Turma                        | Livro       | Unidade | Páginas       | Enviado
---|-------------------------------|------------|---------|---------------|--------
1  | Teens 2 - A (Seg/Qua 18h)     | Teens 2    | 1       | 29, 30, 31, 32|
1  | Teens 2 - A (Seg/Qua 18h)     | Teens 2    | 2       | 45-48         |
2  | Kids 3 - B (Ter/Qui 17h)      | Kids 3     | 1       | 15, 16        |

✨ PRONTO! Agora você tem uma ferramenta para enviar
lembretes automáticos e registrar tudo de forma organizada.
