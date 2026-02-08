# $fieldtype->isDeleteValue(Page $page, Field $field, $value): bool

Source: `wire/core/Fieldtype.php`

Is given value one that should cause the DB row(s) to be deleted rather than saved?

Not applicable to Fieldtypes that override the savePageField() method with their own
implementation, unless they also use this method.

## Arguments

- Page $page
- Field $field
- mixed $value

## Return value

bool

## Meta

- @since 3.0.150
