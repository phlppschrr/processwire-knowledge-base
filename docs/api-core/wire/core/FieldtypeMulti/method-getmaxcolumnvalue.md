# $fieldtypeMulti->getMaxColumnValue(Page $page, Field $field, $column, $noValue = false): int|bool|mixed

Source: `wire/core/FieldtypeMulti.php`

Get max value of column for given Page and Field or boolean false (or specified $noValue) if no rows present

## Usage

~~~~~
// basic usage
$int = $fieldtypeMulti->getMaxColumnValue($page, $field, $column);

// usage with all arguments
$int = $fieldtypeMulti->getMaxColumnValue(Page $page, Field $field, $column, $noValue = false);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$column` `string`
- `$noValue` (optional) `int|bool` Return this value if there are no rows to count from (default=false)

## Return value

- `int|bool|mixed`

## Exceptions

- `WireException`

## Since

3.0.154
