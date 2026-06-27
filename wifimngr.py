import pywifi
    from pywifi import const
    import time
    wifi = pywifi.PyWiFi()
    if len(wifi.interfaces()) == 0:
        self.pr("No WiFi adapter found")
        return
    iface = wifi.interfaces()[0]
    if hasattr(self, "wifidata") and self.wifidata:
      pass
    else:
      self.wifidata = {}
    self.pr("putOS WiFi EZ manager")
    while True:
      prompt=self.inp("WiFi > ")
      prompt=prompt.split(" ")
      if prompt[0] == "show":
        self.execute_command("wifi scan")
      elif prompt[0] == "on":
        inx=self.inp("WiFi connect > ")
        if inx == "yx":
          for i in self.wifidata:
            self.pr(f"[WiFi] {i}")
          dic = self.inp("WiFi connect choose > ")
          if dic in self.wifidata:
            ssid = self.wifidata[dic]["ssid"]
            password = self.wifidata[dic]["password"]
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password
            iface.disconnect()
            time.sleep(1)
            tmp = iface.add_network_profile(profile)
            self.pr("Connecting...")
            iface.connect(tmp)
            for _ in range(10):
                if iface.status() == const.IFACE_CONNECTED:
                    self.pr("Connected")
                    break
                time.sleep(1)
            else:
                self.pr("Connection failed")
        elif inx == "nx":
          ssid = self.inp("WiFi SSID: ")
          password = self.inp("WiFi password: ")
          profile = pywifi.Profile()
          profile.ssid = ssid
          profile.auth = const.AUTH_ALG_OPEN
          profile.akm.append(const.AKM_TYPE_WPA2PSK)
          profile.cipher = const.CIPHER_TYPE_CCMP
          profile.key = password
          iface.disconnect()
          time.sleep(1)
          tmp = iface.add_network_profile(profile)
          self.pr("Connecting...")
          iface.connect(tmp)
          for _ in range(10):
              if iface.status() == const.IFACE_CONNECTED:
                  self.pr("Connected")
                  self.wifidata[ssid] = {
                    "ssid": ssid,
                    "password": password
                  }
                  break
              time.sleep(1)
          else:
              self.pr("Connection failed")
        else:
          self.pr("WiFi")
          self.pr("└── connect")
          self.pr("    ├── yx ── Search in wifidata")
          self.pr("    └── nx ── Create a new entry in wifidata")
          self.pr()
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
