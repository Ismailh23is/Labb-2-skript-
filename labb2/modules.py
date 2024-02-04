import json
import csv

def las_in_csv_till_json():
    csv_filnamn = 'studenter_labb2.csv'
    json_filnamn = 'studenter_labb2.json'

    student_lista = []

    with open(csv_filnamn, 'r', encoding='utf-8-sig') as csv_fil:
        csv_reader = csv.reader(csv_fil)
        header = next(csv_reader)  # Läs rubrikraden

        for rad in csv_reader:
            student_dict = {
                'efternamn': rad[0],
                'fornamn': rad[1],
                'anvandarnamn': rad[2]
            }
            student_lista.append(student_dict)

    with open(json_filnamn, 'w', encoding='utf-8') as json_fil:
        json.dump(student_lista, json_fil, ensure_ascii=False, indent=2)

    print(f'Data har lästs in från {csv_filnamn} och sparats ner till {json_filnamn}.')

def lagg_till_kursmedlem():
    json_filnamn = 'studenter_labb2.json'

    with open(json_filnamn, 'r', encoding='utf-8') as json_fil:
        student_lista = json.load(json_fil)

    ny_efternamn = input('Ange efternamn: ')
    ny_fornamn = input('Ange förnamn: ')
    ny_anvandarnamn = input('Ange användarnamn: ')

    ny_student = {
        'efternamn': ny_efternamn,
        'fornamn': ny_fornamn,
        'anvandarnamn': ny_anvandarnamn
    }

    student_lista.append(ny_student)

    with open(json_filnamn, 'w', encoding='utf-8') as json_fil:
        json.dump(student_lista, json_fil, ensure_ascii=False, indent=2)

    print(f'Ny kursmedlem har lagts till i {json_filnamn}.')

def ta_bort_kursmedlem():
    json_filnamn = 'studenter_labb2.json'

    with open(json_filnamn, 'r', encoding='utf-8') as json_fil:
        student_lista = json.load(json_fil)

    anvandarnamn_att_ta_bort = input('Ange användarnamnet för personen du vill ta bort: ')

    student_lista = [student for student in student_lista if student['anvandarnamn'] != anvandarnamn_att_ta_bort]

    with open(json_filnamn, 'w', encoding='utf-8') as json_fil:
        json.dump(student_lista, json_fil, ensure_ascii=False, indent=2)

    print(f'Kursmedlem med användarnamn {anvandarnamn_att_ta_bort} har tagits bort från {json_filnamn}.')

def visa_json_fil():
    json_filnamn = 'studenter_labb2.json'

    with open(json_filnamn, 'r', encoding='utf-8') as json_fil:
        data = json.load(json_fil)

    print('Data i .json-filen:')
    print(data)

def spara_json_fil_till_csv_fil():
    json_filnamn = 'studenter_labb2.json'
    csv_filnamn = 'studenter_labb2.csv'

    with open(json_filnamn, 'r', encoding='utf-8') as json_fil:
        data = json.load(json_fil)

    header = ['efternamn', 'fornamn', 'anvandarnamn']

    with open(csv_filnamn, 'w', newline='', encoding='utf-8') as csv_fil:
        csv_writer = csv.writer(csv_fil)
        csv_writer.writerow(header)
        for rad in data:
            csv_writer.writerow([rad['efternamn'], rad['fornamn'], rad['anvandarnamn']])

    print(f'Data har sparats från {json_filnamn} till {csv_filnamn}.')

def avsluta_programmet():
    print('Programmet har avslutats.')
