import csv
from datetime import datetime

from matplotlib import pyplot as plt

#Prompt on options & how to select them
print("Temperature Prompt"
    "\n\t1. High Temperatures"
    "\n\t2. Low Temperatures" 
    "\n\t3. Exit" 
    "\n\tSelect the prompt you wish to use by entering number above.")

prompt = 0

#Loop while within prompt range, close program is exit is selected
while prompt != 3:

    prompt = int(input('\n\tEnter number: '))

    #Open file
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []

        #High temperatures
        if prompt == 1:
            print('\n\tYou have selected High Temperatures')
            
            #Get dates and high temps
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)

            #Plot the high temperatures
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')

            #Format plot
            plt.title("Daily high temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()

        #Low temperatures
        elif prompt == 2:
            print('\n\tYou have selected Low Temperatures')

            #Get dates and high temps
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)

            #Plot the high temperatures
            fig, ax = plt.subplots()
            ax.plot(dates, lows, c='blue')

            #Format plot
            plt.title("Daily low temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()

        #Out of prompt range
        elif prompt > 3 or prompt < 1:
            print('\n\tNumber entered is out of the pompts range.')
        

print('\n\tYou have selected Exit. The program will now close.') 