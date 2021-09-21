import sys

import utils

if len(sys.argv) > 1:
    code = sys.argv[1]
else:
    code = 'Eur'

print(utils.currency_rates(code))
