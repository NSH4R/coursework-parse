from bs4 import BeautifulSoup
import requests

'''https://kubsau.ru/education/portfolio/students/1c078a6e-3b5f-4e37-b551-65bfe3ebb28f/ - тестовый url студента
   https://kubsau.ru/education/portfolio/groups/c27cda9c-e5af-47e2-874e-78084a2d0e94/ - тестовый url группы
'''


def parse_student(url: str) -> dict:
    response = requests.get(url, verify=False)  # kringe but working...
    resp_date = response.text if response.status_code == 200 else response.raise_for_status()
    soup = BeautifulSoup(resp_date, 'html.parser')
    works_with_tags = (soup.find_all('table', class_='table-style')[-1].find('tbody', class_='groups-data').
                       find_all('td'))
    works_dict = {}
    for i in range(0, len(works_with_tags), 2):
        works_dict[works_with_tags[i].get_text()] = works_with_tags[i + 1].get_text()
    return works_dict

