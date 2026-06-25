if self.filecontent == "":
  arg1 = self.extarg1
  arg2 = self.extarg2
  arg3 = self.extarg3
  print(eval(f"{arg1}{arg2}{arg3}"))
else:
  print(eval(self.filecontent))
