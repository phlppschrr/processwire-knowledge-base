# $page->removeStatus($statusFlag): $this

Source: `wire/core/Page.php`

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
$result = $page->removeStatus($statusFlag);
~~~~~

## Arguments

- `$statusFlag` `int|string` Status flag constant or string representation (hidden, locked, unpublished, etc.)

## Return value

- `$this`

## Exceptions

- `WireException` If you attempt to remove `Page::statusSystem` or `Page::statusSystemID` statuses without first adding `Page::statusSystemOverride` status.

## See Also

- [Page::addStatus()](method-addstatus.md)
- [Page::hasStatus()](method-hasstatus.md)
