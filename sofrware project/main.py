# Create storage for tickets information.
dictionary = [{"ticket number": 2000,
               "Staff Id": 2345,
               "Email": "eoingnw@gmail.com",
               "Description": "Password change",
               "Ticket Status": "Open",
               "response": "User password was set 1234"},
              {"ticket number": 2001,
               "Staff Id": 2142351,
               "Email": "AMY@gmail.com",
               "Description": "Password change",
               "Ticket Status": "Closed",
               "response": "User password was set 213414"},
              {"ticket number": 2002,
               "Staff Id": 22351,
               "Email": "Sophie@gmail.com",
               "Description": "Password change",
               "Ticket Status": "Closed",
               "response": "User password was set 213414"}
              ]


def banner():
    print("IT 5016 Helpdesk Ticket System ")
    print("________________________________________________")
    print("Select from the following choice:")
    print("\t0:Exit")
    print("\t1:Submit helpdesk tickets")
    print("\t2:Show all tickets")
    print("\t3.Reopened to ticket by number")
    print("\t4:Re-open resolved tickets")
    print("\t5:Display tickets state")
    print("________________________________________________")


# each tickets info.
tickets = {}


def add_ticket(dictionary):
    tickets["ticket number"] = 2000 + len(dictionary)
    staff_id = input("Please enter a staff ID : ")
    staff_name = input("Please enter a creator name: ")
    tickets['Staff Id'] = staff_id
    tickets['name'] = staff_name
    tickets['email'] = input("Please enter a email address: ")
    tickets['Description'] = input("If you require a new password type: Password Change"
                                   "Enter description of problem: ")
    # if User put in "Password change", join characters using staff id and name.
    if tickets['Description'] == "password change":
        str(staff_id).split()
        password_int = staff_id[:2]
        staff_name.split()
        password_str = staff_name[:3]
        password = password_int + password_str
        print(password)
        tickets['response'] = "This is a new password: " + str(password)
        tickets['Ticket Status'] = 'Closed'
    else:
        tickets['response'] = "Not Yet Provided"
        tickets['Ticket Status'] = 'Open'
    dictionary.append(tickets)


def allDisplay(dictionary):
    for list in dictionary:
        for key in list:
            print("________________________________________________")
            print("{}: {}".format(key, list[key]))


def open_Ticketnumber(dictionary):
    search_ticket = int(input("please enter number which ticket open again?:"))
    res = next((list for list in dictionary if list['ticket number'] == search_ticket), None)
    Re_description = input("Please enter new description:")
    if Re_description == "password change":
        str(res['Staff Id']).split()
        password_int = res['Staff Id'][:2]
        res['name'].split()
        password_str = res['name'][:3]
        password = password_int + password_str
        res.update({"response": password})
    else:
        Re_Response = input("Please enter new response:")
        res.update({"Description": Re_description})
        res.update({'response': Re_Response})
        res.update({'Ticket Status': 'Closed'})



def reopen_slovedTicket(dictionary):
    for c in range(len(dictionary)):
        for list in dictionary[c]:
            if dictionary[c][list] == "Closed":
                for key in dictionary[c]:
                    print("________________________________________________")
                    print("{}:{}".format(key, dictionary[c][key]))
    search_ticket = int(input("please enter number which ticket open again?:"))
    res = next((list for list in dictionary if list['ticket number'] == search_ticket), None)
    Re_description = input("Please enter new description:")
    res.update({"Description": Re_description})
    res.update({'response': "Not Yet Provided" })
    res.update({'Ticket Status': 'Open'})


def stateDisplay(dictionary):
    res = [sub['Ticket Status'] for sub in dictionary]
    submit = len(dictionary)
    open =res.count('Open')
    close =res.count('Closed')
    print("Submitted Ticket:{}".format(submit))
    print("Open Ticket:{}".format(open))
    print("Closed Ticket:{}".format(close))





while (True):
    banner()
    choice = int(input())
    if choice == 1:
        ask_add = 'Y'
        while ask_add == 'Y':
            add_ticket(dictionary)
            ask_add = input("Do you want to submit another ticket?(Y/N)\n")
            if ask_add == 'N':
                break
    elif choice == 2:
        print("This is All tickets.")
        print(allDisplay(dictionary))
    elif choice == 3:
        print(open_Ticketnumber(dictionary))
    elif choice == 4:
        print(reopen_slovedTicket(dictionary))
    elif choice == 5:
        print("This is state of tickets:\n")
        print(stateDisplay(dictionary))
    elif choice == 0:
        print("Good bye")
        break

# ticket detail will be put into array

# ask them to enter detail
