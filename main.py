import math
import sys
from os import rename

import requests


r = requests.get("https://github.com/Sweept")
print(r.status_code)
print(r.ok)
print("test")
