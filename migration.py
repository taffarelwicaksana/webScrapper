import mysql.connector
from mysql.connector import Error

def migrate_data(data_list):
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'simamft_try',
        'raise_on_warnings': True
    }
    
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO siswa (
                nama, NIM, no_hp, nama_orangtua, prodi_id, fakultas_id, dosbing_id, user_id,
                semester_berjalan, angkatan, nilai_s6, sks_s7
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            """

            for item in data_list:
                # Jika angkatan 2021, semester berjalan menjadi 'Semester 7'
                semester_berjalan = 'Semester 7' if item['angkatan'] == '2021' else '-'

                values = (
                    item['nama'], item['NIM'], item['no_hp'], item['nama_orangtua'],
                    item['prodi_id'], item['fakultas_id'],
                    item['dosbing_id'], item['user_id'],
                    semester_berjalan, item['angkatan'],
                    item['nilai_s6'], item['sks_s7']
                )
                cursor.execute(insert_query, values)

            connection.commit()
            print("Data berhasil dimigrasi ke database.")
    
    except Error as e:
        print(f"Error saat menghubungkan ke MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
