# $selectors->extractValue(&$str, &$quote): array|string

Source: `wire/core/Selectors.php`

Given a string starting with a value, return that value, and remove it from $str.

## Arguments

- `$str` `string` String to extract value from
- `$quote` `string` Automatically populated with quote type, if found

## Return value

array|string Found values or value (excluding quotes)
