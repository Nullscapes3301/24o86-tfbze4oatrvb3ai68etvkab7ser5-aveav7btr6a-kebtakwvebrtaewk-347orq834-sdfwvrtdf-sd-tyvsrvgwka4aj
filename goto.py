if self.extarg1 == "save":
    self.goto = self.actual_dir
    self.pr("Route saved")

elif self.extarg1 == "show":
    if hasattr(self, "goto") and self.goto:
        self.pr(self.goto)
    else:
        self.pr("No route saved")

elif self.extarg1 == "del":
    self.goto = ""
    self.pr("Route deleted")

else:
    if hasattr(self, "goto") and self.goto:
        self.actual_dir = self.goto
    else:
        self.pr("No route saved")
