# $fieldtypeMulti->___sleepValue(Page $page, Field $field, $value): array

Source: `wire/core/FieldtypeMulti.php`

Given an 'awake' value, as set by wakeupValue, convert the value back to a basic type for storage in DB.

FieldtypeMulti::savePageField expects values as an array, so we convert the $value object to an array

Note that FieldtypeMulti is designed around potentially supporting more than just the 'data' field in
the table, so other fieldtypes may want to override this and return an array of associative arrays containing a 'data' field
and any other fields that map to the table. i.e. $values[] = array('data' => $data, 'description' => $description), etc.
See FieldtypePagefiles module class for an example of this.

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `WireArray`

## Return value

array
