# PagesParents

Source: `wire/core/PagesParents.php`

Inherits: `Wire`

## Summary

ProcessWire Pages Parents

Common methods:
- [`getParents()`](method-getparents.md)
- [`findParents()`](method-findparents.md)
- [`findParentIDs()`](method-findparentids.md)
- [`save()`](method-save.md)
- [`rebuild()`](method-rebuild.md)

Pages Parents
`$pages->parents`
Implements page parents helper methods for the `$pages` API variable and manages the pages_parents DB table.
This is not intended for the public API and instead used internally by
the `$pages` classes, but available at `$pages->parents()->methodName()` if
you want to use anything here.

~~~~~~
// Rebuild the entire pages_parents table
$numRows = $pages->parents()->rebuildAll();
~~~~~~


@since 3.0.156

## Methods
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`getParents(Page|int $page, array $options = array()): array|PageArray`](method-getparents.md) Get parents for given Page and/or specific columns from them
- [`findParents(array $options = array()): array|PageArray`](method-findparents.md) Find all pages that have children
- [`findParentIDs(null|Page|int $fromParent = null): array`](method-findparentids.md) Find IDs of all pages that are parents for other pages, optionally within a parent
- [`save(Page $page): int`](method-save.md) Check if saved page needs any pages_parents updates and perform them when applicable
- [`rebuild(Page $page): int`](method-rebuild.md) Rebuild pages_parents table for given page
- [`movePage(Page $page, Page $oldParent, Page $newParent): int`](method-movepage.md) Rebuild pages_parents table for given page (experimental faster alternative/rewrite of rebuild method)
- [`rebuildBranch(Page|int $fromParent): int`](method-rebuildbranch.md) Rebuild pages_parents branch starting at `$fromParent` and into all descendents
- [`rebuildAll(int|Page $fromParent = null): int`](method-rebuildall.md) Rebuild pages_parents table entirely or from branch starting with a parent branch
- [`clear(Page|int $page): int`](method-clear.md) Clear page from pages_parents index
- [`delete(Page|int $page): int`](method-delete.md) Delete page entirely from pages_parents table (both as page and parent)
- [`descendents(Page $page, string $selector = 'include=all'): PageArray`](method-descendents.md) Find descendents of `$page` by going recursive rather than using pages_parents table (for testing)
