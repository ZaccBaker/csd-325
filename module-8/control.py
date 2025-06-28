from file import *
from data import *

FILE = 'student.json'

#Gets data
def get_data():

    prompt = 'Original Student List'

    data = read_file(FILE)
    output_data(prompt, data)

#My data control
def my_data():

    prompt = 'Updated Student List'
    myName_First = 'Zac'
    myName_Last = 'Baker'
    myStudent_ID = '23156'
    myEmail = 'zabaker@gmail.com'

    myInfo = format_myData(myName_First, myName_Last, myStudent_ID, myEmail)
    dataUpdated = append_myData(myInfo, read_file(FILE))
    update_file(FILE, dataUpdated)
    output_data(prompt, dataUpdated)

    print('The JSON file was updated successfully.')