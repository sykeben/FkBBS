from bbstxt import output as out
import bbstxt
from time import sleep
import easygui as eg


def pause(**opt):
    if "m" in opt:
        sleep(0.25*opt["m"])
    else:
        sleep(0.25)


print("Waiting for user to configure . . .")

use_defaults = eg.ynbox("Would you like to use the default configuration?", "Use defaults?")
if use_defaults:
    bbstxt.baud = 9600
    alias = "guest"
    user_code = ""
else:
    bbstxt.baud = eg.integerbox("Enter baud rate (Default: 9600)", "Configure (1/3): Baud", 9600, 1, 120000000)
    alias = eg.enterbox("Enter your alias (Default: guest)", "Configure (2/3): Alias", "guest")
    user_code = eg.passwordbox("Enter your user-code (Default: [None])", "Configure (3/3): User-Code")

print("Connecting to basic.fkbbs.net (800-135-9521) . . .")
sleep(3)
print("SUCCESS!")
print("")

pause()

out("Welcome to FKBBS-BASIC!")
out("Verifying your information:")
pause()
out("- Alias")
pause()
out("- Usercode")

sleep(1)

print("")
out("Welcome, {0}!".format(alias.upper()))
out("""  _____ _    ____  ____ ____
 |  ___| | _| __ )| __ ) ___|     ___           _
 | |_  | |/ /  _ \\|  _ \\___ \\    / _ )___ ____ (_)___
 |  _| |   <| |_) | |_) |__) |  / _  / _ `(_-</ / __/
 |_|   |_|\_\____/|____/____/  /____/\_,_/___/_/\__/""")

sleep(3)