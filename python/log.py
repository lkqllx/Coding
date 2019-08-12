import logging
import pdb
logging.basicConfig(level='DEBUG')


a = 3
b = 1
logging.info(f'a/b = {round(a/b, 2)}')
pdb.set_trace()
print(a/b)
