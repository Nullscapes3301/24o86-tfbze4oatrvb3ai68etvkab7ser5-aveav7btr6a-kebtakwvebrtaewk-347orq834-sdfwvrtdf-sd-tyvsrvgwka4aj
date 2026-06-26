olddir = self.actual_dir
self.actual_dir = "putOS/system.dir/"
self.execute_command("show file history.data")
self.actual_dir = olddir
