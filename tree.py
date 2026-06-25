if self.actual_dir.startswith("putOS/home.dir/"):
  pass
else:
  print("Acces denied.")
def run(self):
  def show(node, prefix=""):
      items = list(node.items())

      for i, (name, value) in enumerate(items):
          last = i == len(items) - 1
          branch = "└── " if last else "├── "

          print(prefix + branch + name)

          if isinstance(value, dict):
              show(
                  value,
                  prefix + ("    " if last else "│   ")
              )

  show(self.files)
run()
