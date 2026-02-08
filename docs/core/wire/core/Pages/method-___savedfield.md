# $pages->savedField(Page $page, Field $field)

Source: `wire/core/Pages.php`

Hook called after Pages::saveField successfully executes

## Usage

~~~~~
// basic usage
$result = $pages->savedField($page, $field);

// usage with all arguments
$result = $pages->savedField(Page $page, Field $field);
~~~~~

## Hookable

- Hookable method name: `savedField`
- Implementation: `___savedField`
- Hook with: `$pages->savedField()`

## Arguments

- `$page` `Page`
- `$field` `Field`

## See Also

- [Pages::savedPageOrField()](method-___savedpageorfield.md)
