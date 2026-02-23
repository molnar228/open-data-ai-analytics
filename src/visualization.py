import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")

file_path = os.path.join("..", "data", "raw", "master-treiner-2023.csv")
output_dir = os.path.join("reports", "figures")
os.makedirs(output_dir, exist_ok=True)

if os.path.exists(file_path):
    df = pd.read_csv(file_path, sep=';', na_values="null")
    df[['sex1', 'sex2', 'number']] = df[['sex1', 'sex2', 'number']].fillna(0)

    plt.figure(figsize=(12, 6))
    monthly_data = df.groupby('period2')['number'].sum().reset_index()
    sns.barplot(data=monthly_data, x='period2', y='number', palette="viridis")
    plt.title('Кількість присвоєних спортивних звань за місяцями (2023)')
    plt.xlabel('Місяць')
    plt.ylabel('Кількість звань')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "monthly_dynamics.png"))
    print("Графік динаміки збережено!")

    plt.figure(figsize=(8, 8))
    total_m = df['sex1'].sum()
    total_f = df['sex2'].sum()
    plt.pie([total_m, total_f], labels=['Чоловіки', 'Жінки'], autopct='%1.1f%%', colors=['#3498db', '#e74c3c'])
    plt.title('Гендерний розподіл спортивних звань (2023)')
    plt.savefig(os.path.join(output_dir, "gender_distribution.png"))
    print("Графік гендерного розподілу збережено!")

else:
    print("Файл даних не знайдено!")