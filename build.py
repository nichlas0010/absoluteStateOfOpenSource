import os

def clear():
    os.system('cls')

def monthToMonth(n):
    if n == 1:
        return "January"
    if n == 2:
        return "February"
    if n == 3:
        return "March"
    if n == 4:
        return "April"
    if n == 5:
        return "May"
    if n == 6:
        return "June"
    if n == 7:
        return "July"
    if n == 8:
        return "August"
    if n == 9:
        return "September"
    if n == 10:
        return "October"
    if n == 11:
        return "November"
    if n == 12:
        return "December"

try:
    bashScript = open("Time.sh", "x")
    pyscript = open("Time.py", "x")
except:
    answer = ""
    while answer != "Yes" and answer != "No":
        clear()
        print("Cannot install, files already exist!")
        print("Do you want to uninstall? (Yes/No)")
        answer = input("Yes/No:\n")
        if answer == "Yes":
            if os.path.exists("Time.sh"):
                os.remove("Time.sh")
            if os.path.exists("Time.py"):
                os.remove("Time.py")
        exit()

bashScript.write("python Time.py")
bashScript.close()

pyscript.write("from datetime import datetime\n\n")
pyscript.write("import os\n")
pyscript.write("import sys\n")
    
pyscript.write("while True:\n")
pyscript.write("\tcur_time = datetime.now().strftime(\"%Y%m%d%H%M\")\n")
for year in range(1970, 2034):
    clear()
    doneSoFar = year-1969
    print("["+"█"*(doneSoFar//4)+"_"*(16-(doneSoFar//4))+"]")
    print("Now at year:", year)
    for month in range(1, 13):
        for day in range(1, 32):
            for hour in range(24):
                for minute in range(60):
                    pyscript.write("\tif cur_time == \"" + str(year) + str(month) + str(day) + str(hour) + str(minute) + "\":\n")
                    if minute == 0:
                        pyscript.write("\t\tprint(\"The time is now: " + str(hour) + " o'clock, on day " + str(day) + " of " + monthToMonth(month) + ", " + str(year) + "\", end = \'\\r\')\n")
                    else:
                        pyscript.write("\t\tprint(\"The time is now: " + str(minute) + " minutes past " + str(hour) + " o'clock, on day " + str(day) + " of " + monthToMonth(month) + ", " + str(year) + "\", end = \'\\r\')\n")
                    pyscript.write("\t\tcontinue\n")
pyscript.close()

print("Programme installed! Run the \"Time.sh\" file to run it!")