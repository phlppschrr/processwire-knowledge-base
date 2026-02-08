# $fieldtypeMulti->getMaxColumnValue(Page $page, Field $field, $column, $noValue = false): int|bool|mixed

Source: `wire/core/FieldtypeMulti.php`

Get max value of column for given Page and Field or boolean false (or specified $noValue) if no rows present

## Arguments

- Page $page
- Field $field
- string $column
- int|bool $noValue Return this value if there are no rows to count from (default=false)

## Return value

int|bool|mixed

## Throws

- WireException

## Meta

- @since 3.0.154
