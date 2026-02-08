# Selectors::extractValue()

Source: `wire/core/Selectors.php`

Given a string starting with a value, return that value, and remove it from $str.

@param string $str String to extract value from

@param string $quote Automatically populated with quote type, if found

@return array|string Found values or value (excluding quotes)
