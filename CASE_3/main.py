import sqlite3

con = sqlite3.connect("Туризм.db")
cursor = con.cursor()

# создаем таблицу people
cursor.execute("""-- Таблица для услуг (Services)
CREATE TABLE Services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- уникальный идентификатор услуги
    service_name TEXT NOT NULL,  -- название услуги
    description TEXT            -- описание услуги
);
""")

cursor.execute("""
-- Таблица для направлений туров (Destinations)
CREATE TABLE Destinations (
    destination_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- уникальный идентификатор направления
    destination_name TEXT NOT NULL,  -- название направления (страна, город)
    description TEXT                -- описание направления
);
""")

cursor.execute("""
-- Таблица для туристов (Tourists)
CREATE TABLE Tourists (
    tourist_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- уникальный идентификатор туриста
    first_name TEXT NOT NULL,  -- имя
    last_name TEXT NOT NULL,   -- фамилия
    email TEXT,                -- электронная почта
    phone TEXT                 -- номер телефона
);
""")

cursor.execute("""
-- Таблица для заказов (Bookings)
CREATE TABLE Bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- уникальный идентификатор заказа
    tourist_id INTEGER NOT NULL,                    -- внешний ключ на туриста
    destination_id INTEGER NOT NULL,                -- внешний ключ на направление
    booking_date TEXT NOT NULL,                     -- дата бронирования
    service_id INTEGER NOT NULL,                    -- внешний ключ на услугу
    amount INTEGER NOT NULL,                        -- количество туристов
    FOREIGN KEY (tourist_id) REFERENCES Tourists(tourist_id),  -- связь с таблицей туристов
    FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id),  -- связь с таблицей направлений
    FOREIGN KEY (service_id) REFERENCES Services(service_id)  -- связь с таблицей услуг
);

""")
