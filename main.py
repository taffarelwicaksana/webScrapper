import scraper
import migration
import time

def main():
    # Path ke file 
    source_path = "file:///D:/Downloads/TA/Data/data/INDEX%20_%20ADMIN.htm"
    
    print(f"Memulai proses scraping dari {source_path}")
    start_time = time.time()

    data_list = scraper.scrape_data(source_path)
    
    if data_list:
        print(f"Scraping selesai, berhasil mengambil {len(data_list)} data.")
        # Migrasi data ke database
        print("Memulai proses migrasi data ke database.")
        migration.migrate_data(data_list)
    else:
        print("Tidak ada data yang diambil dari proses scraping.")

    end_time = time.time()
    print(f"Proses selesai dalam {end_time - start_time:.2f} detik.")

if __name__ == "__main__":
    main()
