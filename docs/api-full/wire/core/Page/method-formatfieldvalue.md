# $page->formatFieldValue(Field $field, $value): mixed

Source: `wire/core/Page.php`

Return a value consistent with the page’s output formatting state

This is primarily for use as a helper to the getFieldValue() method.

## Usage

~~~~~
// basic usage
$result = $page->formatFieldValue($field, $value);

// usage with all arguments
$result = $page->formatFieldValue(Field $field, $value);
~~~~~

## Arguments

- `$field` `Field`
- `$value` `mixed`

## Return value

- `mixed`
