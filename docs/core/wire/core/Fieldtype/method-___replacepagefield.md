# $fieldtype->___replacePageField(Page $src, Page $dst, Field $field): bool

Source: `wire/core/Fieldtype.php`

Move this field’s data from one page to another.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->___replacePageField($src, $dst, $field);

// usage with all arguments
$bool = $fieldtype->___replacePageField(Page $src, Page $dst, Field $field);
~~~~~

## Arguments

- `$src` `Page` Source Page
- `$dst` `Page` Destination Page
- `$field` `Field`

## Return value

- `bool`
