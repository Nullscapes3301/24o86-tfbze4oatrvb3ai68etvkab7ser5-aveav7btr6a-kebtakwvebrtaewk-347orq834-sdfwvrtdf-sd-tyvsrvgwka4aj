name = self.extarg1
current = self.get_current()
if " " in name:
  print("Invalid name. Please use a valid name without spaces.")
  return
if name == "":
  print("Invalid name. Please use a valid name without spaces.")
elif name in current:
  print("Already exists")
elif name.endswith(".dir"):
  current[name] = {}
else:
  self.file_content = ""
  current[name] = self.file_content
