try:
    print("Mamba version 1.7 (Canary build)")
    print("Mamba is loading modules...")
    import requests
    import random
    import time

    print("Mamba finished loading modules, now loading Mamba's libraries into the Python process.")

    def loop(times, loopcode):
        mambaloopobject = 0
        for mambaloopobject in range(times):
            exec(loopcode)

    def get(url, plaintext, var):
        if plaintext:
            mambagetobj = requests.get(url)
            eval(var + " = mambagetobj.text")
        else:
            eval(var + " = requests.get(url)")
except BaseException as error:
    print("An error occured in the Mamba runtime. Error: " + str(error) + " (In Python form, not Mamba form.)")
    raise RuntimeError("Mamba error occured.")
