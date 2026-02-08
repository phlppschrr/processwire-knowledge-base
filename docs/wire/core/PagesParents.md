# PagesParents

Source: `wire/core/PagesParents.php`

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

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

@since 3.0.156

## __construct()

Construct

@param Pages $pages

## getParents()

Get parents for given Page and/or specific columns from them

- Return value has no exclusions for access control or status.
- Return value order is closest parent to furthest.
- This attempts to return all pages in 1 optimized query, making it potentially faster
  than other methods.
- When using `column` or `columns` options, specify only one or the other, and include
  column(s) native to pages DB table only, with 1 exception—you may specify `path` as
  a column, which will return the generated page path(s).

@param Page|int $page Page or page ID

@param array $options
 - `column` (string): Just return array of values from this column (use `columns` option when you need multiple columns). (default='')
 - `columns` (array): Return array of associative arrays containing these columns for each page (not to be combined with `column` option)
 - `indexBy` (string): Return array indexed by column `id` or `parent_id`, applies only if given column/columns (default='')
 - `includePage` (bool): Also include data for given $page in return value? (default=false)
 - `noHome` (bool): Omit homepage from return value (default=false)
 - `joinQty` (int): Number of parents to join in query before going recursive, for internal use (default=4).

@return array|PageArray If given column/columns returns an array, otherwise returns a PageArray

@since 3.0.156

## findParents()

Find all pages that have children

@param array $options

@return array|PageArray

@since 3.0.156

## findParentIDs()

Find IDs of all pages that are parents for other pages, optionally within a parent

Does not rely on pages_parents index table, so can be used for rebuilding it.

Faster than findParents() in cases where the pages_parents table cannot be used
and there are potentially hundreds/thousands of parents to find. However, it does
use more memory than findParents() even if it can be potentially a lot faster.

~~~~~
// the following two calls should produce identical results (excluding order)
// if they don’t, the index may need to be rebuilt
$pages->parents()->findParentIDs($id);
$pages->parents()->findParents([
  'parent' => $id,
  'indexByID' => true,
  'column' => 'parent_id'
]);
~~~~~

@param null|Page|int $fromParent Specify parent to limit results within, or negative int for minimum parent_id,
  for instance a value of -2 would exclude homepage and items with homepage (id=1) as their parent.

@return array Returns array in format [ id => parent_id ]

@since 3.0.156

## save()

Check if saved page needs any pages_parents updates and perform them when applicable

@param Page $page

@return int Number of rows updated

## rebuild()

Rebuild pages_parents table for given page

This descends into both parents, and children that are themselves parents,
and this method already calls the rebuildBranch() method when appropriate.

@param Page $page

@return int

@since 3.0.156

## movePage()

Rebuild pages_parents table for given page (experimental faster alternative/rewrite of rebuild method)

@param Page $page

@param Page $oldParent

@param Page $newParent

@return int

@throws WireException

@since 3.0.212

## rebuildBranch()

Rebuild pages_parents branch starting at $fromParent and into all descendents

@param Page|int $fromParent From parent Page or ID

@return int Number of rows inserted

## rebuildAll()

Rebuild pages_parents table entirely or from branch starting with a parent branch

@param int|Page $fromParent Specify parent ID or page to rebuild from that parent, or omit to rebuild all

@return int Number of rows inserted

@since 3.0.156

## clear()

Clear page from pages_parents index

@param Page|int $page

@return int

@since 3.0.156

## delete()

Delete page entirely from pages_parents table (both as page and parent)

@param Page|int $page

@return int

@since 3.0.156

## descendents()

Find descendents of $page by going recursive rather than using pages_parents table (for testing)

@param Page $page

@param string $selector

@return PageArray
