# CNA REMINDER BOT

Ferramenta para professores do CNA enviarem **lembretes automáticos** no grupo de coordenação do WhatsApp Desktop.  

---

## 🚀 Como instalar

1️⃣ Clone este repositório:

```bash
git clone https://github.com/seuusuario/cna-reminder.git
cd cna-reminder
```

2️⃣ Crie e ative um **ambiente virtual** (opcional, mas recomendado):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate
```

3️⃣ Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🖥 Como usar

1️⃣ Abra o **WhatsApp Desktop** no seu computador e deixe a janela visível e logada.  

2️⃣ Execute o programa:

```bash
python -m cna_reminder.main
```

3️⃣ Responda às perguntas do programa:  
- Seu nome (aparecerá como "Teacher XXX")  
- Turma (escolha pelo ID)  
- Unidade encerrada  
- Data de entrega  

4️⃣ O programa vai gerar a mensagem automaticamente e copiá-la para a área de transferência. Ele avisará:

```
Você tem 15 segundos para colocar o cursor na caixa de mensagem do grupo
```

5️⃣ Após os 15 segundos:  
- A **mensagem principal** será enviada automaticamente.  
- Em seguida, será enviada a **segunda mensagem automática**:  
```
Enviar para a turma {livro_nome}.
```

---

## 💡 Dicas importantes

- O nome do grupo no `config.py` deve ser exatamente igual ao do WhatsApp Desktop:

```python
COORDINATION_GROUP = "NOME DO GRUPO"
```

- Certifique-se de que a janela do WhatsApp Desktop está em foco antes de rodar o script.  
- Feche o Excel antes de rodar o programa para evitar erros ao salvar a planilha.  
- O programa registra automaticamente a **data/hora do envio** na coluna `enviado_em` do Excel.  
- Caso o Excel esteja aberto, você receberá uma mensagem de erro e deve fechá-lo antes de tentar novamente.  

---

## 📊 Estrutura do Excel

Arquivo: `data/cna_livros.xlsx`  

Colunas obrigatórias:  
- `turma_id`      : número único da turma  
- `turma_nome`    : nome completo da turma  
- `livro_nome`    : nome do livro  
- `unidade`       : número da unidade  
- `paginas`       : páginas da lição de casa  
- `enviado_em`    : preenchido automaticamente após envio  

Exemplo:

| ID | Turma                        | Livro       | Unidade | Páginas       | Enviado |
|----|-------------------------------|------------|---------|---------------|--------|
| 1  | Kids 1                        | Kids 1     | 1       | 30-33         |        |
| 2  | Kids 2                        | Kids 2     | 1       | 15-18         |        |
| 3  | Teen Up 2                     | Teen Up 2  | 1       | 29-32         |        |

---

## ✅ Recursos

- Envio automático de mensagens via **WhatsApp Desktop**.  
- Segunda mensagem automática para lembrar da turma (`Enviar para a turma {livro_nome}`).  
- Registro automático da data/hora no Excel.  
- Configuração fácil para qualquer turma e livro.

---

✨ Agora qualquer professor pode usar o **CNA Reminder Bot** para enviar lembretes automáticos e registrar tudo de forma organizada, sem complicações.  
