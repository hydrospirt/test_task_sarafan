# Тестовое задание для стажировки Сарафан

Это мой проект, и вот информация об авторе:

<div style="display: flex; align-items: center;">
  <img src="https://avatars.githubusercontent.com/u/43341579?s=400&u=23abef0a296e52a8bf1dc29fd6c8c50b4f3feda4&v=4" alt="Ваше Имя" width="100" style="border-radius: 50%; margin-right: 20px;">
  <div>
    <h3>Эдуард Гумен</h3>
    <p>Ссылка на мой профиль GitHub:</p>
    <p><a href="https://github.com/hydrospirt">GitHub Profile</a></p>
  </div>
</div>

<h2>Оглавление</h2>
    <ul>
        <li><a href="#task1">1. Тестовое задание Sequence Generator</a></li>
        <li><a href="#task2">2. Тестовое задание Simple API Shop</a></li>
    </ul>

## Структура

```
├──.gitignore                 # Файл исключений для Git
├──LICENSE                    # Файл Лицензии
├──README.md                  # Файл с инструкциями о проекте
├──assets/                    # Изображения для README.md
├──get_structure.py           # Скрипт для получения структуры проекта
├──setup.bat                  # Скрипт для Windows [для подготовки проекта]
├──setup.cfg                  # Настройки для проектаб например flake8
├──test_task_1/               # Основная директория первого тестового задания
│   ├──EXP.md                 # Описание задачи с чек боксом первого тестового задания
│   ├──main.py                # Основной файл программы
│   ├──requrements.txt        # Текстовый файл с зависимостями
├──test_task_2/               # Основная директория второго тестового задания
│   ├──EXP.md                 # Описание задачи с чек боксом второго тестового задания
│   ├──requirements.txt       # Текстовый файл с зависимостями
│   ├──simple_shop/           # Основная директория проекта Django
│   │   ├──api/               # Директория приложения API
│   │   │   ├──__init__.py    # Файл пакета
│   │   │   ├──apps.py        # Содержит конфигурацию приложения
│   │   │   ├──pagination.py  # Содержит кастомную пагинацию приложения
│   │   │   ├──serializers.py # Содержит сериализаторы приложения
│   │   │   ├──service.py     # Содержит бизнес логику приложения
│   │   │   ├──urls.py        # Содержит URL-шаблоны приложения
│   │   │   ├──utils.py       # Содержит вспомогательные функции приложения
│   │   │   ├──views.py       # Определяет представления приложения
│   │   ├──db.sqlite3         # Файл базы данных, для разработки проекта
│   │   ├──manage.py          # Инструмент для управления проектом Django, для выполнения команд
│   │   ├──media/             # Директория с медиа файлами проекта
│   │   │   ├──category/      # Директория с медиа модели категории
│   │   │   │   ├──2024-08-21/ # Директория с медиа модели категории по датам
│   │   │   ├──product/       # Директория с медиа модели продукта
│   │   │   │   ├──2024-08-21/ # Директория с медиа модели продукта по датам
│   │   │   ├──subcategory/   # Директория с медиа модели подкатегории
│   │   │   │   ├──2024-08-21/ # Директория с медиа модели подкатегории по датам
│   │   ├──products/          # Директория приложения Продуктов
│   │   │   ├──__init__.py    # Файл пакета
│   │   │   ├──admin.py       # Регистрирует модели Продуктов в административной панели
│   │   │   ├──apps.py        # Содержит конфигурацию приложения
│   │   │   ├──models.py      # Определяет модели данных приложения
│   │   │   ├──views.py       # Определяет представления приложения
│   │   ├──simple_shop/       # Файл пакета
│   │   │   ├──__init__.py    # Файл пакета
│   │   │   ├──asgi.py        # Настройка ASGI-сервера
│   │   │   ├──settings.py    # Основные настройки проекта
│   │   │   ├──urls.py        # Маршрутизация URL
│   │   │   ├──wsgi.py        # Настройка WSGI-сервера
│   │   ├──users/             # Директория приложения Пользователи
│   │   │   ├──__init__.py    # Файл пакета
│   │   │   ├──admin.py       # Регистрирует модели Пользователей в административной панели
│   │   │   ├──apps.py        # Содержит конфигурацию приложения
│   │   │   ├──models.py      # Определяет модели данных приложения
│   │   │   ├──views.py       # Определяет представления приложения

```

<h1 id="task1">1. Тестовое задание Sequence Generator</h1>

<p>
  <img src="https://github.com/hydrospirt/test_task_sarafan/blob/master/assets/test1.png" alt="Sequence Generator" width=50%>
</p>

