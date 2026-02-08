# $page->count(): int

Source: `wire/core/Page.php`

Returns number of children page has, affected by output formatting mode.

- When output formatting is on, returns only number of visible children,
  making the return value the same as the `Page::hasChildren()` method.

- When output formatting is off, returns number of all children without exclusion,
  making the return value the same as the `Page::numChildren()` method.

~~~~~
// Get number of visible children, like $page->hasChildren()
$page->of(true); // enable output formatting
$numVisible = $page->count();

// Get number of all children, like $page->numChildren()
$page->of(false); // disable output formatting
$numTotal = $page->count();
~~~~~

## Return value

int Quantity of children

## See also

- [Page::hasChildren()](method-haschildren.md)
- [Page::numChildren()](method-numchildren.md)
