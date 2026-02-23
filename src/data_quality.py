import pandas as pd
import os

file_path = os.path.join("..","data", "raw", "master-treiner-2023.csv")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    print("--- Перевірка пропущених значень ---")
    print(df.isnull().sum())

    print("\n--- Типи даних ---")
    print(df.dtypes)

    print(f"\n--- Дублікати: {df.duplicated().sum()} ---")
else:
    print(f"Помилка: Файл за шляхом {file_path} не знайдено!")