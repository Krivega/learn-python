# Изучение python

## Настройка окружения

Для начала нужно установить пакетный менеджер **uv**
[https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

## Установка зависимостей

- `uv sync`
- `uv pip install --editable .`

## Запуск скриптов

`uv run ПУТЬ_К_СКРИПТУ`

### Примеры

- `uv run src/loopsAndConditions/task1/run.py`
- `uv run src/function1/task4/run.py`

## Запуск тестов

- `uv run pytest`
