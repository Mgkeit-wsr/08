from HHRequests import *
import json


if __name__ == '__main__':
    hh_req = HHRequester()
    # print(HHRequester.get_professional_roles_id("Менеджер", self=HHRequester))
    # print(HHRequester.get_experience_id(self=HHRequester))
    # print(HHRequester.get_metro_id(self=HHRequester))
    # print(HHRequester.get_employment_id(self=HHRequester))
    # print(HHRequester.send_jobs(self=HHRequester))
    # print(HHRequester.get_schedule_id(self=HHRequester))

    with open('requirements.json', encoding='utf-8') as f:
        requirements = json.load(f)
    # print(requirements)

    if requirements['professional_role'] != 'любая':
        requirements['professional_role'] = HHRequester.get_professional_roles_id(requirements['professional_role'],
                                                                           self=HHRequester)
    else:
        requirements.pop('professional_role')

    if requirements['experience'] != 'любая':
        requirements['experience'] = HHRequester.get_experience_id(self=HHRequester)[requirements['experience']]
    else:
        requirements.pop('experience')
    if requirements['metro'] != 'любая':
        requirements['metro'] = HHRequester.get_metro_id(self=HHRequester)[requirements['metro']]
    else:
        requirements.pop('metro')
    if requirements['salary'] != 'любая':
        requirements['salary'] = requirements['salary']
    else:
        requirements.pop('salary')
    if requirements['employment'] != 'любая':
        requirements['employment'] = HHRequester.get_employment_id(self=HHRequester)[requirements['employment']]
    else:
        requirements.pop('employment')
    if requirements['schedule'] != 'любая':
        requirements['schedule'] = HHRequester.get_schedule_id(self=HHRequester)[requirements['schedule']]
    else:
        requirements.pop('schedule')

    # print(requirements)

    hh_req.get_options(requirements)
    hh_req.add_options()

    card = hh_req.send_jobs()
    card = json.loads(card)
    card = card['items'][0]

    print(card['name'])
    print(f"{card['salary']['from']} RUB")
    print(f"{card['address']['street']}, д. {card['address']['building']}, "
          f"метро {card['address']['metro']['station_name']}, "
          f"{card['address']['metro']['line_name']}")
    print(card['snippet']['requirement'])
    print(card['alternate_url'])

    # vacancy = []
    # vacancy.append(card['name'])
    # vacancy.append(f"{card['salary']['from']} RUB")
    # vacancy.append(f"{card['address']['street']}, д. {card['address']['building']}, "
    #       f"метро {card['address']['metro']['station_name']}, "
    #       f"{card['address']['metro']['line_name']}")
    # vacancy.append(card['snippet']['requirement'])
    # vacancy.append(card['alternate_url'])
    #
    # with open('vacancies.txt', "w", encoding='utf-8') as f:
    #     for s in vacancy:
    #         f.write(s + '\n')
