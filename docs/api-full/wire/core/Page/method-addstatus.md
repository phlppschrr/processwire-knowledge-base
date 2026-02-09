# $page->addStatus($statusFlag): $this

Source: `wire/core/Page.php`

Add the specified status to this page

This is the preferred way to add a new status to a page. There is also a corresponding `Page::removeStatus()` method.

## Example

~~~~~
// Add hidden status to the page using status name
$page->addStatus('hidden');

// Add hidden status to the page using status constant
$page->addStatus(Page::statusHidden);
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->addStatus($statusFlag);
~~~~~

## Arguments

- `$statusFlag` `int|string` Status flag constant or string representation (hidden, locked, unpublished, etc.)

## Return value

- `$this`

## See Also

- [Page::removeStatus()](method-removestatus.md)
- [Page::hasStatus()](method-hasstatus.md)
