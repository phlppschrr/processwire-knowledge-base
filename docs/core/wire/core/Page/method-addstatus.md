# Page::addStatus()

Source: `wire/core/Page.php`

Add the specified status to this page

This is the preferred way to add a new status to a page. There is also a corresponding `Page::removeStatus()` method.

~~~~~
// Add hidden status to the page using status name
$page->addStatus('hidden');

// Add hidden status to the page using status constant
$page->addStatus(Page::statusHidden);
~~~~~


@param int|string $statusFlag Status flag constant or string representation (hidden, locked, unpublished, etc.)

@return $this

@see Page::removeStatus(), Page::hasStatus()
