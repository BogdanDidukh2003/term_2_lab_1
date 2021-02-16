class Teacher:

    university = "NULP"
  
    @staticmethod
    def display_output_of_greeting():
        print("Welcome to ", Teacher.university)
        return Teacher.university

    def __init__(self, name_surname, age, gender, experience, alias, subject):
        self.__name_surname = name_surname
        self.__experience = experience
        self.__alias = alias
        self.__subject = subject
        self.__age = age
        self.__gender = gender

    def __str__(self) -> str:
        return ("Teacher " + (self.__name_surname) + " is " + str(self.__age) + " years old " + 
        (self.__gender) + ", teaches " + (self.__subject) + " in " + (Teacher.university) + " and has " + 
        str(self.__experience) + " years of experience. Students call him " + (self.__alias)+ ".")

    def __del__(self):
        pass
    
    