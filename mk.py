name = self.extarg1
current = self.get_current()
if "/" in name:
  self.pr("Invalid name. Please use a valid name without '/'")
if " " in name:
  self.pr("Invalid name. Please use a valid name without spaces.")
if name == "":
  self.pr("Invalid name. Please use a valid name without spaces.")
elif name in current:
  self.pr("Already exists")
elif name.endswith(".dir"):
  current[name] = {}
else:
  self.file_content = ""
  current[name] = self.file_content
