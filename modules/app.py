from ecommerce.sales import calc_shipping

from ecommerce.shopping import sales2

sales2.calc_tax()

calc_shipping()
import sys

# print(dir(sales2))
# print(sys.path)

# module name
print(sales2.__name__)
# package name
print(sales2.__package__)
print(sales2.__file__)
