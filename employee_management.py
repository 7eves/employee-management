import csv

employee_list = []

def display_menu():
    print ("\nEmployee Management System")
    print ("1. Add Employee")
    print ("2. Remove Employee")
    print ("3. Search Employee")
    print ("4. Display All Employees")
    print ("5. Save and Exit")
    return input("Enter your choice (1-5): ")

def add_employee():
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    department = input("Enter employee department: ")

    #creating a dictionary
    employee ={"name": name, "age": age, "department": department}
    employee_list.append(employee)

    print(f"Employee {name} added successfully!")

def remove_employee():
    name = input("Enter name of the employee to remove: ")
    found = False
    for employee in employee_list:
        if employee["name"].lower() == name.lower():
            employee_list.remove(employee)
            print(f"Employee {name} has been removed.")
            found = True
            break # exit the loop
    if not found:
        print("Employee not found. Please enter a valid name.")

def search_employee():
    search = input("Enter the name of employee: ")
    found = False
    for employee in employee_list:
        if search.lower() == employee["name"].lower():
            print (employee)
            found = True
        
    if not found:
        print("Employee not found.")

def display_employee():
    if not employee_list:
        print("No employees found in the database")
    else:
        for employee in employee_list:
            print(employee["name"], employee["age"], employee["department"])


def save_exit():
    with open("employee_list.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Name", "Age", "Department"]) #write the header
        for employee in employee_list:
            csv_writer.writerow([employee["name"], employee["age"], employee["department"]])

    print ("Employee list has been saved!")

#Main loop
while True:
    choice = display_menu()
    
    if choice == "1":
        add_employee()
        
    
    elif choice == "2":
        remove_employee()
        

    elif choice == "3":
        search_employee()
        

    elif choice == "4":
        display_employee()
        

    elif choice == "5":
        save_exit()
        break
    
    else:
        print ("Invalid choice. Please enter a number from 1 to 5.")



