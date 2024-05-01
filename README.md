## Установка и запуск

1. **Скачать репозиторий:**
```bash
git clone https://github.com/atomsis/CPU_loader.git
```
2 **Запустить 
2  **Установить зависимости:**
```python
pip install -r requirements.txt
```
3 **Выполнить миграции Django:**
```bash
python manage.py migrate
```
3. Запустить сервер:
```python
python manage.py runserver 127.0.0.1:8001
```
-----------------------------------------------------------
◾ **Запуск клиент-демона**<br>
**Для запуска клиент-демона, который будет отправлять данные о нагрузке процессора на сервер каждые 10 секунд, выполните следующие шаги:**<br>

**Запустить баш скрипт:**
```
 bash client_daemon.sh
```
----------------------------------------------------------------
Добавленные функциональности:
Страница / для пользователя содержит:
  🟢 -  Таблицу с 100 последними записями.
  🟢 - Таблицу с возможностью сортировки (реализовано с помощью JavaScript).
  🟢 - Агрегированные данные (реализовано с помощью JavaScript):
    🟢 - min/max/avg 100 последних записей. Записи обновляются раз в 10 секунд.
    🟢 - min/max/avg всех записей в БД. Записи обновляются раз в 10 секунд.
🟢Для оформления страницы использованы стили. Данные обновляются динамически без перезагрузки страницы с использованием AJAX.
