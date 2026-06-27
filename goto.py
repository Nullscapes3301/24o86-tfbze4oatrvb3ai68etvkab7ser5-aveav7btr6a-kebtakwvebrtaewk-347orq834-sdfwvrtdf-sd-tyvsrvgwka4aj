if self.extarg1 == "save":
  self.goto = self.actual_dir
  self.pr("Route saved")
elif self.extarg1 == "show":
  try:
    self.pr(self.goto)
  except:
    self.pr("No route saved")
elif self.extarg1 == "del":
  self.goto = ""
  self.pr("Route deleted")
else:
  try:
    if self.goto == "":
      self.pr("No route saved")
    else:
      self.actual_dir = self.goto
  except:
    self.pr("No route saved")
