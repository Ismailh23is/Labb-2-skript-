import modules


def main():

    while True:
        print('-------------Labb 2--------------')
        print('Välj ett av alternativen nedan')
        print('1. Läs in csv-fil till json-fil')
        print('2. Visa json-fil')
        print('3. Lägg till kursmedlem')
        print('4. Ta bort kursmedlem')
        print('5. Spara json-fil till csv-fil')
        print('6. Avsluta Programmet')
        print('---------------------------------')

        print("Välj mellan 1-6 från menyn")
        menyval = input()
        if menyval == "1":
            modules.las_in_csv_till_json()
        elif menyval == "2":
            modules.visa_json_fil()
        elif menyval == "3":
            modules.lagg_till_kursmedlem()
        elif menyval == "4":
            modules.ta_bort_kursmedlem()
        elif menyval == "5":
            modules.spara_json_fil_till_csv_fil()
        elif menyval == "6":
            modules.avsluta_programmet()
            break
        else:
            print("Ogiltigt val, vänligen välj en siffra mellan 1-6")

if __name__ == "__main__":
    main()
