class Department(object):
    #This code initialize department_id and department_dictionary
    dpID = 0
    dpDict = {}
    #This code get the next department id
    @staticmethod
    def getNextDepID():
        Department.dpID += 1
        return Department.dpID
    #This code initialize the department name, department date and department id
    def __init__(self, name, date):
        self.__depname = name
        self.__depdate = date
        self.__depid = 0
        #This code gives every department name an id and insert them in dictionary which the key is the department_id and the value is the department name
        if self.__depname not in self.dpDict.values():
            self.dpDict[self.getNextDepID()] = self.__depname
        if self.__depname in self.dpDict.values():
            for id in self.dpDict:
                if self.dpDict[id] == self.__depname:
                    self.__depid = id
    #This code gets the department id
    def get_dep_id(self):
        return self.__depid
    #This code gets the department name
    def get_dep_name(self):
        return self.__depname
    #This code gets the joining date
    def get_join_date(self):
        return self.__depdate
    #This code prints the department_id, department_name and joining date
    def __str__(self):
        return f"DepartmentID:{self.get_dep_id()}; DepartmentName:{self.get_dep_name()}; JoiningDate:{self.get_join_date()};"

