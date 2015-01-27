import datetime

class Task:
	def __init__(self, name = datetime.date.today(), due = datetime.date.today() + one_day, rep = 0, desc = "", sub = None, stat = 0, dur = 0.5):
		self.name = name
		# Default task name vaule is today's date.
		self.due = due
		# Default due date is tomorrow
		self.rep = rep
		# The repeat vaule will be stored as an integer.
		# The event will repeat after this number of days.
		self.description = desc
		# A description of the task.
		self.subtask = sub
		# Any sub-tasks that make up this task.  These values will be stored as a Task object.
		self.status = stat
		# The status of the task as a percentage. Incomplete tasks are 0%, and complete tasks are 100%.
		self.duration = dur
		# The value of duration can be stored as any time unit. 
		# As default, it is stored in hours, and defaults to 0.5 hours.
	def getName(self):
		return(self.name)
	def setName(self, n):
		self.name = n
	def getDue(self):
		return(self.due)
	def setDue(self, d):
		self.name = n
	def getRep(self):
		return(self.rep)
	def setRep(self, r):
		self.rep = r
	def getDesc(self):
		return(self.description)
	def setDesc(self, ds):
		self.description = ds
	def getSub(self):
		return(self.subtask)
	def setSub(self, s):
		self.subtask = s
	def getStat(self):
		return(self.status)
	def setStat(self, st):
		self.status = st
	def getDur(self):
		return(self.duration)
	def setDur(self, dr):
		self.duration = dr
		
