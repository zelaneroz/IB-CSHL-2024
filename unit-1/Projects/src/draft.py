import csv
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
from pathlib import Path
import random
import string
warnings.filterwarnings("ignore")

def password_req(password):
    messg = []
    bool_temp = False
    if not any(x.isupper() for x in password):
        messg.append('String must have 1 upper case character.')
    if not any(x.islower() for x in password):
        messg.append('String must have 1 lower case character.')
    if not any(x.isdigit() for x in password):
        messg.append('String must have 1 number.')
    if len(password) < 8:
        messg.append('String length should be atleast 8.')
    if not messg:
        messg.append('Valid string.')
        bool_temp=True
    print(messg)
    return bool_temp

def register():
    print("\n\n\33[46m - - - - - \33[1;97mREGISTER\33[46m - - - - - \33[0m")
    #BORDER FOR REGISTRATION
    fname = str(input("\33[0;97mFirst Name: "))
    lname = str(input("Last Name: "))
    uname = str(input("Create a username: "))
    password = str(input("""\nThis ledger requires a password with the following: 
•At least one uppercase letter
•At least one lowercase letter
•At least one number or symbol

Create password: """))
    #CHECK IF PASSWORD HAS ALL REQUIREMENTS
    strt = 1
    while strt >= 1:
        if password_req(password)==True:
            password2 = str(input("Confirm password: "))
            while password2!=password:
                password2 = str(input("Wrong password. Please re-enter: "))
            strt-=1
        else:
            password = str(input("Please enter a valid password. Try again: "))

    msg = f"\nAccount creation successful. Welcome, {fname}!"

    c = int(input("""\n\nWhat would you like to do?
1. Create new ledger
2. Access existing ledger 

Enter choice: """))
    if c==1:
        file_name = str(input("Enter file name: "))
        fle = Path(f'{file_name}.csv')
        fle.touch(exist_ok=True)
        f = open(fle)
        data = [fname, lname, uname, password, fle]
        print(msg)
        with open("user.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(data)
        i = 0
        while i == 0:
            password5 = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(5))
            print("Your Ledger's access code is: \33[0;31m", password5, ".\33[40m\33[0;36mPlease use and remember\33[0;36m this access code for other accounts to access your ledger\33[0m\n\n\n")
            i += 1
        main_ledger(fle)
    #ADD PASSWORD5

    # COLLATE & APPEND DATA

        data = [fle, password5]
        with open("cofcsv.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(data)

    if c == 2:
        g = str(input("Enter access code: "))
        with open("cofcsv.csv", "r") as file:
            csv_data = file.readlines()
        for line in csv_data:
            line = line.strip()
            ac_code = line.split(",")[-1]
            if g == ac_code:
                with open("user.csv", "r") as file:
                    user_data = file.readlines()
                for line2 in user_data:
                    line2 = line2.strip()
                    fle = line2.split(",")[-1]
                main_ledger(fle)

def login():
    print("\n\n\33[46m - - - - - \33[1;97mLOGIN\33[46m - - - - - \33[0m\n")
    a = str(input("Username: "))

    checker, un_checker, msg, attempts = False, False, "", 3
    with open("user.csv", "r") as file:
        user_data = file.readlines()
    for line in user_data:
        line = line.strip()
        un_temp = line.split(",")[2]
        if a == un_temp:
            un_checker = True
    if un_checker == False:
        print("Would you like to Register for a new account instead?")
    if un_checker == True:
        b = str(input("Password: "))
        while attempts > 0:
            p_temp = line.split(",")[3]
            fname = line.split(",")[0]
            fle = line.split(",")[-1]
            if a == un_temp and b == p_temp:
                checker = True
                print(f"Welcome, {fname}. Opening {fle}...")
                attempts = 0
                main_ledger(fle)
            else:
                b = str(input(f"\33[0;31mWrong. {attempts} attemps left. Please try again: \33[0m"))
                attempts -= 1
        if checker==False:
            b = str(input("Would you like to create a new account instead? [Yes/No]"))
            if b.upper()=="YES":
                register()
            else:
                print("Closing Ledger")

def cashflow(fle):
    tot_rec, tot_sent = 0, 0
    # Cashflow formula = TOTAL "RECEIVED" - TOTAL "SENT"
    with open(f"{fle}", "r") as file:
        fin_data = file.readlines()
        for line in fin_data:
            line = line.strip()
            # print(str(line.split(",")[3])) #AMOUNT
            # print(str(line.split(",")[2]))  # CATEGORY
            if str(line.split(",")[2]) == 'SEND':
                tot_sent += int(line.split(",")[3])
            if str(line.split(",")[2]) == "RECEIVE":
                tot_rec += int(line.split(",")[3])
            # print(tot_rec)
        cashflow2 = tot_rec - tot_sent
        csf = (f"\n\33[45m\33[1;97mCash Flow\n\33[0;35mTotal Outflow: {tot_sent} \nTotal Inflow:  {tot_rec} \nCashflow:      {cashflow2}\33[0m\n")
        return csf

def baltrend(fle):
    bal2 = []
    with open(f"{fle}", "r") as file:
        fin_data = file.readlines()
        for line in fin_data:
            line = line.strip()
            bal2.append(int(line.split(",")[-1]))
    print("\n\33[0;37mPlease close the tab with the plot to continue with the ledger.")
    plt.plot(bal2)
    plt.show()

def exp(fle):
    expenses,temp = "",0
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    i, temp_bal,exp_msg,expss = 1,0,"",[]
    while i<=12:
        with open(f"{fle}", "r") as file:
            fin_data = file.readlines()
            for line in fin_data:
                line = line.strip()
                month_temp = line.strip().split(" ")[0]
                month_temp = str(month_temp)[1:]
                #print(line.strip().strip().split(",")[3])
                if str(month_temp) == months[i-1]:
                    #temp_bal = 0
                    if str(line.strip().split(",")[2])=="SEND":
                        #print(line.strip().split(",")[3])
                        temp_bal += int(line.strip().split(",")[3])
        expss.append(temp_bal)
    #print(month_temp, ": ", temp_bal)
        i+=1
        temp_bal=0
    #print(expss)
    j=0
    now = datetime.now()
    now = now.strftime('%Y')

    exp_msg+="\n\33[43m\33[1;97m" + now + " Monthly Expenses Structure\n"
    while j<12:
        exp_msg += "\33[0;33m"+str(months[j]) + ": " + str(expss[j]) + "\n"
        j+=1
    exp_msg+="\33[1;97mTOTAL: "+"\33[1;97m"+str(sum(expss))+"\n"
    return exp_msg

def inc(fle):
    expenses, temp = "", 0
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    i, temp_bal, exp_msg, expss = 1, 0, "", []
    while i <= 12:
        with open(f"{fle}", "r") as file:
            fin_data = file.readlines()
            for line in fin_data:
                line = line.strip()
                month_temp = line.strip().split(" ")[0]
                month_temp = str(month_temp)[1:]
                # print(line.strip().strip().split(",")[3])
                if str(month_temp) == months[i - 1]:
                    # temp_bal = 0
                    if str(line.strip().split(",")[2]) == "RECEIVE":
                        # print(line.strip().split(",")[3])
                        temp_bal += int(line.strip().split(",")[3])
        expss.append(temp_bal)
        # print(month_temp, ": ", temp_bal)
        i += 1
        temp_bal = 0
    # print(expss)
    j = 0
    now = datetime.now()
    now = now.strftime('%Y')

    exp_msg += "\n\33[42m\33[1;97m" + now + " Monthly Income Structure \n"
    while j < 12:
        exp_msg += "\33[0;32m"+str(months[j]) + ": " + str(expss[j]) + "\n"
        j += 1
    exp_msg += "\33[1;97mTOTAL: " + "\33[1;97m" + str(sum(expss))
    return exp_msg

def ledger(fle):
    strt = 1
    while strt>=1:
        try:
            a = int(input("""\33[0;97mThis digital ledger aims to organize your transactions and show important statistics about your current crypto wallet. What would you like to do?
1. Show ledger
2. Add transaction to ledger
3. Show statistics

Enter choice [1-3]: """))
            strt-=1
        except ValueError:
            print("Try again. Please enter a number.")
    strt=1
    while strt>=1:
        strt -= 1
        if a < 1 or a > 3:
            print("Please choose a valid option. Enter a number between 1-3.")
            a = int(input("Enter choice[1-3]: "))
            strt += 1
    if a == 1:
        print("\33[44m                COSMOS LEDGER                 \33[0m\n")
        with open(f"{fle}", "r") as file:
            fin_data = file.readlines()

        for line in fin_data:
            line = line.strip()
            print("\33[0m",line)
        print("\33[44m                                              \33[0m")
    if a == 2:
        # ------CATEGORY & AMOUNT------
        # HOW TO INPUT MULTIPLE ROWS OF DATA AT THE SAME TIME??
        # I ALREADY USED WRITEROWS BUT HOW I CAN I ENTER MULTIPLE ROWS?
        # SHOULD I USE LOOPS FOR THIS PART
        print("\33[46mAdd Transaction\33[0m")
        category = str(input("Send, Receive, or Trade: "))
        amount = int(input("Enter Amount: "))
        category=category.upper()

        # ------TIMESTAMP------
        now = datetime.now()
        timestamp2 = now.strftime('%B %d, %Y | %I:%M %p')

        # ------BALANCE------
        prev_bal=0
        with open(f"{fle}", "r") as file:
            fin_data = file.readlines()
            for line in fin_data:
                line = line.strip()
                prev_bal=int(line.split(",")[-1])

            if category == "SEND":
                balance = prev_bal-amount
            if category == "RECEIVE":
                balance = prev_bal+amount
            if category == "TRADE":
                balance = prev_bal

        data = [timestamp2, category, amount, balance]

        # COLLATE & APPEND DATA
        with open(f"{fle}", "a") as file:
            writer = csv.writer(file)
            writer.writerow(data)

    if a == 3:
        print("""What would you like to know? 
        1. Cash Flow
        2. Balance Trend
        3. Annual Expenses Structure
        4. Annual Income Structure
        5. All""")
        strt = 1
        while strt >= 1:
            try:
                d = int(input("Enter choice [1-5]: "))
                strt -= 1
            except ValueError:
                print("Try again. Please enter a number.")

        if d == 1:
            print(cashflow(fle))
        if d == 2:
            print(baltrend(fle))
        if d==3:
            print(exp(fle))
        if d==4:
            print(inc(fle))
        if d==5:
            print(cashflow(fle))
            print(exp(fle))
            print(inc(fle))
            print(baltrend(fle))


def main_ledger(fle):
    starter = 1
    while starter > 0:
        ledger(fle)
        b = str(input("\n\33[0;97mWould you like to do another action? [\33[0;32mYES/\33[0;31mNO\33[0;97m]: "))
        if b.upper() == "NO":
            starter -= 1
            c = str(input("\33[0;97mWould you like to close the ledger? [\33[0;31mYES/\33[0;32mNO\33[0;97m]:"))
            if c.upper() == "YES":
                print("Closing")
                break
            elif c.upper() == "NO":
                starter += 1



message = "\n\n\n\33[0;96mCosmos is a decentralized network of independent parallel blockchains, each powered by BFT. Cosmos is attempting to create an “internet of blockchains,” or an interoperable network of sovereign, application - specific blockchains.\n"
atom = "\33[46m\33[1;97m     ☽     ☄     ☽     ☄     ☽     ☄     ATOM     ☄     ☽     ☄     ☽     ☄     ☽     \33[0m"
atom = atom.center(40, '*')
from time import sleep
for text in atom:
    print(text, sep='', end='', flush=True)
    sleep(0.03)
print(message.center(70,' '))

a = int(input("""\33[0;97m1. Register
2. Log in
3. Quit

Enter choice: """))

if a==1:
    register()
if a==2:
    login()
if a==3:
    msg2 = "Closing Atom. Thank you."
    for char in msg2:
        print(char, sep='', end='', flush=True)
        sleep(0.1)