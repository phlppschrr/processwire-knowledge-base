# $textformatter->formatValue(Page $page, Field $field, &$value)

Source: `wire/core/Textformatter.php`

Format the given text string with Page and Field provided.

Module developers may override this function completely when providing your own text formatter. No need to call the parent.

## Arguments

- Page $page
- Field $field
- string|mixed $value Value is provided as a reference, so is modified directly (not returned).
