if self.extarg1 == "save":
  self.goto = self.actual_dir
elif self.extarg1 == "show":
  self.pr(self.goto)
elif self.extarg1 == "del":
  self.goto = ""
else:
  self.actual_dir = self.goto
