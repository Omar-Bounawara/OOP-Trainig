"""
IT Company Management System

Author: Omar Bounawara

This program defines classes for managing departments and employees within a company.
It allows the creation of departments, addition of positions to departments, creation of employees,
and provides functionality to display information about departments and employees, apply raises,
and calculate department expenses.
"""

from datetime import datetime

class Departement:
    # List of available departments
    departements = ["Security", "Development", "Infrastructure", "Support", "Networking"]

    # Dictionary to store department positions
    departements_positions = {
        "Security": ["Security Analyst", "Incident Responder", "Cryptography Specialist"],
        "Development": ["Software Engineer", "UI/UX Designer", "Database Administrator"],
        "Infrastructure": ["Systems Administrator", "Cloud Solutions Architect", "DevOps Engineer"],
        "Support": ["Technical Support Specialist", "Customer Success Manager", "IT Support Coordinator"],
        "Networking": ["Network Engineer", "Wireless Network Specialist", "NOC Technician"],
    }

    def __init__(self, name, positions):
        # Initialize department with a name and a list of positions
        self.name = name
        self.positions = positions

        # Add the department to the list if it doesn't exist
        if name not in Departement.departements:
            Departement.departements.append(name)
            Departement.departements_positions[name] = positions

        # List to store employees in the department
        self.employees = []

    def __repr__(self):
        # Return a string representation of the department
        positions = "\n".join(self.positions)
        return f"{self.name}\nList of Positions :\n{positions}"

    def update_list_of_employees(self):
        # Update the list of employees in the department based on the global list of all employees
        self.employees = [employee for employee in Employee.employees if employee.departement == self.name]

    def list_of_employees(self):
        # Return the list of employees in the department
        self.update_list_of_employees()
        return self.employees

    def show_list_of_employees(self):
        # Display information about each employee in the department
        self.update_list_of_employees()
        for employee in self.employees:
            print(employee)

    def expenses(self):
        # Calculate the total expenses for the department based on employee salaries
        self.update_list_of_employees()
        s = sum(employee.salery for employee in self.employees)
        return s

    def add_position(self, position):
        # Add a new position to the department
        self.positions.append(position)


class Employee:
    # List to store all employees
    employees = []

    def __init__(self, full_name, cin, birth_date, departement, position, salery):
        # Initialize an employee with personal information, department, position, and salary
        assert Employee.check_full_name(full_name), 'Full name not valid: consider checking its type and size'
        assert Employee.check_cin(cin), 'CIN not valid: consider checking its type and size'
        assert Employee.check_birth_date(birth_date), 'Birth Date not valid: consider checking its type and size'
        assert Employee.check_departement(departement), 'Department not valid: consider checking its type and size'
        assert Employee.check_position(position, departement), 'Position not valid: consider checking its type and size'
        assert Employee.check_salery(salery), 'Salary not valid: consider checking its type and size'

        self.full_name = full_name
        self.cin = cin
        self.birth_date = birth_date
        self.departement = departement
        self.position = position
        self.salery = salery

        # Add the employee to the global list
        Employee.employees.append(self)

    def __repr__(self):
        # Return a string representation of the employee
        return (
            f"Full Name: {self.full_name}\n"
            f"CIN: {self.cin}\n"
            f"Birth Date: {str(self.birth_date)[:10]}\n"
            f"Department: {self.departement}\n"
            f"Position: {self.position}\n"
            f"Salary: {self.salery}\n"
        )

    def apply_raise(self, raise_value):
        # Apply a salary raise to the employee
        self.salery += raise_value

    @staticmethod
    def check_full_name(full_name):
        # Check if the full name is valid
        is_str = isinstance(full_name, str)
        is_alpha_valid = full_name.replace(" ", "").isalpha()
        space_count_valid = len(full_name.split(' ')) == 2
        space_position_valid = full_name.find(" ") > 2
        size_valid = len(full_name) > 8
        is_valid = is_str and is_alpha_valid and space_count_valid and space_position_valid and size_valid
        return is_valid

    @staticmethod
    def check_cin(cin):
        # Check if the CIN is valid
        is_str = isinstance(cin, str)
        size_valid = len(cin) == 8
        is_num = cin.isnumeric()
        is_valid = is_str and size_valid and is_num
        return is_valid

    @staticmethod
    def check_birth_date(birth_date):
        # Check if the birth date is valid
        is_date = isinstance(birth_date, datetime)
        year_valid = 1960 <= birth_date.year <= 2004
        is_valid = is_date and year_valid
        return is_valid

    @staticmethod
    def check_departement(departement_to_check):
        # Check if the department is valid
        exists = departement_to_check in Departement.departements
        return exists

    @staticmethod
    def check_position(position, employee_departement):
        # Check if the position is valid for the given department
        exists = position in Departement.departements_positions.get(employee_departement)
        return exists

    @staticmethod
    def check_salery(salery):
        # Check if the salary is valid
        is_float = isinstance(salery, float)
        logical_value = salery > 0
        is_valid = is_float and logical_value
        return is_valid


# Create departments
security_department = Departement("Security", ["Security Analyst", "Incident Responder", "Cryptography Specialist"])
development_department = Departement("Development", ["Software Engineer", "UI/UX Designer", "Database Administrator"])
support_department = Departement("Support", ["Technical Support Specialist", "Customer Success Manager", "IT Support Coordinator"])

# Add positions to departments
security_department.add_position("Security Consultant")
development_department.add_position("Mobile App Developer")
support_department.add_position("Help Desk Technician")

# Print department information
print(security_department)
print(development_department)
print(support_department)

# Create employees
employee1 = Employee("Elliot Alderson", "12345678", datetime(1990, 5, 1), "Security", "Security Analyst", 75000.0)
employee2 = Employee("Angela Moss", "87654321", datetime(1988, 10, 15), "Development", "Software Engineer", 80000.0)
employee3 = Employee("Darlene Alderson", "55555555", datetime(1995, 3, 25), "Support", "Technical Support Specialist", 60000.0)

# Print employee information
print(employee1)
print(employee2)
print(employee3)

# Show list of employees in each department
security_department.show_list_of_employees()
development_department.show_list_of_employees()
support_department.show_list_of_employees()

# Apply raise to an employee
employee1.apply_raise(5000.0)
print(f"Updated salary for {employee1.full_name}: ${employee1.salery}")

# Calculate expenses for each department
print(f"Security Department Expenses: ${security_department.expenses()}")
print(f"Development Department Expenses: ${development_department.expenses()}")
print(f"Support Department Expenses: ${support_department.expenses()}")

