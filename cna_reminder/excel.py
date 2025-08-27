import pandas as pd
from datetime import datetime

EXCEL_PATH = "data/cna_livros.xlsx"

# Antes estava 'load_data', volta para 'carregar_turmas'
def carregar_turmas():
    return pd.read_excel(EXCEL_PATH)

# Antes estava 'mark_sent', volta para 'registrar_envio'
def registrar_envio(df, turma_id, unidade):
    df.loc[
        (df["turma_id"] == turma_id) & (df["unidade"] == unidade),
        "enviado_em"
    ] = datetime.now()
    df.to_excel(EXCEL_PATH, index=False)
