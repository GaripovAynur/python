#SearchPhoneNumber
"""Проверяет встречается ли телефонный номер \d{3}-\d{3}-\d{4}"""

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('МОй НОМЕР : 324-354-3581.')
print('Найденный телефонный номер: '  + mo.group())