- [Cсылка на тестовое задание 1](https://github.com/hydrospirt/test_task_sarafan/blob/master/test_task_1/EXP.md)

Это простой прототип на Python, который генерирует последовательность чисел на основе введенного пользователем целого положительного числа. Последовательность генерируется путем многократного добавления текущего числа i к последовательности i раз, пока длина последовательности не достигнет введенного пользователем значения.

## Установка:

1. **Клонируйте репозиторий:**
   ```bash
   git clone git@github.com:hydrospirt/test_task_sarafan.git
   cd test_task_sarafan
   ```

2. **Создайте виртуальное окружение и активируйте его:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
   ```

3. **Установите необходимые зависимости:**
   ```bash
   pip install -r test_task_1/requirements.txt
   ```

4. **Запусти CLI программу:**
   ```bash
   python test_task_1/main.py
   ```

3. При появлении запроса введите положительное целое число.

## Обзор кода

Скрипт состоит из следующих компонентов:

- `VERSION`: строковая константа, представляющая текущую версию скрипта.
- `TIME`: объект datetime, представляющий текущее время запуска скрипта..
- `sequence_generator`: Функция-генератор, которая принимает положительное целое число `sequence_length` в качестве входных данных и выдает строковое представление последовательности..
- `__main__`: Точка входа в скрипт, которая отображает логотип, версию и время и запрашивает у пользователя ввод данных. Ввод проверяется, чтобы убедиться, что это положительное целое число, и функция `sequence_generator` вызывается с использованием ввода в качестве аргумента. Результирующая последовательность выводится на консоль.

## Зависимости

- `art`: Библиотека Python для генерации текста в формате ASCII art.


<h1 id="task2">2. Тестовое задание Simple API Shop</h1>

<p>
  <img src="https://github.com/hydrospirt/test_task_sarafan/blob/master/assets/test_task2_swagger.png" alt="Admin Panel" width=50%>
</p>
<p>
  <img src="https://github.com/hydrospirt/test_task_sarafan/blob/master/assets/test2_admin_panel.png" alt="Admin Panel" width=50%>
</p>

- [Ссылка на тестовое задание 2](https://github.com/hydrospirt/test_task_sarafan/blob/master/test_task_2/EXP.md)

Это RESTful API для простого интернет-магазина, созданный с использованием Django и платформы Django Rest Framework. API позволяет клиентам просматривать и приобретать товары, просматривать свою корзину и управлять ею.

## Функционал

- **Управление категориями и подкатегориями:**
  - Создание, редактирование и удаление категорий и подкатегорий через админку.
  - Категории и подкатегории имеют наименование, slug-имя и изображение.
  - Подкатегории связаны с родительской категорией.
  - Эндпоинт для просмотра всех категорий с подкатегориями с пагинацией.

- **Управление продуктами:**
  - Добавление, изменение и удаление продуктов через админку.
  - Продукты относятся к определенной подкатегории и категории, имеют наименование, slug-имя, изображение в 3-х размерах и цену.
  - Эндпоинт для вывода продуктов с пагинацией, включая поля: наименование, slug, категория, подкатегория, цена, список изображений.

- **Управление корзиной:**
  - Эндпоинты для добавления, изменения (изменение количества) и удаления продукта в корзине.
  - Эндпоинт для вывода состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
  - Возможность полной очистки корзины.

- **Безопасность:**
  - Операции по эндпоинтам категорий и продуктов доступны любому пользователю.
  - Операции по эндпоинтам корзины доступны только авторизованным пользователям со своей корзиной.
  - Авторизация по токену.

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone git@github.com:hydrospirt/test_task_sarafan.git
   cd test_task_sarafan
   ```

2. **Создайте виртуальное окружение и активируйте его:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r test_task_2/requirements.txt
   ```

4. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```

5. **Создайте суперпользователя:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```
7. **Перейдите по ссылкам:**
   ```bash
   http://127.0.0.1:8000/admin/ # Административная панель
   http://127.0.0.1:8000/swagger/ # Автодокументация Swagger
   ```

## API Endpoints

### Категории

- **GET /api/categories/** - Получить список всех категорий с подкатегориями (с пагинацией).

### Продукты

- **GET /api/products/** - Получить список всех продуктов (с пагинацией).

### Корзина

- **POST /api/cart/** - Добавить продукт в корзину.
- **PUT /api/cart/** - Изменить количество продукта в корзине.
- **DELETE /api/cart/** - Удалить продукт из корзины.
- **GET /api/cart/** - Просмотреть состав корзины с подсчетом количества и суммы стоимости товаров.
- **DELETE /api/cart/clear/** - Очистить корзину.

## Авторизация

Для операций с корзиной требуется авторизация по токену. Получите токен через эндпоинт `/api/token/` и используйте его в заголовках запросов:

```http
Authorization: Bearer your_token_here
```

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).


