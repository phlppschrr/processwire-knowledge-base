# $fieldtype->___emptyPageField(Page $page, Field $field): bool

Source: `wire/core/Fieldtype.php`

Empty out the DB table data for page field, but leave everything else in tact.

In most cases this may be nearly identical to `Fieldtype::deletePageField()`, but would be different
for things like page references where we wouldn't want relational data deleted.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->___emptyPageField($page, $field);

// usage with all arguments
$bool = $fieldtype->___emptyPageField(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field` Field object

## Return value

- `bool` True on success, false on DB delete failure.

## Exceptions

- `WireException`
