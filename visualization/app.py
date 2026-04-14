import os
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/lab_db")
PLOT_DIR = "/app/plots"


def get_engine():
    return create_engine(DATABASE_URL)


def create_visualizations():
    print("Починаємо генерацію візуалізацій...")
    engine = get_engine()

    try:
        df = pd.read_sql_table('sports_data', engine)

        for col in ['number', 'sex1', 'sex2']:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        sns.set_theme(style="whitegrid")

        plt.figure(figsize=(8, 6))
        total_men = df['sex1'].sum()
        total_women = df['sex2'].sum()

        plt.pie([total_men, total_women], labels=['Чоловіки', 'Жінки'],
                autopct='%1.1f%%', colors=['#4C72B0', '#C44E52'])
        plt.title('Розподіл спортсменів за статтю')
        plt.savefig(f"{PLOT_DIR}/gender_distribution.png", bbox_inches='tight')
        plt.close()
        print("Збережено графік: gender_distribution.png")

        plt.figure(figsize=(10, 6))
        title_counts = df.groupby('title')['number'].sum().sort_values(ascending=False)

        sns.barplot(x=title_counts.values, y=title_counts.index, palette="viridis")
        plt.title('Кількість спортсменів за званнями')
        plt.xlabel('Кількість')
        plt.ylabel('Звання')
        plt.tight_layout()
        plt.savefig(f"{PLOT_DIR}/titles_distribution.png", bbox_inches='tight')
        plt.close()
        print("Збережено графік: titles_distribution.png")

        print("Всі візуалізації успішно згенеровано!")

    except Exception as e:
        print(f"Виникла помилка при візуалізації: {e}")


if __name__ == "__main__":
    create_visualizations()