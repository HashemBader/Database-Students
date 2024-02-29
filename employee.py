class Employee(object):
    #This code initialize employee id
    emID = 0
    #This code gets the employee id in this form "EMPxxxx" which xxxx is the id number
    @staticmethod
    def getNextEmpID():
        Employee.emID += 1
        if len(str(Employee.emID)) == 1:
            emp_id = "EMP000"+ str(Employee.emID)
        if len(str(Employee.emID)) == 2:
            emp_id = "EMP00" + str(Employee.emID)
        if len(str(Employee.emID)) == 3:
            emp_id = "EMP0" + str(Employee.emID)
        if len(str(Employee.emID)) == 4:
            emp_id = "EMP" + str(Employee.emID)
        return emp_id
    #This code decrement employee id by 1
    @staticmethod
    def decrementEmpID():
        Employee.emID -= 1
    #This code initialize employee first name, employee last name, employee id and department list
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__empID = self.getNextEmpID()
        self.__deplist = []
    #This code gets employee id
    def get_emp_id(self):
        return self.__empID
    # This code gets employee first name
    def get_fName(self):
        return self.__first_name
    # This code gets employee last name
    def get_lName(self):
        return self.__last_name
    # This code gets department list
    def get_depLst(self):
        return self.__deplist
    # This code sets employee first name by recieving first name and make it the employee first name
    def set_fName(self, first_name):
        self.__first_name = first_name
    # This code sets employee last name by recieving last name and make it the employee last name
    def set_lName(self, last_name):
        self.__last_name = last_name
    #This code add a department in the department list
    def add_dept(self, dep):
        self.__deplist.append(dep)
    #This code prints employee id, employee first name, employee last name and number of departments the employee has
    def __str__(self):
        return f"EmpID:{self.get_emp_id()}; FirstName:{self.get_fName()}; LastName:{self.get_lName()}; NumberOfDepts:{len(self.get_depLst())} "
