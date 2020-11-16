# Some examples of objects and methods.

class Time(object):
    """ Represents a time """
    
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)) 

    def __add__(self, other):
        if isinstance(other, Time):
            return(self.add_time(other))
        else:
            return(self.increment(other))
        
    def __radd__(self, other):
        return(self.__add__(other))

    def add_time(self, other):
        seconds = self.time2int() + other.time2int()
        return(int2time(seconds))
    
    def print_time(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))
    
    def time2int(self):
        """ Converts a Time object to an integer representing the total
            amount of seconds that the Time object represents 
            Arguments: self - Time object """
            
        hours = self.hour
        minutes = self.minute
        seconds = self.second
        
        return(hours*3600 + minutes*60 + seconds)
    
    def increment(self, seconds, minutes=0, hours=0):
        inc_secs = self.time2int()
        inc_secs += 3600*hours + 60*minutes + seconds
        
        return(int2time(inc_secs))
    
    def is_after(self, other):
        return(self.time2int() > other.time2int())
        
def int2time(seconds):
    """ Takes an integer and returns the Time object representing that amount
        of settings """
    time = Time()
    time.hour, minutes = divmod(seconds, 3600)
    time.minute, time.second = divmod(minutes, 60)
    return(time) 

class Point(object):
    """ Represents a point in 2 dimensional Euclidean space"""
    
    def __init__(self, xord=0, yord=0):
        self.x = xord
        self.y = yord
        
    def __add__(self, other):
        if isinstance(other, Point):
            return(self.add_point(other))
        else:
            return(Point(self.x + other[0], self.y + other[1]))
        
    def add_point(self, other):
        return(Point(self.x + other.x, self.y + other.y))
    
    def __radd__(self, other):
        return(self.__add__(other))
        
    def __str__(self):
        return('(%g,%g)' % (self.x, self.y))
        
    def print_point(self):
        print("(%g,%g)" % (self.x, self.y))




