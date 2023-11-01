#!/usr/bin/env python3

import re

def renamer(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None: # This condition ends the edge case while testing.
        return name #return "", returns bug for single name edge case. fyi
    return "{} {}".format(result[2], result[1])
    
