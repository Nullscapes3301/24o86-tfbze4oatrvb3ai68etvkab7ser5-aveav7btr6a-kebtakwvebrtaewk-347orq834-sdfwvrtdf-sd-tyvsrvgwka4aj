if self.actual_dir.startswith("putOS/home.dir/"):
  pass
else:
  self.pr("Acces denied.")
def tree(node, prefix=""):
    items = list(node.items())

    for i, (name, value) in enumerate(items):
        last = i == len(items) - 1
        branch = "└── " if last else "├── "

        self.pr(prefix + branch + name)

        if isinstance(value, dict):
            tree(value, prefix + ("    " if last else "│   "))

tree(self.files)
