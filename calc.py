if self.filecontent == "":
  arg1 = self.extarg1
  arg2 = self.extarg2
  arg3 = self.extarg3
  self.pr(eval(f"{arg1}{arg2}{arg3}"))
else:
  self.pr(eval(self.filecontent))
