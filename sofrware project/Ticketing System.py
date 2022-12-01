from collections import Counter
def banner():
    print("________________________________________________")
    print("IT 5016 Helpdesk Ticket System ")
    print("________________________________________________")
    print("Select from the following choice:")
    print("\t0:Exit")
    print("\t1:Submit help desk tickets")
    print("\t2:Show all tickets")
    print("\t3.Reopened to ticket by number")
    print("\t4:Re-open resolved tickets")
    print("\t5:Display tickets state")
    print("________________________________________________")

List=[]
class Tickets(object):
    Count = 0
    def __init__(self):
        Tickets.Count +=1
        self.Ticket_number = 0
        self.Staff_Id = ""
        self.Name = ""
        self.Email = ""
        self.Description = ""
        self.Response = ""
        self.TicketStatu = ""
    def EnterDate(self):
        self.Ticket_number =len(List)+2000
        self.Staff_Id = input("Please enter a staff ID : ")
        self.Name = input("Please enter a creator name: ")
        self.Email = input("Please enter a email address: ")
        self.Description = input("If you require a new password type: Password Change\n"
                                "Enter description of problem:\n")
        # if User put in "Password change", join characters using staff id and name.
        if self.Description == "password change":
            self.Staff_Id.split()
            password_int = self.Staff_Id[:2]
            self.Name.split()
            password_str = self.Name[:3]
            password = password_int + password_str

            self.Response = "This is a new password: " + str(password)
            self.TicketStatus = 'Closed'
        else:
            self.Response = "Not Yet Provided"
            self.TicketStatus = 'Open'



    def Display(self):
        print("________________________________________________")
        print("Ticket Number:", self.Ticket_number)
        print("Ticket Creator:",self.Name)
        print("Staff ID:",self.Staff_Id)
        print("Email Address:",self.Email)
        print("Description:",self.Description)
        print("Response:",self.Response)
        print("Ticket Status:",self.TicketStatus)
        print("________________________________________________")

    def Search_as_Number(self):
        search_ticket = int(input("please enter number which ticket would you want again:"))
        for i in List:
            if i.Ticket_number == search_ticket:
                Re_description = input("Please enter new description:")
                if Re_description == "password change":
                    i.Staff_Id.split()
                    password_int = i.Staff_Id[:2]
                    i.Name.split()
                    password_str = i.Name[:3]
                    password = password_int + password_str
                    i.Description = Re_description
                    i.Response = "This is a new password: " + str(password)
                    i.TicketStatus = "Closed"
                elif 'resolved' or 'solved' in Re_description.split():
                    i.Response = Re_description
                    i.TicketStatus = 'Closed'
                else:
                    Re_Response = input("Please enter new response:")
                    i.Response = Re_Response
                    i.TicketStatus = 'Open'

    def reopen_slovedTicket(self):
        for i in List:
            if i.TicketStatus == 'Closed':
                i.Display()
        search_ticket = int(input("please enter number which ticket open again?:"))
        for i in List:
            if i.Ticket_number == search_ticket:
                Re_description = input("Please enter new description:")
                i.Response = Re_description
                i.TicketStatus = 'Open'


    def stateDisplay(self):
        open_count = 0

        for i in List:
             if i.TicketStatus == 'Open':
                open_count +=1
        close_count = Tickets.Count - open_count
        print("Tickets Created:", Tickets.Count)
        print("Tickets To Solve:", open_count)
        print("Tickets Resolved:", close_count)








class main:
    while True:
        banner()
        choice = int(input())
        if choice == 1:
            ask_add = 'Y'
            while ask_add == 'Y':
                a = Tickets()
                a.EnterDate()
                List.append(a)
                ask_add = input("Do you want to submit another ticket?(Y/N)\n")
                if ask_add == 'N':
                    break
            Tickets.stateDisplay(a)
        elif choice == 2:
            Tickets.stateDisplay(a)
            print("\nPrinting Tickets:\n")
            for i in range(len(List)):
                List[i].Display()
        elif choice == 3:
            Tickets.Search_as_Number(a)
            Tickets.stateDisplay(a)
        elif choice == 4:
            Tickets.reopen_slovedTicket(a)
            Tickets.stateDisplay(a)
        elif choice == 5:
            print("This is state of tickets:\n")
            Tickets.stateDisplay(a)

        elif choice == 0:
            print("Good bye")
            break


