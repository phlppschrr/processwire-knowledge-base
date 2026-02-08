# $pagesType->saved(Page $page, array $changes = array(), $values = array())

Source: `wire/core/PagesType.php`

Hook called after a page of this type is successfully saved

## Usage

~~~~~
// basic usage
$result = $pagesType->saved($page);

// usage with all arguments
$result = $pagesType->saved(Page $page, array $changes = array(), $values = array());
~~~~~

## Hookable

- Hookable method name: `saved`
- Implementation: `___saved`
- Hook with: `$pagesType->saved()`

## Arguments

- `$page` `Page` The page that was saved
- `$changes` (optional) `array` Array of field names that changed
- `$values` (optional) `array` Array of values that changed, if values were being recorded, see Wire::getChanges(true) for details.

## Since

3.0.128
