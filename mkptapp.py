def code(arg):
    import base64
    return base64.b64encode(arg.encode()).decode()

if self.extarg1 == ".":
    i=self.inp("text > ")
    i = i.replace("\\n", "\n")
    self.pr("putOS app > ", f"PTAPP{code(code(code(i)))}")
else:
    current = self.get_current()
    i=self.inp("text > ")
    i = i.replace("\\n", "\n")
    current[self.extarg1] = f"PTAPP{code(code(code(i)))}"
