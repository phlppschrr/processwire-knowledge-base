# $fieldtype->getBlankValue(Page $page, Field $field): string|int|object|null

Source: `wire/core/Fieldtype.php`

Return the blank value for this fieldtype, whether that is a blank string, zero value, blank object or array

Default/non-implemented behavior is to return a blanks string.

## Usage

~~~~~
// basic usage
$string = $fieldtype->getBlankValue($page, $field);

// usage with all arguments
$string = $fieldtype->getBlankValue(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page|NullPage`
- `$field` `Field`

## Return value

- `string|int|object|null`
