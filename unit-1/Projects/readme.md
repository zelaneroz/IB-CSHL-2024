# Crypto Wallet

![](22ROOSE-master768.gif)  
<sub>Illustration for Glenn Harvey</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

Design statement:
I will to design and make a <ins>digital ledger</ins> for a client who is <ins>Ms. Sato</ins>, a local trader. The <ins>project</project> will be about <ins>designing a digital ledger</a> and is constructed using the software <ins>Python 3.9.13</ins>. It will take <ins>2 weeks</ins> to make and will be evaluated according to the criteria below.


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the crypotocurrency selected - Cosmos.
3. The electronic ledger allows to enter, withdraw and record transaction (including the recipient, sender, timestamp, and wallet ID of the involved stakeholders).
4. The electronic ledger categorizes transactions into either buying, selling, or transfer of Cosmos coins.
5. The electronic ledger shows important statistics such as Cash Flow, Balance Trend, and Income & Expenses Structure.
6. The electronic ledger is secured; it requires a password for access.
7. The electronic ledger caters to the client, Ms. Sato, and multiple users at the same time; it allows multiple users to have their own ledger or access the same ledger as Ms. Sato.

## Rationale for Proposed Solution
The proposed product, Atom: a Cosmos Crypto E-ledger, is an effective solution to the client, Ms. Sato's problem and status quo. The program effectively meets Ms. Sato's problem as the ledger easily ouputs statistics like Cash Flow, Balance Trend, Income Structure, and Expenses Structure. It also easily shows past transactions, which include information like Timestamp, Amount, Balance, and Categories: Buy, Sell, and Trade. The program is able to create multiple ledgers, in case Ms. Sato wants to create different ledgers for multiple functions or in case she wants a fresh start. Lastly, the program is secure since each ledger is limited to a user, or a user that knows the specific ledger's access code. The program's account registration's password requirements add to the program's sense of security as it lessens the tendency for external users to easily guess passwords through word combinations or "dictionary attacks".

# Criteria B: Design

## Test Plan
#### Registration
| **Variable**        | **Input** | **Code**               | **Output**                        | **Expected Output**               | **Satisfied?** |
|---------------------|-----------|------------------------|-----------------------------------|-----------------------------------|----------------|
| fname - First name  | Zelan     | None                   | None                              | None                              | ✓              |
| lname - Last Name   | Espanto   | None                   | None                              | None                              | ✓              |
| uname - Username    | zelaneroz | None                   | None                              | None                              | ✓              |
| password - Password | zelan123  | password_req(password) | False                             | False                             | ✓              |
| password - Password | Zelan123  | password_req(password) | True                              | True                              | ✓              |
| c                   | 3         | accepted range: [1-2]  | False; Error Message; Input again | False; Error Message; Input again | ✓              |
| c                   | 2         | accepted range: [1-2]  | *Asks for ledger access code*     | *Asks for ledger access code*     | ✓              |
| c                   | 1         | accepted range: [1-2]  | *Asks for new ledger file name*   | *Asks for new ledger file name*   | ✓              |
|                     |           |                        |                                   |                                   |                |
#### Login
| **Variable**      | **Input**                 | **Code**                        | **Output**                                       | **Expected Output**                              | **Satisfied? |
|-------------------|---------------------------|---------------------------------|--------------------------------------------------|--------------------------------------------------|--------------|
| a - str(Username) | zelaneroz                 | *Checks if username exists*     | True                                             | True                                             | ✓            |
| a - str(Username) | canela2                   | *Checks if username exists*     | False                                            | False                                            | ✓            |
| b - Password      | Zelan123                  | *Checks if password is correct* | True                                             | True                                             | ✓            |
| b - Password      | Zelan123456               | *Checks if password is correct* | False                                            | False *3 more password input attempts*           | ✓            |
| b - Password      | Zelan123456 (3rd attempt) | *Checks if password is correct* | False *Offers if user wants to register instead* | False *Offers if user wants to register instead* | ✓            |

