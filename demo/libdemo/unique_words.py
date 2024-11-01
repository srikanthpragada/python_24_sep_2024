data = """
We’re hearing more now from locals in eastern Spain, who are attempting to return to normality as the clean-up operation continues.
“We have to get up in any way we can,” Rafael Lopez, a resident of Picanya, says.
“Right now I'm going to work by foot as there's no other way to get there, I need to walk 5km to get to work. It's a disaster, a disaster, everywhere."
He adds: "We haven't been through the worst part yet. Nothing can come through, no food, nothing. The only thing that comes are the rescue trucks that can maybe bring a bit of food, but you need to walk 15 to 20 km to buy some bread."
"""

import re

words = re.findall(r"[a-zA-Z]+", data)

for w in sorted(set(words)):
    print(w)

