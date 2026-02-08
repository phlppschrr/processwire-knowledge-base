# $fields->___deleteFieldDataByTemplate(Field $field, Template $template): bool

Source: `wire/core/Fields.php`

Physically delete all field data (from the database) used by pages of a given template

This is for internal API use only. This method is intended only to be called by
Fieldtype::deleteTemplateField

If you need to remove a field from a Fieldgroup, use Fieldgroup::remove(), and this
method will be call automatically at the appropriate time when save the fieldgroup.

## Usage

~~~~~
// basic usage
$bool = $fields->___deleteFieldDataByTemplate($field, $template);

// usage with all arguments
$bool = $fields->___deleteFieldDataByTemplate(Field $field, Template $template);
~~~~~

## Arguments

- `$field` `Field`
- `$template` `Template`

## Return value

- `bool` Whether or not it was successful

## Exceptions

- `WireException` when given a situation where deletion is not allowed
