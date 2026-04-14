import os
import pandas as pd
from sqlalchemy import create_engine
import json

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/lab_db")
REPORT_PATH = "/app/reports/research_report.json"


def get_engine():
    return create_engine(DATABASE_URL)


def run_research():
    print("Починаємо дослідження даних...")
    engine = get_engine()

    try:
        df = pd.read_sql_table('sports_data', engine)

        cols_to_numeric = ['number', 'sex1', 'sex2', 'invalidity']
        for col in cols_to_numeric:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        stats = {
            "total_records": len(df),
            "total_athletes": int(df['number'].sum()),
            "total_men": int(df['sex1'].sum()),
            "total_women": int(df['sex2'].sum()),
            "by_title": df.groupby('title')['number'].sum().to_dict()
        }

        with open(REPORT_PATH, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=4, ensure_ascii=False)

        print(f"Дослідження завершено. Результати збережено у: {REPORT_PATH}")

    except Exception as e:
        print(f"Виникла помилка під час дослідження: {e}")


if __name__ == "__main__":
    run_research()