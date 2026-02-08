# PagesParents::findParentIDs()

Source: `wire/core/PagesParents.php`

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
