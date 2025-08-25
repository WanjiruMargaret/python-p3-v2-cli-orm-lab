# lib/helpers.py

from models.department import Department
from models.employee import Employee


# ------------------------
# Department CLI functions
# ------------------------

def list_departments():
    depts = Department.get_all()
    for d in depts:
        print(d)


def find_department_by_name():
    name = input("Enter the department's name: ")
    dept = Department.find_by_name(name)
    if dept:
        print(dept)
    else:
        print(f"Department {name} not found")


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    dept = Department.find_by_id(id_)
    if dept:
        print(dept)
    else:
        print(f"Department {id_} not found")


def create_department():
    name = input("Enter the department's name: ")
    try:
        dept = Department.create(name)
        print(f"Success: {dept}")
    except Exception as e:
        print("Error creating department: ", e)


def update_department():
    id_ = input("Enter the department's id: ")
    dept = Department.find_by_id(id_)
    if not dept:
        print(f"Department {id_} not found")
        return
    name = input("Enter the department's new name: ")
    try:
        dept.name = name
        dept.update()
        print(f"Success: {dept}")
    except Exception as e:
        print("Error updating department: ", e)


def delete_department():
    id_ = input("Enter the department's id: ")
    dept = Department.find_by_id(id_)
    if not dept:
        print(f"Department {id_} not found")
        return
    dept.delete()
    print(f"Department {id_} deleted")


# ---------------------
# Employee CLI functions
# ---------------------

def list_employees():
    employees = Employee.get_all()
    for emp in employees:
        print(emp)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employees = Employee.get_all()
    found = [e for e in employees if e.name == name]
    if found:
        for e in found:
            print(e)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    emp = Employee.find_by_id(id_)
    if emp:
        print(emp)
    else:
        print(f"Employee {id_} not found")


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    dept_id = input("Enter the employee's department id:")
    try:
        emp = Employee.create(name, job_title, int(dept_id))
        print(f"Success: {emp}")
    except Exception as e:
        print("Error creating employee: ", e)


def update_employee():
    id_ = input("Enter the employee's id: ")
    emp = Employee.find_by_id(id_)
    if not emp:
        print(f"Employee {id_} not found")
        return
    try:
        new_name = input("Enter the employees's new name: ")
        emp.name = new_name
        new_title = input("Enter the employee's new job title: ")
        emp.job_title = new_title
        new_dept = input("Enter the employees's new department id: ")
        emp.department_id = int(new_dept)

        emp.update()
        print(f"Success: {emp}")
    except Exception as e:
        print("Error updating employee: ", e)


def delete_employee():
    id_ = input("Enter the employee's id: ")
    emp = Employee.find_by_id(id_)
    if not emp:
        print(f"Employee {id_} not found")
        return
    emp.delete()
    print(f"Employee {id_} deleted")


def list_department_employees():
    dept_id = input("Enter the department's id: ")
    dept = Department.find_by_id(dept_id)
    if not dept:
        print(f"Department {dept_id} not found")
        return
    for emp in dept.employees():
        print(emp)
