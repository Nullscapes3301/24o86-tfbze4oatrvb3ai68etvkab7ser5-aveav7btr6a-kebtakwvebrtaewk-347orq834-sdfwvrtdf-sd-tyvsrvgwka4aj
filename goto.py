if self.extarg1 == "save":
  self.goto = self.actual_dir
  self.pr("Route saved")
elif self.extarg1 == "show":
  self.pr(self.goto)
elif self.extarg1 == "del":
  self.pr("Route deleted")
else:
  if not self.goto == "":
    self.actual_dir = self.goto
