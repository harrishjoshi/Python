import pprint

message = "It was a bright cold day in April, and the clocks were stricking thirteen."
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)
