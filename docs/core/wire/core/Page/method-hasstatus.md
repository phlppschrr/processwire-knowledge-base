# $page->hasStatus($status): bool

Source: `wire/core/Page.php`

Does this page have the given status?

This method is the preferred way to check if a page has a particular status.
The status may be specified as one of the `Page::status` constants or a string representing
one of the constants, i.e. `hidden`, `unpublished`, `locked`, and so on.

~~~~~
// check if page has hidden status using status name
if($page->hasStatus('hidden')) { ... }

// check if page has hidden status using status constant
if($page->hasStatus(Page::statusHidden)) { ... }

// There are also method shortcuts, i.e.
if($page->isHidden()) { ... }
if($page->isUnpublished()) { ... }
if($page->isLocked()) { ... }
~~~~~

## Arguments

- `$status` `int|string` Status flag constant or string representation (hidden, locked, unpublished, etc.)

## Return value

bool Returns true if page has the given status, or false if it doesn't.

## See also

- [Page::addStatus()](method-addstatus.md)
- [Page::removeStatus()](method-removestatus.md)
- [Page::isHidden()](method-ishidden.md)
- [Page::isUnpublished()](method-isunpublished.md)
- [Page::isLocked()](method-islocked.md)
