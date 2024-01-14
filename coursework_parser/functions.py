from bs4 import BeautifulSoup
import requests
import re
import urllib3

urllib3.disable_warnings()

'''https://kubsau.ru/education/portfolio/students/1c078a6e-3b5f-4e37-b551-65bfe3ebb28f/ - тестовый url студента
   https://kubsau.ru/education/portfolio/groups/c27cda9c-e5af-47e2-874e-78084a2d0e94/ - тестовый url группы
'''


def parse_portfolio(stud_id: str) -> dict:
    url = f'https://kubsau.ru/education/portfolio/students/{stud_id}'
    response = requests.get(url, verify=False)  # kringe but working...
    resp_date = response.text if response.status_code == 200 else response.raise_for_status()
    soup = BeautifulSoup(resp_date, 'html.parser')
    works_with_tags = (soup.find_all('table', class_='table-style')[-1].find('tbody', class_='groups-data').
                       find_all('td'))
    works_dict = {}

    for i in range(0, len(works_with_tags), 2):
        works_dict[works_with_tags[i].get_text()] = works_with_tags[i + 1].get_text()
    return works_dict


def get_students(group_id: str) -> dict:
    url = f'https://kubsau.ru/education/portfolio/groups/{group_id}'
    response = requests.get(url, verify=False)  # kringe but working...
    resp_date = response.text if response.status_code == 200 else response.raise_for_status()
    soup = BeautifulSoup(resp_date, 'html.parser')
    group_ids_teg = soup.find('div', class_='page-content').find_all('li')
    students_dict = {}

    for i in range(0, len(group_ids_teg)):
        student_id = re.sub(r'/education/portfolio/students/|/', '', group_ids_teg[i].find('a').get('href'))
        student_name = group_ids_teg[i].a.string
        students_dict[student_id] = {'name': student_name}
    return students_dict


def find_coursework(group_id: str, desired_topic: str):
    students = get_students(group_id)
    found_students = [{'student_id': key, 'name': students[key]['name'], 'title': subject} for key in students.keys()
                      for subject in parse_portfolio(key).values() if desired_topic in subject]
    return found_students


print(find_coursework('90dfc605-d7f3-49d0-9ff3-2737b908ebac',
                      'Разработка информационной  системы  для автоматизации  подготовки, хранения и выдачи на печать платежного требования'))
print(find_coursework('d30a74aa-0dfb-4abc-bc0c-2c254ed361c2',
                      'Разработка информационной  системы  для автоматизации  подготовки, хранения и выдачи на печать платежного требования'))
print(find_coursework('f5e1fe2c-4e8a-41bc-bbdd-796945b598ca',
                      'Разработка информационной  системы  для автоматизации  подготовки, хранения и выдачи на печать платежного требования'))
