import pandas as pd
import re

# Regex pattern to split on commas that are not enclosed by quotes
# Explanation:
# r',             # Matches a comma
# (?=             # Start of a positive lookahead assertion
#    (?:          # Start of a non-capturing group
#       [^"]*"    # Match any number of non-quote characters followed by a quote
#       [^"]*"    # Match another set of any number of non-quote characters followed by a quote
#    )*           # End of the non-capturing group, repeated any number of times
#    [^"]*$       # Match any number of non-quote characters until the end of the line
# )'              # End of the lookahead assertion
regex_pattern = r',(?=(?:[^"]*"[^"]*")*[^"]*$)'