#### Main Program
| **Variable**     | **Input** | **Code**                                         | **Output**                                               | **Expected Output**                                      | **Satisfied? |
|------------------|-----------|--------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|--------------|
| a (int) - Option | 1         | if a==1: register()                              | *Register function initiated*                            | *Register Function initiated*                            | ✓            |
| a (int) - Option | 2         | if a==2: login()                                 | *Log in function initiated*                              | *Log in function initiated*                              | ✓            |
| a (int) - Option | 3         | if a==3: *Closes program*                        | End program                                              | End program                                              | ✓            |
| a (int) - Option | gyfhghsj  | *Validates if input is an int*                   | False                                                    | False Choose again                                       | ✓            |
| a (int) - Option | 4         | *Checks if input is within accepted range (1-3)* | False                                                    | False *Error Message. Enter again*                       | ✓            |
| b - str [YES/NO] | Yes       | *Would you like to do another action?*           | ledger()                                                 | ledger()                                                 | ✓            |
| b - str [YES/NO] | No        | *Would you like to do another action?*           | *Asks: Would you like to close the ledger*               | *Asks: Would you like to close the ledger*               | ✓            |
| b - str [YES/NO] | Yes       | *Would you like to close the ledger?*            | *Closing*                                                | *Closing*                                                | ✓            |
| b - str [YES/NO] | No        | *Would you like to close the ledger*             | *Asks: Would you like to do another action*              | *Asks: Would you like to do another action?*             | ✓            |
| a - int          | 1         | *Enter choice [1-3]*                             | *Shows Ledger*                                           | *Shows Ledger*                                           | ✓            |
| a - int          | 2         | *Enter choice [1-3]*                             | *Asks for new row of data for the ledger*                | *Asks for new row of data for the ledger*                | ✓            |
| a - int          | 3         | *Enter choice [1-3]*                             | *Show statistics options*                                | *Show statistics options*                                | ✓            |
| a - int          | ohgfhh    | *Enter choice [1-3]*                             | print("Try again. Please enter a number.")               | print("Try again. Please enter a number.")               | ✓            |
| a - int          | 5         | *Enter choice [1-3]*                             | Please choose a valid option.... *Ask for another input* | Please choose a valid option.... *Ask for another input* | ✓            |


## System Diagram
![project_diagrams-System Diagram drawio](https://user-images.githubusercontent.com/113817801/194740842-3a772d67-ff86-456d-8a38-1af79ebbaff7.png)


## Flow Diagrams
#### Registration Function Flowchart

![project_diagrams-Log in Flowchart drawio](https://user-images.githubusercontent.com/113817801/194741830-c2aa6430-7bc3-491f-abb9-1f54f4d03d70.png)

#### Password Requirement Flowchart
![project_diagrams-Password Requirement drawio](https://user-images.githubusercontent.com/113817801/194742633-7faf7f34-802e-4049-b22a-ece8b5801ed0.png)

#### Balance Trend Flowchart
![project_diagrams-Balance Trend drawio](https://user-images.githubusercontent.com/113817801/194742862-6da6bfcd-9f01-495a-9ab7-729f251cc8ab.png)



## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                                         | To have a clear idea of the hardware and software requirements for the proposed solution                        | 10min         | Sep 22                | B         |
| 2       | Completion of success criteria                                         | To have a good definition of what needs to be achieved and what a successful project would look like                        | 10min         | Sep 22               | A         |
| 3       | Alpha Development                                         | Create an initial draft of the code that satisfies the success criteria created.                        | 7 hours         | October 6               | C         |
| 4       | Beta-testing                                         | Test the program on actual users and uncover any issue or bugs before releasing to the client.                        | 40 minutes         | October 7               | A         |
| 5       | Beta Development                                        | Fix uncovered issues & bugs, and add features that are previously suggested                       | 6 hours         | October 9               | C         |


<br></br>


# Criteria C: Development
## Existing Tools
**Integrated Development Environment (IDE)**: PyCharm


**Libraries**
* import warnings; warnings.filterwarnings("ignore")
* random
* pathlib
* datetime
* matplotlib.pyplot
* string
* time


**Structures**
* Functions
* Loops
    * For
    * While
* Validation: try, except ValueError
* with open ("\.csv", "a") as file
* write.(\data)
* Data Types: String, Boolean, Integer
* Animation: sleep (typewriter effect)


## Sources
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html 
