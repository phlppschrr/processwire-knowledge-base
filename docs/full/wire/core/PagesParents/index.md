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
Method: [__construct()](method-__construct.md)
Method: [getParents()](method-getparents.md)
Method: [findParents()](method-findparents.md)
Method: [findParentIDs()](method-findparentids.md)
Method: [save()](method-save.md)
Method: [rebuild()](method-rebuild.md)
Method: [movePage()](method-movepage.md)
Method: [rebuildBranch()](method-rebuildbranch.md)
Method: [rebuildAll()](method-rebuildall.md)
Method: [clear()](method-clear.md)
Method: [delete()](method-delete.md)
Method: [descendents()](method-descendents.md)
