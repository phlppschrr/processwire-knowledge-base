# PagesParents

Source: `wire/core/PagesParents.php`

Inherits: `Wire`

ProcessWire Pages Parents

Pages Parents
$pages->parents
Implements page parents helper methods for the $pages API variable and manages the pages_parents DB table.
This is not intended for the public API and instead used internally by
the $pages classes, but available at `$pages->parents()->methodName()` if
you want to use anything here.

~~~~~~
// Rebuild the entire pages_parents table
$numRows = $pages->parents()->rebuildAll();
~~~~~~


@since 3.0.156

Methods:
- [`__construct(Pages $pages)`](method-__construct.md)
- [`getParents(Page|int $page, array $options = array()): array|PageArray`](method-getparents.md)
- [`findParents(array $options = array()): array|PageArray`](method-findparents.md)
- [`findParentIDs(null|Page|int $fromParent = null): array`](method-findparentids.md)
- [`save(Page $page): int`](method-save.md)
- [`rebuild(Page $page): int`](method-rebuild.md)
- [`movePage(Page $page, Page $oldParent, Page $newParent): int`](method-movepage.md)
- [`rebuildBranch(Page|int $fromParent): int`](method-rebuildbranch.md)
- [`rebuildAll(int|Page $fromParent = null): int`](method-rebuildall.md)
- [`clear(Page|int $page): int`](method-clear.md)
- [`delete(Page|int $page): int`](method-delete.md)
- [`descendents(Page $page, string $selector = 'include=all'): PageArray`](method-descendents.md)
