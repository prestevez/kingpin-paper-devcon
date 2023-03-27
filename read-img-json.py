#!/usr/bin/env python3

import json
import sys
firstarg=sys.argv[1]

# read file
with open(firstarg, 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# show values
print(obj.get('Env')[1]) # Returns R Version in semver format