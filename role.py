
def role_find(title):
    job_role_list = title.replace(',', '').replace('-', ' ').replace('.', '').replace('&', '') \
                .replace('|', '').replace('@', ' ').replace('/', ' ').replace(':', '').split()
    if "Chief" in job_role_list:
        role = "C-Officer"
        num = 0
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("President" in job_role_list):
        role = "Senior Vice President"
        num = 1
    elif "SVP" in job_role_list:
        role = "Senior Vice President"
        num = 1
    elif "VP" in job_role_list or "President" in job_role_list or "VicePresident" in job_role_list \
            or "Vice" in job_role_list:
        role = "Vice President"
        num = 2
    elif "AVP" in job_role_list:
        role = "Associate Vice President"
        num = 3
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Director" in job_role_list):
        role = "Senior Director"
        num = 4
    elif "Global" in job_role_list and "Director" in job_role_list:
        role = "Global Director"
        num = 5
    elif ("Associate" in job_role_list or "Assistant" in job_role_list) and "Director" in job_role_list:
        role = "Associate Director"
        num = 7
    elif "Director" in job_role_list:
        role = "Director"
        num = 6
    elif "Global" in job_role_list and "Head" in job_role_list:
        role = "Global Head"
        num = 8
    elif "Head" in job_role_list:
        role = "Head"
        num = 9
    elif "Principle" in job_role_list and "Manager" in job_role_list:
        role = "Principle Manager"
        num = 10
    elif "Lead" in job_role_list and "Manager" in job_role_list:
        role = "Lead Manager"
        num = 11
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Manager" in job_role_list):
        role = "Senior Manager"
        num = 12
    elif ("Associate" in job_role_list or "Assistant" in job_role_list) and "Manager" in job_role_list:
        role = "Associate Manager"
        num = 14
    elif "Manager" in job_role_list:
        role = "Manager"
        num = 13
    elif "Leader" in job_role_list or "leader" in job_role_list:
        role = "Leader"
        num = 15
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Consultant" in job_role_list):
        role = "Senior Consultant"
        num = 18
    elif "Consultant" in job_role_list:
        role = "Consultant"
        num = 19
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Partner" in job_role_list):
        role = "Senior Partner"
        num = 20
    elif "Partner" in job_role_list:
        role = "Partner"
        num = 21
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Specialist" in job_role_list):
        role = "Senior Specialist"
        num = 22
    elif "Specialist" in job_role_list:
        role = "Specialist"
        num = 23
    elif "strategist" in job_role_list:
        role = "strategist"
        num = 24
    elif "Coordinator" in job_role_list:
        role = "Coordinator"
        num = 25
    elif "Representative" in job_role_list:
        role = "Representative"
        num = 26
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Executive" in job_role_list):
        role = "Senior Executive"
        num = 27
    elif "Executive" in job_role_list:
        role = "Executive"
        num = 28
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Analyst" in job_role_list):
        role = "Senior Analyst"
        num = 29
    elif "Analyst" in job_role_list:
        role = "Analyst"
        num = 30
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Engineer" in job_role_list):
        role = "Senior Engineer"
        num = 31
    elif "Engineer" in job_role_list:
        role = "Engineer"
        num = 32
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Developer" in job_role_list):
        role = "Senior Developer"
        num = 33
    elif "Developer" in job_role_list:
        role = "Developer"
        num = 34
    elif "Expert" in job_role_list:
        role = "Expert"
        num = 35
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Associate" in job_role_list):
        role = "Senior Associate"
        num = 36
    elif "Associate" in job_role_list:
        role = "Associate"
        num = 37
    elif ("Senior" in job_role_list or "Sr" in job_role_list) and ("Lead" in job_role_list):
        role = "Senior Lead"
        num = 16
    elif "Lead" in job_role_list or "lead" in job_role_list:
        role = "Lead"
        num = 17
    elif "Intern" in job_role_list:
        role = "Intern"
        num = 38
    else:
        role = "Others"
        num = 39
    return [num, role]
