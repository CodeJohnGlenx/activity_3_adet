import sqlite3 


connection = sqlite3.connect('faculty.db')
cursor = connection.cursor()

# Create a Table 
sql = """CREATE TABLE IF NOT EXISTS faculty (
    number INTEGER UNSIGNED,
    name TEXT,
    status TEXT,
    department INTEGER UNSIGNED,
    programming INTEGER UNSIGNED,
    database INTEGER UNSIGNED,
    data_communication INTEGER UNSIGNED,
    thesis INTEGER UNSIGNED,
    compiler_design INTEGER UNSIGNED,
    software_engineering INTEGER UNSIGNED
)
"""
cursor.execute(sql)
connection.commit()
connection.close()


# insert entry 
def save(entries):
    connection = sqlite3.connect('faculty.db')
    cursor = connection.cursor()
    sql = f"""INSERT INTO faculty
    (number, name, status, department, programming, database, data_communication, thesis, compiler_design, software_engineering)
    VALUES ({entries['faculty_num']}, '{entries['faculty_name']}', '{entries['faculty_status']}', {entries['faculty_department']}, {entries['programming']}, {entries['database']}, {entries['data_communication']}, {entries['thesis']}, {entries['compiler_design']}, {entries['software_engineering']});
    """

    cursor.execute(sql)
    connection.commit()
    connection.close()

# edit entry
def edit(entries):
    connection = sqlite3.connect('faculty.db')
    cursor = connection.cursor()
    sql = f"""
    UPDATE faculty
    SET name='{entries['faculty_name']}', status='{entries['faculty_status']}', department={entries['faculty_department']}, programming={entries['programming']}, database={entries['database']}, data_communication={entries['data_communication']}, thesis={entries['thesis']}, compiler_design={entries['compiler_design']}, software_engineering={entries['software_engineering']}
    WHERE number={entries['faculty_num']};
    """

    cursor.execute(sql)
    connection.commit()
    connection.close()

# delete entry by faculty_id
def delete(faculty_id):
    connection = sqlite3.connect('faculty.db')
    cursor = connection.cursor()
    sql = f"""
    DELETE FROM faculty WHERE number={faculty_id}
    """

    cursor.execute(sql)
    connection.commit()
    connection.close()

# search entry by faculty_id
def search(faculty_id):
    connection = sqlite3.connect('faculty.db')
    cursor = connection.cursor()
    sql = f"""
    SELECT * FROM faculty WHERE 
    number = {faculty_id};
    """

    cursor.execute(sql)
    connection.commit()

    result = cursor.fetchall()

    connection.close()

    return result

# view entries 
def view(entries):
    conditions = []
    connection = sqlite3.connect('faculty.db')
    cursor = connection.cursor()

    if entries['faculty_num'] > 0:
        conditions.append(f" number LIKE '%{entries['faculty_num']}%'")
    if entries['faculty_name'] != '':
        conditions.append(f" name LIKE '%{entries['faculty_name']}%'")
    if entries['faculty_status'] != '':
        conditions.append(f" status LIKE '%{entries['faculty_status']}%'")
    if entries['faculty_department'] >= 0:
        conditions.append(f" department LIKE '%{entries['faculty_department']}%'")
    if entries['programming'] == 1:
        conditions.append(f" programming LIKE '%{entries['programming']}%'")
    if entries['database'] == 1:
        conditions.append(f" database LIKE '%{entries['database']}%'")
    if entries['data_communication'] == 1:
        conditions.append(f" data_communication LIKE '%{entries['data_communication']}%'")
    if entries['thesis'] == 1:
        conditions.append(f" thesis LIKE '%{entries['thesis']}%'")
    if entries['compiler_design'] == 1:
        conditions.append(f" compiler_design LIKE '%{entries['compiler_design']}%'")
    if entries['software_engineering'] == 1:
        conditions.append(f" software_engineering LIKE '%{entries['software_engineering']}%'")
    
    if conditions:
        sql = f"""
        SELECT * FROM faculty WHERE 
        {" AND".join(conditions)};
        """
    else:
        sql = f"""
        SELECT * FROM faculty
        """

    cursor.execute(sql)
    connection.commit()

    result = cursor.fetchall()

    connection.close()

    return result

