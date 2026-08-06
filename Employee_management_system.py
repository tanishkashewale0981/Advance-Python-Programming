# Employee Management System using OOP

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      : ₹", self.salary)
        print("Category    :", self.category())
        print("-" * 30)


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Employee Salary: "))

        emp = Employee(emp_id, name, salary)
        self.employees.append(emp)

        print("Employee Added Successfully!\n")

    def display_all(self):
        if len(self.employees) == 0:
            print("No employee records found.")
        else:
            print("\n------ Employee Details ------")
            for emp in self.employees:
                emp.display()


# Main Program
company = Company()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        company.add_employee()
    elif choice == 2:
        company.display_all()
    elif choice == 3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Please try again.")