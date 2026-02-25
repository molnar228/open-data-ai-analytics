# REPORT.md: Аналіз відкритих даних спортивних звань України (2023)
1. Вступ
Дана лабораторна робота присвячена аналізу відкритих даних Міністерства молоді та спорту України за 2023 рік. Об'єктом дослідження є статистика осіб, яким було присвоєно спортивні звання (Майстер спорту, Заслужений майстер спорту тощо).

2. Хід роботи
Проєкт було реалізовано з дотриманням стандартів розробки та контролю версій:

Структурування: Створено чітку ієрархію папок (src/, data/raw/, reports/figures/) для відокремлення коду від даних та звітів.

Контроль версій: Кожен етап (завантаження, аналіз, візуалізація) виконувався в окремих feature-гілках.

Обробка даних: Написано Python-скрипти з використанням бібліотеки pandas для очищення даних (обробка null значень) та коректного парсингу CSV-файлів.

Документування: Ведення CHANGELOG.md та створення тегу версії v0.1.0.

3. Результати дослідження
В ході аналізу було перевірено три ключові гіпотези:

Гендерний розподіл: Аналіз показав, що кількість чоловіків (sex1), які отримали звання, переважає кількість жінок (sex2). Це підтверджує гіпотезу про вищу представленість чоловіків у професійному спорті вищих досягнень у 2023 році.

Сезонна динаміка: Було виявлено пікові періоди присвоєння звань. Найбільша кількість нагороджень припадає на кінці кварталів, що може бути пов'язано з графіком проведення змагань та бюрократичними циклами звітності.

Інклюзивність: Було розраховано відсоток звань, присвоєних особам з інвалідністю. Дані свідчать про стабільну підтримку інклюзивного спорту в Україні.

4. Вирішення merge-конфлікту
У межах роботи було штучно створено та успішно розв'язано конфлікт у файлі README.md.

Причина: Дві гілки (conflict-a та conflict-b) одночасно змінили опис гіпотез в одній секції.

Рішення: Конфлікт було розв'язано вручну шляхом поєднання обох версій тексту, видалення маркерів Git (<<<<<<<, =======) та фіксації фінального стану через git commit.

5. Висновки
Робота дозволила опанувати навички роботи з Git у складних сценаріях (конфлікти, теги) та навчитися працювати з "сирими" державними відкритими даними. Отримані результати візуалізовано та збережено у папку reports/figures/.

6. Git Log Graph
```   * dcdc6c4 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) chore: add CHANGELOG.md for version 0.1.0
* 1fe09c9 (feature/visualization) feat: complete visualization with script and charts
* bc8fad1 visual: add generated charts for gender and monthly stats
*   8bf2be7 Merge remote-tracking branch 'origin/main'
|\  
| *   b9bd1ef Merge pull request #2 from molnar228/feature/data_research
:...skipping...
* dcdc6c4 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) chore: add CHANGELOG.md for version 0.1.0
* 1fe09c9 (feature/visualization) feat: complete visualization with script and charts
* bc8fad1 visual: add generated charts for gender and monthly stats
*   8bf2be7 Merge remote-tracking branch 'origin/main'
|\  
| *   b9bd1ef Merge pull request #2 from molnar228/feature/data_research
| |\  
| | * b1d265a (origin/feature/data_research, feature/data_research) Add data research script for hypothesis testing
| * |   0eda2f0 Merge pull request #1 from molnar228/feature/data_quality_analysis
| |\ \  
| | |/  
| |/|   
| | * 90bcf07 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Add data quality analysis script
| |/  
* |   a77957b Fix: resolve merge conflict in README by combining hypotheses
|\ \  
| * | f12c490 (conflict-b) Change hypothesis to version B
| |/  
* / eff49ad (conflict-a) Change hypothesis to version A
|/  
* 62d3f0d Data: add raw dataset file
* 149daff (origin/feature/data_load, feature/data_load) Feat: add script for loading sports awards data
* 7c8f63f Update README.md
* 5bd7cdf Update .gitignore
* 899a01b Create .gitignore
* ca832bf Create .gitignore
* a32ef51 Create .gitignore
* a513d29 Create README.md
* 7e71c2e Create .gitignore
* 3dcaa76 Initial commit
~
~
~
~
~
~
(END)
* dcdc6c4 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) chore: add CHANGELOG.md for version 0.1.0
* 1fe09c9 (feature/visualization) feat: complete visualization with script and charts
* bc8fad1 visual: add generated charts for gender and monthly stats
*   8bf2be7 Merge remote-tracking branch 'origin/main'
|\  
| *   b9bd1ef Merge pull request #2 from molnar228/feature/data_research
| |\  
| | * b1d265a (origin/feature/data_research, feature/data_research) Add data research script for hypothesis testing
| * |   0eda2f0 Merge pull request #1 from molnar228/feature/data_quality_analysis
| |\ \  
| | |/  
| |/|   
| | * 90bcf07 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Add data quality analysis script
:...skipping...
* dcdc6c4 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) chore: add CHANGELOG.md for version 0.1.0
* 1fe09c9 (feature/visualization) feat: complete visualization with script and charts
* bc8fad1 visual: add generated charts for gender and monthly stats
*   8bf2be7 Merge remote-tracking branch 'origin/main'
|\  
| *   b9bd1ef Merge pull request #2 from molnar228/feature/data_research
| |\  
| | * b1d265a (origin/feature/data_research, feature/data_research) Add data research script for hypothesis testing
| * |   0eda2f0 Merge pull request #1 from molnar228/feature/data_quality_analysis
| |\ \  
| | |/  
| |/|   
| | * 90bcf07 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Add data quality analysis script
| |/  
* |   a77957b Fix: resolve merge conflict in README by combining hypotheses
|\ \  
| * | f12c490 (conflict-b) Change hypothesis to version B
| |/  
* / eff49ad (conflict-a) Change hypothesis to version A
|/  
* 62d3f0d Data: add raw dataset file
* 149daff (origin/feature/data_load, feature/data_load) Feat: add script for loading sports awards data
* 7c8f63f Update README.md
* 5bd7cdf Update .gitignore
* 899a01b Create .gitignore
* ca832bf Create .gitignore
* a32ef51 Create .gitignore
* a513d29 Create README.md
* 7e71c2e Create .gitignore
* 3dcaa76 Initial commit
```
