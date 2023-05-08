import datetime


class Project:
     def __int__(self, name="", start_date="", priority=int, cost=float, completion=int):
         self.name = name
         self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%y").date()
         self.priority = priority
         self.cost = cost
         self.completion = completion

     def __str__(self):
         return f"{self.name}, {self.start_date}, {self.priority}, {self.cost:,.2f}, {self.completion}"

     def __repr__(self):
         return f"{self.name}, {self.start_date}, {self.priority}, {self.cost:,.2f}, {self.completion}"

     def is_complete(self):
         return int(self.completion) == 100

     def __it__(self, other):
         return self.priority <= other.priority

     def compare_date(self, input_date):
         input_date = datetime.datetime.strptime(input_date, "%d/%m/%y").date()
         return self.start_date >= input_date

     def undate_percentage(self, value):
         self.completion = value

     def update_priority(self, value):
         self.priority = value


