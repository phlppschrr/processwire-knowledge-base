# $pages->savedPageOrField(Page $page, array $changes = array())

Source: `wire/core/Pages.php`

Hook called after either of Pages::save or Pages::saveField successfully executes

## Usage

~~~~~
// basic usage
$result = $pages->savedPageOrField($page);

// usage with all arguments
$result = $pages->savedPageOrField(Page $page, array $changes = array());
~~~~~

## Hookable

- Hookable method name: `savedPageOrField`
- Implementation: `___savedPageOrField`
- Hook with: `$pages->savedPageOrField()`

## Arguments

- `$page` `Page`
- `$changes` (optional) `array` Names of fields

## See Also

- [Pages::saved()](method-___saved.md)
- [Pages::savedField()](method-___savedfield.md)
