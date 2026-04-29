Ось оновлений та професійний **README.md** для твого репозиторію. Він структурований так, щоб викладач одразу бачив обсяг виконаної роботи та твої навички автоматизації.

---

# Open Data AI Analytics: Azure Cloud Deployment

Цей проєкт присвячений створенню автоматизованої системи аналізу відкритих даних з використанням контейнеризації та хмарної інфраструктури в **Microsoft Azure**. 

Основна мета роботи — реалізація підходу **Infrastructure as Code (IaC)** для розгортання повного циклу обробки даних (ETL, аналіз, візуалізація) без ручного налаштування сервера.

## Технологічний стек
* **IaC:** Terraform
* **Оркестрація:** Docker Compose
* **Хмара:** Microsoft Azure (Virtual Machines, Networking, Cloud Shell)
* **Автоматизація:** cloud-init
* **Аналіз:** Python (Pandas, PySpark), PostgreSQL
* **Візуалізація:** Flask/Python Web-сервіс

## Структура проєкту
```text
open-data-ai-analytics/
├── data/                 # Сирі дані (локально)
├── data_load/            # Модуль завантаження даних у БД
├── data_quality_analysis/ # Модуль перевірки якості
├── data_research/        # Модуль статистичного аналізу
├── visualization/        # Модуль генерації графіків
├── web/                  # Веб-інтерфейс (порт 5000)
├── infra/
│   └── terraform/        # Конфігурація інфраструктури (IaC)
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── cloud-init.yaml
└── compose.yaml          # Конфігурація Docker-контейнерів
```

## Розгортання (Deployment)

### 1. Підготовка в Azure
1. Увійдіть у [Azure Portal](https://portal.azure.com/).
2. Відкрийте **Azure Cloud Shell** (Bash).
3. Склонуйте репозиторій:
   ```bash
   git clone https://github.com/molnar228/open-data-ai-analytics.git
   cd open-data-ai-analytics/infra/terraform
   ```

### 2. Запуск інфраструктури (Terraform)
Виконайте команди для створення ресурсів:
```bash
terraform init
terraform apply -auto-approve
```
Після завершення Terraform виведе `public_ip` вашого сервера.

### 3. Налаштування середовища (Troubleshooting)
Оскільки файли секретів (`.env`) не зберігаються в репозиторії, їх потрібно створити на сервері вручну:
1. Підключіться до VM: `ssh azureuser@<public_ip>` (пароль: `Password12345!`).
2. Перейдіть у папку проєкту: `cd ~/app`.
3. Налаштуйте права доступу: `sudo chown -R azureuser:azureuser ~/app`.
4. Створіть файл `.env`:
   ```bash
   cat <<EOF > .env
   POSTGRES_USER=myuser
   POSTGRES_PASSWORD=mypassword123
   POSTGRES_DB=mydb
   DATABASE_URL=postgresql://myuser:mypassword123@db:5432/mydb
   EOF
   ```
5. Перезапустіть систему: `docker compose down && docker compose up -d`.

## Перевірка результатів
Після завершення роботи всіх модулів (статус `Exited 0` для аналітичних контейнерів), веб-інтерфейс буде доступний за адресою:
**`http://<your_public_ip>:5000`**

## Видалення ресурсів
Щоб уникнути зайвих витрат студентських кредитів, видаліть інфраструктуру після демонстрації:
```bash
terraform destroy -auto-approve
```

---

### Особливості реалізації:
1.  **Автоматизація:** Використано `cloud-init` для автоматичного встановлення Docker, Docker Compose та клонування проєкту під час ініціалізації VM.
2.  **Гнучкість:** Налаштовано динамічне керування регіонами та типами віртуальних машин через `variables.tf`.
3.  **Безпека:** Реалізовано Network Security Group (NSG) з обмеженням доступу лише за необхідними портами (22, 5000).