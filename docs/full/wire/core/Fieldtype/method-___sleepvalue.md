# $fieldtype->___sleepValue(Page $page, Field $field, $value): string|int|float|array

Source: `wire/core/Fieldtype.php`

Given an 'awake' value, as set by wakeupValue(), convert the value back to a basic type for storage in database.

In many cases, this may mean no change to the value, which is why the default here just returns the value.
But for values that are stored with pages as objects (for instance) this method would take that object
and convert it to an array, int or string (serialized or otherwise).

Returned value must be either an array, number, or string.

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `string|int|float|array|object`

## Return value

string|int|float|array

## See also

- [Fieldtype::wakeupValue()](method-___wakeupvalue.md)
