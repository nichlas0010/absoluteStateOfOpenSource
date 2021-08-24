import os

def clear():
    os.system('cls')

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
pyscript.write("\tcur_time = datetime.now().strftime(\"%H:%M\")\n")
for hour in range(24):
    for minute in range(60):
        pyscript.write("\tif cur_time == \"" + str(hour) + ":"+ str(minute) + "\":\n")
        if minute == 0:
            pyscript.write("\t\tprint(\"The time is now: " + str(hour) + " o'clock\", end = \'\\r\')\n")
        else:
            pyscript.write("\t\tprint(\"The time is now: " + str(minute) + " minutes past " + str(hour) + " o'clock\", end = \'\\r\')\n")
        pyscript.write("\t\tcontinue\n")
pyscript.close()

print("Programme installed! Run the \"Time.sh\" file to run it!")