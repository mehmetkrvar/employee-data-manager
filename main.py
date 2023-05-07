import csv
import os

def get_employee_data():
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    departman = input("Departman: ")
    telefon_numarasi = input("Telefon numarası: ")
    sirket_id = input("Şirket ID'si: ")
    gorev = input("Görev: ")
    adres = input("Adres: ")

    return [isim, soyisim, departman, telefon_numarasi, sirket_id, gorev, adres]

def write_to_csv(employee_data, file_name='data.csv'):
    file_exists = os.path.isfile(file_name)

    with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['isim', 'soyisim', 'departman', 'telefon_numarasi', 'sirket_id', 'gorev', 'adres']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'isim': employee_data[0],
            'soyisim': employee_data[1],
            'departman': employee_data[2],
            'telefon_numarasi': employee_data[3],
            'sirket_id': employee_data[4],
            'gorev': employee_data[5],
            'adres': employee_data[6]
        })

def search_employee(isim, soyisim, file_name='data.csv'):
    with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        employee_found = False
        for row in reader:
            if row['isim'] == isim and row['soyisim'] == soyisim:
                print("Çalışan bilgileri:")
                print("İsim: ", row['isim'])
                print("Soyisim: ", row['soyisim'])
                print("Departman: ", row['departman'])
                print("Telefon numarası: ", row['telefon_numarasi'])
                print("Şirket ID'si: ", row['sirket_id'])
                print("Görev: ", row['gorev'])
                print("Adres: ", row['adres'])
                employee_found = True
                break

        if not employee_found:
            print("Bu isim ve soyisimle eşleşen bir çalışan bulunamadı.")

def main_menu():
    while True:
        print("\nLütfen yapmak istediğiniz işlemi seçin:")
        print("1. Veri Girişi")
        print("2. Çalışanı Sorgula")
        print("3. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == '1':
            employee_data = get_employee_data()
            write_to_csv(employee_data)
        elif choice == '2':
            isim = input("İsim: ")
            soyisim = input("Soyisim: ")
            search_employee(isim, soyisim)
        elif choice == '3':
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == '__main__':
    main_menu()
