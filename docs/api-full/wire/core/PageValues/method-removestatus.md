# $pageValues->removeStatus(Page $page, $statusFlag): Page

Source: `wire/core/PageValues.php`

Remove the specified status from this page

This is the preferred way to remove a status from a page. There is also a corresponding `Page::addStatus()` method.

## Example

~~~~~
// Remove hidden status from the page using status name
$page->removeStatus('hidden');

// Remove hidden status from the page using status constant
$page->removeStatus(Page::statusHidden);
~~~~~

## Usage

~~~~~
// basic usage
$page = $pageValues->removeStatus($page, $statusFlag);

// usage with all arguments
$page = $pageValues->removeStatus(Page $page, $statusFlag);
~~~~~

## Arguments

- `$page` `Page`
- `$statusFlag` `int|string` Status flag constant or string representation (hidden, locked, unpublished, etc.)

## Return value

- `Page`

## Exceptions

- `WireException` If you attempt to remove `Page::statusSystem` or `Page::statusSystemID` statuses without first adding `Page::statusSystemOverride` status.

## See Also

- [Page::addStatus()](../Page/method-addstatus.md)
- [Page::hasStatus()](../Page/method-hasstatus.md)
