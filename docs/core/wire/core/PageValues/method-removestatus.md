# PageValues::removeStatus()

Source: `wire/core/PageValues.php`

Remove the specified status from this page

This is the preferred way to remove a status from a page. There is also a corresponding `Page::addStatus()` method.

~~~~~
// Remove hidden status from the page using status name
$page->removeStatus('hidden');

// Remove hidden status from the page using status constant
$page->removeStatus(Page::statusHidden);
~~~~~

@param Page $page

@param int|string $statusFlag Status flag constant or string representation (hidden, locked, unpublished, etc.)

@return Page

@throws WireException If you attempt to remove `Page::statusSystem` or `Page::statusSystemID` statuses without first adding `Page::statusSystemOverride` status.

@see Page::addStatus(), Page::hasStatus()
