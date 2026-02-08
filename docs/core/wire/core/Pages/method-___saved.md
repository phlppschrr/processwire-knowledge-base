# Pages::___saved()

Source: `wire/core/Pages.php`

Hook called after a page is successfully saved

This is the same as hooking after `Pages::save`, except that it occurs before other save-related hooks.
Whereas `Pages::save` hooks occur after. In most cases, the distinction does not matter.


@param Page $page The page that was saved

@param array $changes Array of field names that changed

@param array $values Array of values that changed, if values were being recorded, see Wire::getChanges(true) for details.

@see Pages::savedPageOrField(), Pages::savedField()
