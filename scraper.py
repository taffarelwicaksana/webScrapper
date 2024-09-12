from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def scrape_data(source_path):
    service = Service('D:/Downloads/TA/Data/scrapper/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(source_path)
    data = []

    time.sleep(2)  
    user_id_start = 14

    try:
        rows = driver.find_elements(By.XPATH, '//table/tbody/tr')
        print(f"Jumlah baris ditemukan: {len(rows)}")  
        
        for i, row in enumerate(rows[1:], start=user_id_start):  
            if i > user_id_start + 23:  
                break
            nama = row.find_element(By.XPATH, './td[3]').text
            nim = row.find_element(By.XPATH, './td[4]').text
            prodi = row.find_element(By.XPATH, './td[5]').text
            angkatan = row.find_element(By.XPATH, './td[6]').text
            ip = row.find_element(By.XPATH, './td[8]').text
            sks = row.find_element(By.XPATH, './td[9]').text

            try:
                no_hp = row.find_element(By.XPATH, './td[10]').text
                no_hp = no_hp if no_hp.strip() else '-'
            except:
                no_hp = '-'

            try:
                nama_orangtua = row.find_element(By.XPATH, './td[11]').text
                nama_orangtua = nama_orangtua if nama_orangtua.strip() else '-'
            except:
                nama_orangtua = '-'

            if prodi == "Teknik Elektro S1":
                prodi_id = 2
                fakultas_id = 1
            else:
                prodi_id = None
                fakultas_id = None

            data.append({
                'nama': nama,
                'NIM': nim,
                'no_hp': no_hp,
                'nama_orangtua': nama_orangtua,
                'prodi_id': prodi_id,
                'fakultas_id': fakultas_id,
                'angkatan': angkatan,
                'nilai_s6': float(ip),
                'sks_s7': int(sks),
                'dosbing_id': 8,
                'user_id': i
            })
    
    except Exception as e:
        print(f"Terjadi kesalahan saat scraping: {e}")
    finally:
        driver.quit()

    return data
