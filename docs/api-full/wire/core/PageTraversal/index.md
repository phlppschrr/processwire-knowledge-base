# PageTraversal

Source: `wire/core/PageTraversal.php`

## Summary

ProcessWire Page Traversal

Common methods:
- [`numChildren()`](method-numchildren.md)
- [`numDescendants()`](method-numdescendants.md)
- [`children()`](method-children.md)
- [`child()`](method-child.md)
- [`parents()`](method-parents.md)

Provides implementation for Page traversal functions.
Based upon the jQuery traversal functions.

## Methods
- [`numChildren(Page $page, bool|string|int|array $selector = null, array $options = array()): int`](method-numchildren.md) Return number of children, optionally with conditions
- [`numDescendants(Page $page, bool|string|int|array $selector = null): int`](method-numdescendants.md) Return number of descendants, optionally with conditions
- [`children(Page $page, string|array $selector = '', array $options = array()): PageArray`](method-children.md) Return this page's children pages, optionally filtered by a selector
- [`child(Page $page, string|array $selector = '', array $options = array()): Page|NullPage`](method-child.md) Return the page's first single child that matches the given selector.
- [`parents(Page $page, string|array|bool $selector = ''): PageArray`](method-parents.md) Return this page's parent pages, or the parent pages matching the given selector.
- [`numParents(Page $page, string $selector = ''): int`](method-numparents.md) Return number of parents (depth relative to homepage) that this page has, optionally filtered by a selector
- [`parentsUntil(Page $page, string|Page|array $selector = '', string|array $filter = ''): PageArray`](method-parentsuntil.md) Return all parent from current till the one matched by $selector
- [`rootParent(Page $page): Page`](method-rootparent.md) Get the lowest-level, non-homepage parent of this page
- [`siblings(Page $page, string $selector = ''): PageArray`](method-siblings.md) Return this Page's sibling pages, optionally filtered by a selector.
- [`_getIncludeMode(string|array|Selectors $selector): string`](method-_getincludemode.md) Get include mode specified in selector or blank if none
- [`_nextFinderOptions(Page $page, string|array|Selectors $selector, array $options): array`](method-_nextfinderoptions.md) Builds the PageFinder options for the _next() method
- [`_next(Page $page, string|array|Selectors $selector = '', array $options = array()): Page|NullPage|PageArray|int`](method-_next.md) Provides the core logic for next, prev, nextAll, prevAll, nextUntil, prevUntil
- [`index(Page $page, string|array|bool|Selectors $selector = ''): int`](method-index.md) Return the index/position of the given page relative to its siblings
- [`next(Page $page, string|array|Selectors $selector = ''): Page|NullPage`](method-next.md) Return the next sibling page
- [`prev(Page $page, string|array|Selectors $selector = ''): Page|NullPage`](method-prev.md) Return the previous sibling page
- [`nextAll(Page $page, string|array|Selectors $selector = '', array $options = array()): PageArray`](method-nextall.md) Return all sibling pages after this one, optionally matching a selector
- [`prevAll(Page $page, string|array|Selectors $selector = '', array $options = array()): PageArray`](method-prevall.md) Return all sibling pages prior to this one, optionally matching a selector
- [`nextUntil(Page $page, string|Page|array|Selectors $selector = '', string|array $filter = '', array $options = array()): PageArray`](method-nextuntil.md) Return all sibling pages after this one until matching the one specified
- [`prevUntil(Page $page, string|Page|array $selector = '', string|array $filter = '', array $options = array()): PageArray`](method-prevuntil.md) Return all sibling pages prior to this one until matching the one specified
- [`urlOptions(Page $page, array|int|string|bool|Language $options = array()): string`](method-urloptions.md) Returns the URL to the page with $options
- [`urls(Page $page, array $options = array()): array`](method-urls.md) Return all URLs that this page can be accessed from (excluding URL segments and pagination)
- [`editUrl(Page $page, array|bool|string $options = array()): string`](method-editurl.md) Return the URL necessary to edit page
- [`httpUrl(Page $page, array $options = array()): string`](method-httpurl.md) Returns the URL to the page, including scheme and hostname
- [`references(Page $page, string|bool $selector = '', Field|string $field = '', bool $getCount = false): PageArray|array|int`](method-references.md) Return pages that are referencing the given one by way of Page references
- [`hasReferences(Page $page, string $selector = '', string|Field|bool $field = ''): int|array`](method-hasreferences.md) Return number of VISIBLE pages that are following (referencing) the given one by way of Page references
- [`numReferences(Page $page, string $selector = '', string|Field|bool $field = ''): int|array`](method-numreferences.md) Return number of ANY pages that are following (referencing) the given one by way of Page references
- [`referencing(Page $page, bool|Field|string|int $field = false, bool $getCount = false): PageArray|int|array`](method-referencing.md) Return pages that this page is referencing by way of Page reference fields
- [`numReferencing(Page $page, bool $field = false): int|array`](method-numreferencing.md) Return number of pages this one is following (referencing) by way of Page references
- [`links(Page $page, string $selector = '', bool|string|Field $field = false, array $options = array()): PageArray|array|int`](method-links.md) Find other pages linking to the given one by way contextual links is textarea/html fields
- [`numLinks(Page $page, bool $field = false): int`](method-numlinks.md) Return total found number of pages linking to this one with no exclusions
- [`hasLinks(Page $page, bool $field = false): array|int|PageArray`](method-haslinks.md) Return total number of pages visible to current user linking to this one
- [`nextSibling(Page $page, $selector = '', ?PageArray $siblings = null)`](method-nextsibling.md) *************************************************************************************************************** LEGACY METHODS
- [`nextSibling(Page $page, string|array $selector = '', ?PageArray $siblings = null): Page|NullPage`](method-nextsibling.md) Return the next sibling page, within a group of provided siblings (that includes the current page)
- [`prevSibling(Page $page, string|array $selector = '', ?PageArray $siblings = null): Page|NullPage`](method-prevsibling.md) Return the previous sibling page within a provided group of siblings that contains the current page
- [`nextAllSiblings(Page $page, string|array $selector = '', ?PageArray $siblings = null): PageArray`](method-nextallsiblings.md) Return all sibling pages after this one, optionally matching a selector
- [`prevAllSiblings(Page $page, string|array $selector = '', ?PageArray $siblings = null): PageArray`](method-prevallsiblings.md) Return all sibling pages before this one, optionally matching a selector
- [`nextUntilSiblings(Page $page, string|Page|array $selector = '', string|array $filter = '', ?PageArray $siblings = null): PageArray`](method-nextuntilsiblings.md) Return all sibling pages after this one until matching the one specified
- [`prevUntilSiblings(Page $page, string|Page|array $selector = '', string|array $filter = '', ?PageArray $siblings = null): PageArray`](method-prevuntilsiblings.md) Return all sibling pages before this one until matching the one specified
