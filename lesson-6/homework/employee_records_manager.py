import os

def add_employee():
    with open('employees.txt', 'a') as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully.")

def view_employees():
    if os.path.exists('employees.txt'):
        with open('employees.txt', 'r') as file:
            records = file.readlines()
            if records:
                for record in records:
                    print(record.strip())
            else:
                print("No employee records found.")
    else:
        print("No employee records found.")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    if os.path.exists('employees.txt'):
        with open('employees.txt', 'r') as file:
            for record in file:
                if record.startswith(emp_id + ','):
                    print(record.strip())
                    found = True
                    break
    if not found:
        print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False
    if os.path.exists('employees.txt'):
        with open('employees.txt', 'r') as file:
            records = file.readlines()
            for record in records:
                if record.startswith(emp_id + ','):
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
                    found = True
                else:
                    updated_records.append(record)
        if found:
            with open('employees.txt', 'w') as file:
                file.writelines(updated_records)
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")
    else:
        print("No employee records found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False
    if os.path.exists('employees.txt'):
        with open('employees.txt', 'r') as file:
            records = file.readlines()
            for record in records:
                if not record.startswith(emp_id + ','):
                    updated_records.append(record)
                else:
                    found = True
        if found:
            with open('employees.txt', 'w') as file:
                file.writelines(updated_records)
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")
    else:
        print("No employee records found.")


while True:
    print("\nEmployee Records Manager")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_employee()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")