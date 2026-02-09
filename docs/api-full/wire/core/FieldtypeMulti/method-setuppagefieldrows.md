# $fieldtypeMulti->setupPageFieldRows(Page $page, Field $field, $value): WireArray

Source: `wire/core/FieldtypeMulti.php`

Prepare rows for save or delete

## Usage

~~~~~
// basic usage
$items = $fieldtypeMulti->setupPageFieldRows($page, $field, $value);

// usage with all arguments
$items = $fieldtypeMulti->setupPageFieldRows(Page $page, Field $field, $value);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- $value

## Return value

- `WireArray`

## Exceptions

- `WireException`
