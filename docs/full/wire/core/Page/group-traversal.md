# Page: traversal

Source: `wire/core/Page.php`

@property Page|string|int $parent The parent Page object or a NullPage if there is no parent. For assignment, you may also use the parent path (string) or id (integer).

@property PageArray $parents All the parent pages down to the root (homepage). Returns a PageArray.

@property Page $rootParent The parent page closest to the homepage (typically used for identifying a section)

@property int $numChildren The number of children (subpages) this page has, with no exclusions (fast).

@property int $hasChildren The number of visible children this page has. Excludes unpublished, no-access, hidden, etc.

@property int $numDescendants Number of descendants (quantity of children, and their children, and so on). @since 3.0.116

@property int $numParents Number of parent pages (i.e. depth) @since 3.0.117

@property PageArray $children All the children of this page. Returns a PageArray. See also $page->children($selector).

@property Page|NullPage $child The first child of this page. Returns a Page. See also $page->child($selector).

@property PageArray $siblings All the sibling pages of this page. Returns a PageArray. See also $page->siblings($selector).

@property Page $next This page's next sibling page, or NullPage if it is the last sibling. See also $page->next($pageArray).

@property Page $prev This page's previous sibling page, or NullPage if it is the first sibling. See also $page->prev($pageArray).

@property int $index Index of this page relative to its siblings, regardless of sort (starting from 0).

@property PageArray $references Return pages that are referencing the given one by way of Page references.

@property int $numReferences Total number of pages referencing this page with Page reference fields.

@property int $hasReferences Number of visible pages (to current user) referencing this page with page reference fields.

@property PageArray $referencing Return pages that this page is referencing by way of Page reference fields.

@property int $numReferencing Total number of other pages this page is pointing to (referencing) with Page fields.

@property PageArray $links Return pages that link to this one contextually in Textarea/HTML fields.

@property int $numLinks Total number of pages manually linking to this page in Textarea/HTML fields.

@property int $hasLinks Number of visible pages (to current user) linking to this page in Textarea/HTML fields.
