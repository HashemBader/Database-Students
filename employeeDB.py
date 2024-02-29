import csv
import copy
import datetime as dt

from employee import Employee
from department import Department


class EmployeeDB(object):
    #This code initialize the file, employee dictionary and employee_object_list
    def __init__(self, file_name):
        self.__file = file_name
        self.__emp_dic = {}
        self.__emp_obj_list = []
    #This code reads the file and get the informations and put them in the dictionary, it makes the SNO the keys
    # and the information related to it the values
    #After observing everything from the file it prints how many records added to the dictionary
    def read_file(self):
        with open(self.__file, "r") as f:
            for line in f:
                clear = line.rstrip().split(",")
                keys = clear[0]
                if keys == 'SNo':
                    continue
                values = clear[1:]
                self.__emp_dic[keys] = values
        print(f"{len(self.__emp_dic)} records added to the dictionary")
    #This code gets the employee_object_list
    def get_obj_lst(self):
        return self.__emp_obj_list
    #This code checks if the employee_object is in the employee_object_list, if it is in the list it will return the
    # index of the employee object, if it is not in the list it will return -1
    def emp_exists(self, emp_obj):
        for index in range(len(self.__emp_obj_list)):
            if emp_obj.get_fName() == self.__emp_obj_list[index].get_fName() and emp_obj.get_lName() == self.__emp_obj_list[index].get_lName():
                return index
        return -1
    #This code will add the unique employee and his departments in the employee_object_list if it doesn't exist in the list
    #In the end it prints how many unique employees were added
    def add_emp_data(self):
        for SNO in self.__emp_dic:
            emp = Employee(self.__emp_dic[SNO][0], self.__emp_dic[SNO][1])
            if self.emp_exists(emp) == -1:
                dep = Department(self.__emp_dic[SNO][2], self.__emp_dic[SNO][3])
                emp.add_dept(dep)
                self.__emp_obj_list.append(emp)
            else:
                Employee.decrementEmpID()
                index = self.emp_exists(emp)
                dep = Department(self.__emp_dic[SNO][2], self.__emp_dic[SNO][3])
                self.__emp_obj_list[index].add_dept(dep)
        print(f"{len(self.__emp_obj_list)} unique employees added to the database.")
    #This code will print the employees who have more than 1 department and print how many were found and their details
    def print_cross_emp(self):
        count = 1
        for emp_obj in self.get_obj_lst():
            if len(emp_obj.get_depLst()) > 1:
                print(f"Record {count} found!")
                print(emp_obj)
                print(f"Appointments found:")
                dep_lis = emp_obj.get_depLst()
                count += 1
                for dep_obj in dep_lis:
                    print(dep_obj)
    #This code receives an employee id and removes it if it exist in the list
    def remove_emp(self, emp_id):
        for emp_obj in self.get_obj_lst():
            empID = emp_obj.get_emp_id()
            if empID == emp_id:
                self.__emp_obj_list.remove(emp_obj)
                print(f"Successfully removed employee with employee id: {emp_id}")
                return
        else:
            print("Employee not found!")
    #This code receives an employee id and check if it has more than 1 department, if it has more than 1 it will take
    # the difference of the first date of joining and the last date then print the difference in days
    def date_diff(self, emp_id):
        for emp_obj in self.get_obj_lst():
            if emp_obj.get_emp_id() == emp_id:
                if len(emp_obj.get_depLst()) > 1:
                    dep_lis = emp_obj.get_depLst()
                    date_lis = []
                    for dep_obj in dep_lis:
                        date = dep_obj.get_join_date()
                        clear = date.split("-")
                        adate = dt.datetime(year= int(clear[0]), month= int(clear[1]), day= int(clear[2]))
                        date_lis.append(adate)
                    new_date_list = sorted(date_lis)
                    max = new_date_list[-1]
                    min = new_date_list[0]
                    difference = max - min
                    result = difference.days
                    print(f"Difference between cross-appointments (in days) is: {result}")
                else:
                    print("Employee is not cross-appointed.")


def main():
    comp = EmployeeDB("employeeInfo.csv")
    print("******************************************************************************")
    comp.read_file()
    print("******************************************************************************")
    comp.add_emp_data()
    print("******************************************************************************")
    comp.print_cross_emp()
    print("******************************************************************************")
    str_id = input(f"Enter an EMP ID to be removed from the available {len(comp.get_obj_lst())} records: ")
    comp.remove_emp(str_id)
    print(f"Total employee objects remaining in the list are: {len(comp.get_obj_lst())}")
    print("******************************************************************************")
    str_id = input(f"Enter an EMP ID to compute days between cross-appointments: ")
    comp.date_diff(str_id)
    print("******************************************************************************")


if __name__ == "__main__":
    main()
