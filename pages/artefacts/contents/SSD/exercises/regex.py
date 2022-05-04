import re

class Solution:

  UK_POSTAL_CODE_PATTERN = r'^(((([A-Z]{1,2})[0-9])[A-Z])|(([A-Z])[0-9])|(([A-Z]{1,2})[0-9]{1,2})) ([0-9]([A-Z]{2}))$'

  def parse_uk_postal_code(self, postal_code):
    result = re.match(self.UK_POSTAL_CODE_PATTERN, postal_code)

    if result is None:
      return None

    if result.group(2) is not None:
      return {
        'isValid': True,
        'outwardCode': result.group(1),
        'inwardCode': result.group(9),
        'postcodeArea': result.group(4),
        'districtCode': result.group(3),
        'subDistrict': result.group(1),
        'unit': result.group(10),
      }
    elif result.group(5) is not None:
      return {
        'isValid': True,
        'outwardCode': result.group(1),
        'inwardCode': result.group(9),
        'postcodeArea': result.group(6),
        'districtCode': result.group(5),
        'subDistrict': None,
        'Unit': result.group(10),
      }
    else:
      return {
        'isValid': True,
        'outwardCode': result.group(1),
        'inwardCode': result.group(9),
        'postcodeArea': result.group(8),
        'districtCode': result.group(7),
        'subDistrict': None,
        'Unit': result.group(10),
      }

if __name__ == '__main__':
  postal_code_list = [
    'AA9A 9AA',
    'M60 1NW',
    'W1A 1HQ',
    'EC1A 1BB',
  ]
  actual_results = [Solution().parse_uk_postal_code(code) for code in postal_code_list]
  expected_results = [
    {'isValid': True, 'outwardCode': 'AA9A', 'inwardCode': '9AA', 'postcodeArea': 'AA', 'districtCode': 'AA9', 'subDistrict': 'AA9A', 'unit': 'AA'},
    {'isValid': True, 'outwardCode': 'M60', 'inwardCode': '1NW', 'postcodeArea': 'M', 'districtCode': 'M60', 'subDistrict': None, 'Unit': 'NW'},
    {'isValid': True, 'outwardCode': 'W1A', 'inwardCode': '1HQ', 'postcodeArea': 'W', 'districtCode': 'W1', 'subDistrict': 'W1A', 'unit': 'HQ'},
    {'isValid': True, 'outwardCode': 'EC1A', 'inwardCode': '1BB', 'postcodeArea': 'EC', 'districtCode': 'EC1', 'subDistrict': 'EC1A', 'unit': 'BB'},
  ]
  for i in range(len(postal_code_list)):
    actual_result = actual_results[i]
    expected_result = expected_results[i]
    assert actual_result == expected_result
    print(f'Case {i + 1}: Passed')
