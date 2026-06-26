while True:
  if self.login():
    break
  else:
    self.pr("Login error")
