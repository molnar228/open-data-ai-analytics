import pandas as pd
import os

file_path = os.path.join("..", "data", "raw", "master-treiner-2023.csv")

if os.path.exists(file_path):
    df = pd.read_csv(file_path, sep=';', na_values="null")

    print("--- 1. Гендерний розподіл (Гіпотеза 1) ---")
    total_sex1 = df['sex1'].fillna(0).sum()
    total_sex2 = df['sex2'].fillna(0).sum()
    print(f"Чоловіки: {int(total_sex1)}, Жінки: {int(total_sex2)}")

    print("\n--- 2. Статистика інклюзивності (Гіпотеза 3) ---")
    total_awards = df['number'].fillna(0).sum()
    total_invalidity = df['invalidity'].fillna(0).sum()
    percent_inv = (total_invalidity / total_awards) * 100 if total_awards > 0 else 0
    print(f"Відсоток звань для осіб з інвалідністю: {percent_inv:.2f}%")

    print("\n--- 3. Топ-3 місяці за кількістю нагород ---")
    monthly_stats = df.groupby('period2')['number'].sum().sort_values(ascending=False)
    print(monthly_stats.head(3))