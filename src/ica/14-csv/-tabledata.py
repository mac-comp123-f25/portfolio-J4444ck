
def lookup_office(name, direct_table):
    for row in direct_table:
        if row['Name'] == name:
            # return both building and office number as a tuple or formatted string
            return row['Building'], row['Office']

    return "No entry: " + name

def lookup_by_date(month, day, table):
    for row in table:
        if row['Month'] == month and str(row['Day']) == str(day):
            return row

    return "No entry for " + month + " " + str(day)



def collect_by_letter(letter, table):
    match_list = []
    for row in table:
        name = row.get('Name', '')
        if name and name[0].upper() == letter.upper():
            match_list.append(row)
    return match_list

def select_by_month(month, table):
    match_list = []
    for row in table:
        if row.get('Month') == month:
            match_list.append(row)
    return match_list