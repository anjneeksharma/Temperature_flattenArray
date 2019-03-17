class TempTracker:
    """Temperature Tracker"""

    def __init__(self):
        self.temps = [0] * 111
        self.num_temps = 0
        self.min = 111
        self.max = -1
        self.total = 0
        self.mean = None

    def insert(self, temp):
        if temp < 0 or temp > 110:
            raise Exception("Entered Temperature is not in range")
        self.temps[temp] += 1
        self.num_temps += 1
        if temp < self.min:
            self.min = temp
        if temp > self.max:
            self.max = temp
        self.total += temp
        self.mean = self.total / float(self.num_temps)

    def get_max(self):
        max = self.max
        if max == -1:
            max = None
        return max

    def get_min(self):
        min = self.min
        if min == 111:
            min = None
        return min

    def get_mean(self):
        return self.mean


# creating object of tempure class
tempObj = TempTracker()

# inserting tempure 10 and 5
tempObj.insert(10)
tempObj.insert(5)
print("Max Temperature = %s" % (tempObj.get_max()))
print("Min Temperature = %s" % (tempObj.get_min()))
print("Mean Temperature = %s" % (tempObj.get_mean()))
