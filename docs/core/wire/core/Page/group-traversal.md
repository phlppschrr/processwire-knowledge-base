# Page: traversal

Source: `wire/core/Page.php`

- [$parent: Page|string|int](method-parent.md) The parent Page object or a NullPage if there is no parent. For assignment, you may also use the parent path (string) or id (integer).

- [$parents: PageArray](method-parents.md) All the parent pages down to the root (homepage). Returns a PageArray.

- [$rootParent: Page](method-___rootparent.md) The parent page closest to the homepage (typically used for identifying a section)

- [$numChildren: int](method-numchildren.md) The number of children (subpages) this page has, with no exclusions (fast).

- [$hasChildren: int](method-haschildren.md) The number of visible children this page has. Excludes unpublished, no-access, hidden, etc.

- [$numDescendants: int](method-numdescendants.md) Number of descendants (quantity of children, and their children, and so on). @since 3.0.116

- [$numParents: int](method-numparents.md) Number of parent pages (i.e. depth) @since 3.0.117

- [$children: PageArray](method-children.md) All the children of this page. Returns a PageArray. See also $page->children($selector).

- [$child: Page|NullPage](method-child.md) The first child of this page. Returns a Page. See also $page->child($selector).

- [$siblings: PageArray](method-siblings.md) All the sibling pages of this page. Returns a PageArray. See also $page->siblings($selector).

- [$next: Page](method-next.md) This page's next sibling page, or NullPage if it is the last sibling. See also $page->next($pageArray).

- [$prev: Page](method-prev.md) This page's previous sibling page, or NullPage if it is the first sibling. See also $page->prev($pageArray).

- [$index: int](method-index.md) Index of this page relative to its siblings, regardless of sort (starting from 0).

- [$references: PageArray](method-___references.md) Return pages that are referencing the given one by way of Page references.

- $numReferences: int Total number of pages referencing this page with Page reference fields.

- $hasReferences: int Number of visible pages (to current user) referencing this page with page reference fields.

- $referencing: PageArray Return pages that this page is referencing by way of Page reference fields.

- $numReferencing: int Total number of other pages this page is pointing to (referencing) with Page fields.

- [$links: PageArray](method-___links.md) Return pages that link to this one contextually in Textarea/HTML fields.

- $numLinks: int Total number of pages manually linking to this page in Textarea/HTML fields.

- $hasLinks: int Number of visible pages (to current user) linking to this page in Textarea/HTML fields.
