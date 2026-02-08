# $pages->___saved(Page $page, array $changes = array(), $values = array())

Source: `wire/core/Pages.php`

Hook called after a page is successfully saved

This is the same as hooking after `Pages::save`, except that it occurs before other save-related hooks.
Whereas `Pages::save` hooks occur after. In most cases, the distinction does not matter.

## Arguments

- `$page` `Page` The page that was saved
- `$changes` (optional) `array` Array of field names that changed
- `$values` (optional) `array` Array of values that changed, if values were being recorded, see Wire::getChanges(true) for details.

## See also

- [Pages::savedPageOrField()](method-___savedpageorfield.md)
- [Pages::savedField()](method-___savedfield.md)
