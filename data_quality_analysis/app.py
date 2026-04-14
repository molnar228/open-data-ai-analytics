import os
import time
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import json

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/lab_db")
REPORT_PATH = "/app/reports/quality_report.json"


def get_engine():
    engine = create_engine(DATABASE_URL)
    for i in range(10):
        try:
            with engine.connect() as conn:
                return engine
        except OperationalError:
            time.sleep(3)
    raise Exception("Не вдалося підключитися до БД.")


def analyze_quality():
    print("Починаємо перевірку якості даних...")
    engine = get_engine()

    try:
        df = pd.read_sql_table('sports_data', engine)
        print(f"Зчитано {len(df)} рядків з таблиці 'sports_data'.")

        report = {
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "duplicates": int(df.duplicated().sum()),
            "missing_values": df.isnull().sum().to_dict(),
            "data_types": df.dtypes.astype(str).to_dict()
        }

        with open(REPORT_PATH, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)

        print(f"Аналіз завершено. Звіт збережено у: {REPORT_PATH}")

    except ValueError:
        print("Помилка: Таблиця 'sports_data' не знайдена в базі. Спочатку запусти data_load.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


if __name__ == "__main__":
    analyze_quality()