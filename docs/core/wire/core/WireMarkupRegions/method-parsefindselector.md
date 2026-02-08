# WireMarkupRegions::parseFindSelector()

Source: `wire/core/WireMarkupRegions.php`

Given a $find selector return array with tests and other meta info

@param string $find

@return array Returns array of [
  'tests' => [ 0 => '', 1 => '', ...],
  'find' => '',
  'findTag' => '',
  'hasClass' => '',
]
