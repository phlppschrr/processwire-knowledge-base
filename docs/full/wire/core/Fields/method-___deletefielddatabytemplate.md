# $fields->___deleteFieldDataByTemplate(Field $field, Template $template): bool

Source: `wire/core/Fields.php`

Physically delete all field data (from the database) used by pages of a given template

This is for internal API use only. This method is intended only to be called by
Fieldtype::deleteTemplateField

If you need to remove a field from a Fieldgroup, use Fieldgroup::remove(), and this
method will be call automatically at the appropriate time when save the fieldgroup.

## Arguments

- Field $field
- Template $template

## Return value

bool Whether or not it was successful

## Throws

- WireException when given a situation where deletion is not allowed
