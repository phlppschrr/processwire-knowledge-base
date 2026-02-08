# $fieldtype->___deletePageField(Page $page, Field $field): bool

Source: `wire/core/Fieldtype.php`

Delete the given Field from the given Page.

Must delete entries from field's database table that belong to the Page.

## Arguments

- Page $page
- Field $field Field object

## Return value

bool True on success, false on DB delete failure.

## Throws

- WireException
