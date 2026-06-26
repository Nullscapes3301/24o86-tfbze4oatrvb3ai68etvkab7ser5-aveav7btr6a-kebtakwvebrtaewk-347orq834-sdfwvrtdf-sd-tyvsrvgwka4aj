while True:
  prompt=self.inp("WiFi > ")
  prompt=prompt.split(" ")
  if prompt[0] == "show":
    self.execute_command("wifi scan")
  if prompt[0] == "on":
    self.execute_command("wifi connect")
  if prompt[0] == "inf":
    self.execute_command("wifi info")
  if prompt[0] == "off":
    self.execute_command("wifi disconnect")
