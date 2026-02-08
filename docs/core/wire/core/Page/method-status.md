# $page->status($value = false, $status = null): int|array|Page

Source: `wire/core/Page.php`

Get or set current status

- When manipulating status, you may prefer to use the `$page->addStatus()` and `$page->removeStatus()` methods instead.

- Use this `status()` method when you want to set multiple statuses at once, or when you want to get status rather than set it.

- You can also get or set status directly, by manipulating the `$page->status` property.

~~~~~
// Get the current status as bitmask
$status = $page->status();

// Get an array of status names assigned to page
$statuses = $page->status(true);

// Set status by Page constant bitmask
$page->status(Page::statusHidden | Page::statusUnpublished);

// Set status by name
$page->status('unpublished');

// Set status by names
$page->status(['hidden', 'unpublished']);
~~~~~

## Arguments

- `$value` (optional) `bool|int` Optionally specify one of the following: - `true` (boolean): To return an array of status names (indexed by status number). - `integer|string|array`: Status number(s) or status name(s) to set the current page status (same as $page->status = $value)
- `$status` (optional) `int|null` If you specified `true` for first argument, optionally specify status value you want to use (if not the current).

## Return value

int|array|Page If setting status, `$this` is returned. If getting status: current status or array of status names is returned.

## See also

- [Page::addStatus()](method-addstatus.md)
- [Page::removeStatus()](method-removestatus.md)
- [Page::hasStatus()](method-hasstatus.md)
