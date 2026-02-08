# $pageValues->removeStatus(Page $page, $statusFlag): Page

Source: `wire/core/PageValues.php`

Remove the specified status from this page

This is the preferred way to remove a status from a page. There is also a corresponding `Page::addStatus()` method.

~~~~~
// Remove hidden status from the page using status name
$page->removeStatus('hidden');

// Remove hidden status from the page using status constant
$page->removeStatus(Page::statusHidden);
~~~~~

## Arguments

- Page $page
- int|string $statusFlag Status flag constant or string representation (hidden, locked, unpublished, etc.)

## Return value

Page

## Throws

- WireException If you attempt to remove `Page::statusSystem` or `Page::statusSystemID` statuses without first adding `Page::statusSystemOverride` status.

## See also

- [Page::addStatus()](../Page/method-addstatus.md)
- [Page::hasStatus()](../Page/method-hasstatus.md)
