# $fieldtype->deletePageField(Page $page, Field $field): bool

Source: `wire/core/Fieldtype.php`

Delete the given Field from the given Page.

Must delete entries from field's database table that belong to the Page.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->deletePageField($page, $field);

// usage with all arguments
$bool = $fieldtype->deletePageField(Page $page, Field $field);
~~~~~

## Hookable

- Hookable method name: `deletePageField`
- Implementation: `___deletePageField`
- Hook with: `$fieldtype->deletePageField()`

## Arguments

- `$page` `Page`
- `$field` `Field` Field object

## Return value

- `bool` True on success, false on DB delete failure.

## Exceptions

- `WireException`
