# $fieldtype->emptyPageFieldTable(Page $page, Field $field): bool

Source: `wire/core/Fieldtype.php`

Empty DB table of page field

## Usage

~~~~~
// basic usage
$bool = $fieldtype->emptyPageFieldTable($page, $field);

// usage with all arguments
$bool = $fieldtype->emptyPageFieldTable(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`

## Return value

- `bool`

## Exceptions

- `WireException`

## Since

3.0.189
