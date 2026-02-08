# $fieldtype->replacePageField(Page $src, Page $dst, Field $field): bool

Source: `wire/core/Fieldtype.php`

Move this field’s data from one page to another.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->replacePageField($src, $dst, $field);

// usage with all arguments
$bool = $fieldtype->replacePageField(Page $src, Page $dst, Field $field);
~~~~~

## Hookable

- Hookable method name: `replacePageField`
- Implementation: `___replacePageField`
- Hook with: `$fieldtype->replacePageField()`

## Arguments

- `$src` `Page` Source Page
- `$dst` `Page` Destination Page
- `$field` `Field`

## Return value

- `bool`
