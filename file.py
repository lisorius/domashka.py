import sqlite3

# Устанавливаем соединение с базой данных
db = sqlite3.connect('server.db')

# Создаем объект-курсор для выполнения SQL-запросов
sql = db.cursor()

# Создаем таблицы, если их еще нет
sql.execute('''CREATE TABLE IF NOT EXISTS tab_text_1 (value TEXT)''')
sql.execute('''CREATE TABLE IF NOT EXISTS tab_chislo_2 (value INTEGER)''')

# Создаем список со строками и числами
b = ['яблоко', 12, 'кокос', 83, 'человек', 32]

# Перебираем элементы списка
for i in b:
    # Если элемент является строкой, добавляем его в таблицу tab_text_1
    if type(i) == str:
        sql.execute('''INSERT INTO tab_text_1 (value) VALUES (?)''', (i,))
        db.commit()
        # Вычисляем длину строки и добавляем ее в таблицу tab_chislo_2
        a = len(i)
        sql.execute('''INSERT INTO tab_chislo_2 (value) VALUES (?)''', (a,))
        db.commit()
    # Если элемент является чётным числом, добавляем его в таблицу tab_chislo_2
    elif type(i) == int and i % 2 == 0:
        sql.execute('''INSERT INTO tab_chislo_2 (value) VALUES (?)''', (i,))
        db.commit()
        # иначе добавить его в таблицу tab_chislo_2, слово нечётное.
    else:
        sql.execute('''INSERT INTO tab_chislo_2 (value) VALUES (?)''', ("нечётное",))
        db.commit()


# Закрываем курсор и соединение с базой данных
sql.close()
db.close()
