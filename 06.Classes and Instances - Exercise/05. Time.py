class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours, minutes, seconds):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds >= self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours >= self.max_hours:
                    self.hours = 0

        return self.get_time()

"""
-	set_time(hours, minutes, seconds) - update the time
-	get_time() - returns "{hh}:{mm}:{ss}"
-	next_second() - update the time with one second (use the class attributes for validation) and return the new time (using the get_time() method)
"""

time = Time(9, 30, 60)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(24, 59, 59)
print(time.next_second())


"""
09:31:00
11:00:00
01:00:00
"""
