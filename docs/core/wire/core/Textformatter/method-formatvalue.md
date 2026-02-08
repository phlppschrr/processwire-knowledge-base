# $textformatter->formatValue(Page $page, Field $field, &$value)

Source: `wire/core/Textformatter.php`

Format the given text string with Page and Field provided.

Module developers may override this function completely when providing your own text formatter. No need to call the parent.

## Usage

~~~~~
// basic usage
$result = $textformatter->formatValue($page, $field, $value);

// usage with all arguments
$result = $textformatter->formatValue(Page $page, Field $field, &$value);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `string|mixed` Value is provided as a reference, so is modified directly (not returned).
