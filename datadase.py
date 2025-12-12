import psycopg2

with psycopg2.connect(
        dbname="laba",
        user="postgres",
        password="0508",
        host="localhost",
        port="5432",
    ) as conn:
    conn.autocommit = True

    def db_select(table):
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table}")
            print(cur.fetchall())
                
    def db_create(data):
        with conn.cursor() as cur:
            try:
                cur.execute(f"""
                        INSERT INTO weather_data 
                        (temperature, city, cloudiness, humidity, pressure, wind_speed, wind_direction) 
                        VALUES (
                    {data['temp']}, 
                '{data['city_name']}', 
                '{data['clouds']}', 
                {data['rh']}, 
                {data['pres']}, 
                {data['wind_spd']}, 
                '{data['wind_cdir_full']}'
                                            )
                                                """)
                print("успешное сохранение в БД!!!")
            except Exception as e:
                print(e)
        
    def db_delete(city):
        with conn.cursor() as cur:
            cur.execute(f"""DELETE FROM weather_data WHERE city = '{city}'""")
            print(f"запись с {city} удалена")