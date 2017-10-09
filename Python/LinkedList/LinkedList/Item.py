class Item:
    """ Item for LinkedList """
    __value = 0;
    __next = None;
    __last = None;

    def __init__(self):
        __value = 0;
        __next = None;
        __last = None;
    
    def __init__(self, value):
        self.__value = value;
        __next = None;
        __last = None;
    

    def __str__(self):
        return str(self.__value)

    def getValue(self):
        return self.__value;

    def getNext(self):
        return self.__next;

    def getLast(self):
        return self.__last

    def setValue(self, value):
        self.__value = value

    def setNext(self, next):
        self.__next = next

    def setLast(self, last):
        self.__last = last;

    def move(self, direction):
        if(direction == True):
            return self.__next;
        else:
            return self.__last;

