# $fieldtype->sanitizeValue(Page $page, Field $field, $value): string|int|WireArray|object

Source: `wire/core/Fieldtype.php`

Sanitize the value for runtime storage and return it.

- Implementation is required by Fieldtype modules, as this method is abstract.
- This method should remove anything that's invalid from the given value. If it can't be sanitized, it should be made blank.
- This method filters every value set to a Page instance, so it should do it's thing as quickly as possible.

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `string|int|WireArray|object`

## Return value

string|int|WireArray|object
