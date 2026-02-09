# $pageValues->setStatus(Page $page, $value): Page

Source: `wire/core/PageValues.php`

Set the status setting, with some built-in protections

This method is also used when you set status directly, i.e. `$page->status = $value;`.

## Example

~~~~~
// set status to unpublished
$page->setStatus('unpublished');

// set status to hidden and unpublished
$page->setStatus('hidden, unpublished');

// set status to hidden + unpublished using Page constant bitmask
$page->setStatus(Page::statusHidden | Page::statusUnpublished);
~~~~~

## Usage

~~~~~
// basic usage
$page = $pageValues->setStatus($page, $value);

// usage with all arguments
$page = $pageValues->setStatus(Page $page, $value);
~~~~~

## Arguments

- `$page` `Page`
- int|array|string Status value, array of status names or values, or status name string.

## Return value

- `Page`

## See Also

- [Page::addStatus()](../Page/method-addstatus.md)
- [Page::removeStatus()](../Page/method-removestatus.md)
