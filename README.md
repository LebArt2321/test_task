Это веб-приложение предназначено для определения заполненных форм. Оно анализирует данные формы, переданные через POST запрос, и возвращает имя соответствующего шаблона формы.

## Начало работы

Эти инструкции помогут вам запустить копию проекта на вашей локальной машине для разработки и тестирования.

### Предварительные требования

Для запуска этого проекта вам понадобится Python и pip. Вы также можете использовать virtualenv для создания изолированной среды Python.

```bash
python3 -m venv venv
source venv/bin/activate # Для Unix или MacOS
venv\Scripts\activate    # Для Windows
```

### Установка

Чтобы установить и запустить проект, выполните следующие шаги:

```bash
git clone https://github.com/LebArt2321/test_task
pip install -r requirements.txt
```

### Использование
Для запуска сервера разработки выполните:

```bash
uvicorn main:app --reload
```

Вы можете получить доступ к документации API и интерактивному интерфейсу Swagger UI по адресу:

http://127.0.0.1:8000/docs

### Тестирование
Для запуска тестов используйте следующую команду:

```bash
pytest
```
