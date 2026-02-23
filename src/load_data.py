import pandas as pd

def load_data():
    path = "../data/raw/master-treiner-2023.csv"
    try:
        df = pd.read_csv(path)
        print("Дані успішно завантажено!")
        print(df.head())
        return df
    except FileNotFoundError:
        print("Файл не знайдено. Перевір шлях data/raw/")

if __name__ == "__main__":
    load_data()
