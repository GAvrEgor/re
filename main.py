from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

phone = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
num = r"+7(\2)\3-\4-\5 \6\7"
list = []
def main(phonebook_list):
    new_list = []
    for item in phonebook_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(phone, num, item[5]),
                  item[6]]
        new_list.append(result)
    return join(new_list)


def join(contacts):
    for contact in contacts:
        firstname = contact[0]
        lastname = contact[1]
        surname = contact[2]
        for new_contact in contacts:
            new_firstname = new_contact[0]
            new_lastname = new_contact[1]
            new_surname = new_contact[2]
            if firstname == new_firstname and \
               lastname == new_lastname and \
               (surname == new_surname or surname == "" or new_surname == ""):
                if contact[2] == "":
                    contact[2] = new_contact[2]
                if contact[3] == "":
                    contact[3] = new_contact[3]
                if contact[4] == "":
                    contact[4] = new_contact[4]
                if contact[5] == "":
                    contact[5] = new_contact[5]
                if contact[6] == "":
                    contact[6] = new_contact[6]

    result_list = []
    for elem in contacts:
        if elem not in result_list:
            result_list.append(elem)

    return result_list


# # код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
  datawriter.writerows(main(contacts_list))
