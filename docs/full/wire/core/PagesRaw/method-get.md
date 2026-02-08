# $pagesRaw->get($selector, $field = '', $options = array()): array

Source: `wire/core/PagesRaw.php`

Get page (no exclusions) and return raw data from it in a PHP array

## Arguments

- `$selector` `string|array|Selectors`
- `$field` (optional) `string|Field|int|array` Field/property name to get or array of them (or omit to get all)
- `$options` (optional) `array|bool` See options for Pages::find - `objects` (bool): Use objects rather than associative arrays? (default=false) - `entities` (bool|array): Entity encode string values? True, or specify array of field names. (default=false) - `indexed` (bool): Index by page ID? (default=false) - `flat` (bool|string): Flatten return value as `["field.subfield" => "value"]` rather than `["field" => ["subfield" => "value"]]`? Optionally specify field delimiter, otherwise a period `.` will be used as the delimiter. (default=false) 3.0.193+

## Return value

array

## Since

3.0.172
