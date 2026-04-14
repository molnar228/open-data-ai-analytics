import os
import time
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/lab_db")
DATA_PATH = "/app/data/raw/dataset.csv"


def get_engine():
    engine = create_engine(DATABASE_URL)
    for i in range(10):
        try:
            with engine.connect() as conn:
                print("Успішно підключено до бази даних!")
                return engine
        except OperationalError:
            print(f"База даних ще не готова, чекаємо... (спроба {i + 1}/10)")
            time.sleep(3)
    raise Exception("Не вдалося підключитися до бази даних.")


def load_data():
    print(f"Читаємо файл: {DATA_PATH}")
    try:
        df = pd.read_csv(DATA_PATH, sep=';')

        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        print(f"Прочитано {len(df)} рядків. Стовпці: {list(df.columns)}")

        engine = get_engine()

        df.to_sql('sports_data', engine, if_exists='replace', index=False)
        print("Дані успішно завантажено в таблицю 'sports_data'!")

    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {DATA_PATH}. Перевір налаштування volumes.")
    except Exception as e:
        print(f"Критична помилка: {e}")


if __name__ == "__main__":
    load_data()