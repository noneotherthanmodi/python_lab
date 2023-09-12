class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def update_salary_by_department(self, department, percent_increase):
        if self.department == department:
            self.salary *= (1 + percent_increase / 100)

no_of_employees=int(input('enter the number of employee detatils required'))
employees=[]
# Print updated salaries
#for employee in employees:
#    print(employee.name, employee.salary)
for i in range(no_of_employees):
    print("enter",i,'th','employee details')
    print("employee name")
    name=input()
    print("employee id")
    id=input()
    print("employee dept")
    dept=input()
    print("employee salary")
    sal=int(input())
    employees.append(Employee(name,id,dept,sal))
print('EmpName\t EmpId\t EmpDept\t EmpSalary\n')
for emp in employees:
    print(emp.name,'\t',emp.employee_id,'\t',emp.department,'\t',emp.salary,'\n')
dept=input('enter the department to update the salary')
# Increase salaries of Sales department employees by 10%
for employee in employees:
    if employee.department==dept:
           employee.update_salary_by_department(dept, 10)

for employee in employees:
    print(employee.name, employee.salary)
