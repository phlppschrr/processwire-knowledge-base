# $fieldtypeMulti->wakeupValue(Page $page, Field $field, $value): WireArray

Source: `wire/core/FieldtypeMulti.php`

Process the value to convert it from array to whatever object it needs to be

## Usage

~~~~~
// basic usage
$items = $fieldtypeMulti->wakeupValue($page, $field, $value);

// usage with all arguments
$items = $fieldtypeMulti->wakeupValue(Page $page, Field $field, $value);
~~~~~

## Hookable

- Hookable method name: `wakeupValue`
- Implementation: `___wakeupValue`
- Hook with: `$fieldtypeMulti->wakeupValue()`

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `array`

## Return value

- `WireArray`
