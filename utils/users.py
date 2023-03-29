class Person:
    def __init__(self):
        self.__height = 182
        self.__weight = 78
    def get_cm_height(self):
        return self.__height 
    def get_m_height(self):
        return self.__height / 100