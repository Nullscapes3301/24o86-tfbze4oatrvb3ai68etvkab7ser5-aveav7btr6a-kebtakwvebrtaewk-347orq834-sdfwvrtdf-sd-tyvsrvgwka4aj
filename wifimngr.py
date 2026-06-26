while True:
  self.pr("putOS WiFi EZ manager")
  prompt=self.inp("WiFi > ")
  prompt=prompt.split(" ")
  if prompt[0] == "show":
    self.execute_command("wifi scan")
  elif prompt[0] == "on":
    self.execute_command("wifi connect")
  elif prompt[0] == "inf":
    self.execute_command("wifi info")
  elif prompt[0] == "off":
    self.execute_command("wifi disconnect")
  elif prompt[0] == "":
    pass
  elif prompt[0] == "exit":
    break
  else:
    self.pr("Invalid command:", prompt[0])
