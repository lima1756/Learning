from os import system, listdir
#class Athlete:
    #def __init__(self,a_name,a_dob=None,a_times=[]):
    #    self.name=a_name
   #     self.dob=a_times
  #      self.times=a_times
 #   def top3(self):
#        return (sorted(set([sanitize(t) for t in self.times]))[0:3])
#    def add_item(self, time):
     #   self.times.append(time)
    #def add_items(self, times=[]):
        #self.times.extend(times)
class Athletelist(list):
    def __init__(self,a_name,a_dob=None):
        self.name=a_name
        self.dob=a_dob
    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])
    def add_item(self, time):
        self.append(time)
    def add_items(self, times=[]):
        self.extend(times)
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
            regresar = Athletelist(templ.pop(0), templ.pop(0))
            regresar.add_items(templ)
            return (regresar)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
    return(None)
sarah = get_coach_data("sarah2.txt")
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
sarah.add_item('1.11')
sarah.add_items(['1.16','2.15'])
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))