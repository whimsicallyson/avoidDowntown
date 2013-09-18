import csv
import datetime

#sets today's date, to match the CSV input styles
todayRaw = datetime.date.today()
today = todayRaw.strftime("%m/%d/%y")
todayFootball = todayRaw.strftime("%A, %B %d").upper() #because the NFL csv is different


rawPiratesSchedule = csv.reader(open('pirates_schedule.csv', 'r'), delimiter=',')
piratesSchedule = []

next(rawPiratesSchedule) #skip header row


#in Pirates schedule, we want rows 0 (date), 1 (time), and 4 (location)
for row in rawPiratesSchedule:
    date = row[0][:8]
    time = row[1][:5]
    location = row[4]

    if location == "PNC Park":
        piratesSchedule.append({date:time})

#print piratesSchedule

    

rawSteelersSchedule = csv.reader(open('nfl-2013-schedule1.csv', 'r'), delimiter=',')

steelersSchedule = []

next(rawSteelersSchedule)

#in Steelers schedule, we want rows 2 (home team), 3 (date), and 4 (time)
for row in rawSteelersSchedule:
    location = ''.join(row[2][1:4])
    date = row[3][:-2]
    time = row[4][:4]

    if location == "PIT":
        steelersSchedule.append({date:time})

#print steelersSchedule


rawPenguinsSchedule = csv.reader(open('penguins_schedule.csv','r'), delimiter=',')

penguinsSchedule = []

next(rawPenguinsSchedule)

#in Penguins schedule, we want rows 0 (date), 1 (time), and 4 (location)
for row in rawPenguinsSchedule:
    date = ''.join([row[0][:6], row[0][-2:]])
    time = row[1][:4]
    location = row[4]

    if location[:6] == "CONSOL":
        penguinsSchedule.append({date:time})

#print penguinsSchedule


for row in piratesSchedule:
    if today in row:
        print "BASEBALL GAME TODAY"
        break

for row in penguinsSchedule:
    if today in row:
        print "HOCKEY GAME TODAY"
        break

for row in steelersSchedule:
    if today in row:
        print "FOOTBALL GAME TODAY"
        break


