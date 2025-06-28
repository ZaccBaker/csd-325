
#Formats info from data and outputs original list
def output_data(prompt, data):

    print(f'\n{prompt}')

    for info in data:
        
        print(f'\t{info['L_Name']}, {info['F_Name']} : ID = {info['Student_ID']}, Email = {info['Email']}')


#Format my data to dictionary, json format
def format_myData(fName, lName, id, email):

    info = {
        "F_Name": fName,
        "L_Name": lName,
        "Student_ID": id,
        "Email": email
    }
    
    return info

#Append my data to json original data, read_file is used as parameter for data
def append_myData(myInfo, data):

    data.append(myInfo)

    # print(data)
    return data