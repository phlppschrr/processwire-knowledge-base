# $page->resetTrackChanges($trackChanges = true): $this

Source: `wire/core/Page.php`

Clears out any tracked changes and turns change tracking ON or OFF

Use this method when you want to clear a list of tracked changes on the page. Note that any changes are still
present, but ProcessWire no longer knows they had been changed. Meaning, the changes won't be available to
the `$page->isChanged()` and `$page->getChanges()` methods, and the changes might be skipped over if/when
the page is saved.

## Usage

~~~~~
// basic usage
$result = $page->resetTrackChanges();

// usage with all arguments
$result = $page->resetTrackChanges($trackChanges = true);
~~~~~

## Arguments

- `$trackChanges` (optional) `bool` True to turn change tracking ON, or false to turn OFF. Default of true is assumed.

## Return value

- `$this`

## See Also

- [Page::isChanged()](method-ischanged.md)
- [Page::getChanges()](index.md)
- [Page::trackChanges()](index.md)
