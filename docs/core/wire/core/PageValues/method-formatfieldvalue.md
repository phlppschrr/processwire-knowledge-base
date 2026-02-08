# $pageValues->formatFieldValue(Page $page, Field $field, $value): mixed

Source: `wire/core/PageValues.php`

Return a value consistent with the page’s output formatting state

This is primarily for use as a helper to the getFieldValue() method.

## Usage

~~~~~
// basic usage
$result = $pageValues->formatFieldValue($page, $field, $value);

// usage with all arguments
$result = $pageValues->formatFieldValue(Page $page, Field $field, $value);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `mixed`

## Return value

- `mixed`
