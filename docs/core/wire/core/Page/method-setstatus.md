# $page->setStatus($value): self

Source: `wire/core/Page.php`

Set the status setting, with some built-in protections

This method is also used when you set status directly, i.e. `$page->status = $value;`.

~~~~~
// set status to unpublished
$page->setStatus('unpublished');

// set status to hidden and unpublished
$page->setStatus('hidden, unpublished');

// set status to hidden + unpublished using Page constant bitmask
$page->setStatus(Page::statusHidden | Page::statusUnpublished);
~~~~~

## Arguments

- int|array|string Status value, array of status names or values, or status name string.

## Return value

self

## See also

- [Page::addStatus()](method-addstatus.md)
- [Page::removeStatus()](method-removestatus.md)
