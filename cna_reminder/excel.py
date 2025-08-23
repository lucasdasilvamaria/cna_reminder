import pandas as pd
from datetime import datetime
from pathlib import Path
from .config import EXCEL_PATH

def load_data():
    return pd.read_excel(EXCEL_PATH)

def save_data(df):
    df.to_excel(EXCEL_PATH, index=False)

def mark_sent(df, turma_id, unidade):
    mask = (df["turma_id"] == turma_id) & (df["unidade"] == unidade)
    df.loc[mask, "enviado_em"] = datetime.now().strftime("%d/%m/%Y %H:%M")
    save_data(df)
