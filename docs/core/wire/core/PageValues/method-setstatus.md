# PageValues::setStatus()

Source: `wire/core/PageValues.php`

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

@param Page $page

@param int|array|string Status value, array of status names or values, or status name string.

@return Page

@see Page::addStatus(), Page::removeStatus()
