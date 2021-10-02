import os
import time

if input("Should we add the Cobra REPL to path? (Only avalable on Windows) (Y/n)") == "n"
  print("Okay, procceding.")
  exit()
 else:
  print("Adding Cobra REPL to Windows PATH...")
  addpath1 = time.time()
  os.system('Start-Process "cmd.exe /c mkdir C:\cobra && setx /M path "%path%;C:\cobra" && move repl.exe C:\cobra\repl.exe" -Verb RunAs')
  addpath2 = time.time()
  print("Operation completed in " + addpath2 - addpath1 + " seconds.")
