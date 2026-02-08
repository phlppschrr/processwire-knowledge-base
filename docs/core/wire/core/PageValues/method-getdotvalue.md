# $pageValues->getDotValue(Page $page, $key): mixed|null

Source: `wire/core/PageValues.php`

Given a 'field.subfield' type string traverse properties and return value

## Usage

~~~~~
// basic usage
$result = $pageValues->getDotValue($page, $key);

// usage with all arguments
$result = $pageValues->getDotValue(Page $page, $key);
~~~~~

## Arguments

- `$page` `Page`
- `$key` `string`

## Return value

- `mixed|null`
