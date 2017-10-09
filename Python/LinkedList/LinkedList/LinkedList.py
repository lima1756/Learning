from Item import Item

class LinkedList:
    """Double Linked List"""
    
    __start = None;
    __end = None;
    __count = 0;

    def __init__(self):
        __count = 0;
        __start = None;
        __end = None;

    def getStart(self):
        return __start

    def getEnd(self):
        return __end;

    def getCount(self):
        return __count;

    def addLast(self, item):
        if(self.__count == 0):
            self.__start = item;
            self.__start.setNext(self.__start);
            self.__start.setLast(self.__start);
            self.__end = self.__start
        else:
            self.__end.setNext(item);
            item.setLast(self.__end);
            item.setNext(self.__start);
            self.__end = item;
            self.__start.last = self.__end;

        self.__count += 1;
    
    def __str__(self):
        theString = ""
        now = self.__start;
        for x in range(0, self.__count-1):
            theString += str(now) + ", "
            now = now.getNext();   
        else:
            theString += str(now)
        return theString;

    def getItem(self, position):
        now = self.__start;
        direction = False;
        if (position >= 0):
            direction = True;    
        for x in range(0, position):
            now = now.move(direction)
        return now;
       
    def isEmpty(self):
        if(self.__count==0):
            return True;
        else:
            return False
   
    def removeItem(self, position):
        if(not self.isEmpty()):
            now = self.__start;
            direction = False;
            if (position >= 0):
                direction = True;    
            for x in range(0, position):
                now = now.move(direction)
            if(self.__count>1):
                now.getLast().setNext(now.getNext());
                now.getNext().setLast(now.getLast());
            else:
                self.__start = None;
                self.__end = None;
            self.__count -=1;
            return now;
        else:
            return None;
        

    def removeLast(self):
        ok = self.removeItem(self.__count-1);
        if(self.__end is not None):
            self.__end = self.__end.getLast();
        return ok;

    def removeStart(self):
        ok = self.removeItem(0);
        if(self.__start is not None):
            self.__start = self.__start.getNext();
        return ok;