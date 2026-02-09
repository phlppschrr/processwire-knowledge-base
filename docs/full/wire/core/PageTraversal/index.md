# PageTraversal

Source: `wire/core/PageTraversal.php`

ProcessWire Page Traversal

Provides implementation for Page traversal functions.
Based upon the jQuery traversal functions.

Methods:
- [`numChildren(Page $page, bool|string|int|array $selector = null, array $options = array()): int`](method-numchildren.md)
- [`numDescendants(Page $page, bool|string|int|array $selector = null): int`](method-numdescendants.md)
- [`children(Page $page, string|array $selector = '', array $options = array()): PageArray`](method-children.md)
- [`child(Page $page, string|array $selector = '', array $options = array()): Page|NullPage`](method-child.md)
- [`parents(Page $page, string|array|bool $selector = ''): PageArray`](method-parents.md)
- [`numParents(Page $page, string $selector = ''): int`](method-numparents.md)
- [`parentsUntil(Page $page, string|Page|array $selector = '', string|array $filter = ''): PageArray`](method-parentsuntil.md)
- [`rootParent(Page $page): Page`](method-rootparent.md)
- [`siblings(Page $page, string $selector = ''): PageArray`](method-siblings.md)
- [`_getIncludeMode(string|array|Selectors $selector): string`](method-_getincludemode.md)
- [`_nextFinderOptions(Page $page, string|array|Selectors $selector, array $options): array`](method-_nextfinderoptions.md)
- [`_next(Page $page, string|array|Selectors $selector = '', array $options = array()): Page|NullPage|PageArray|int`](method-_next.md)
- [`index(Page $page, string|array|bool|Selectors $selector = ''): int`](method-index.md)
- [`next(Page $page, string|array|Selectors $selector = ''): Page|NullPage`](method-next.md)
- [`prev(Page $page, string|array|Selectors $selector = ''): Page|NullPage`](method-prev.md)
- [`nextAll(Page $page, string|array|Selectors $selector = '', array $options = array()): PageArray`](method-nextall.md)
- [`prevAll(Page $page, string|array|Selectors $selector = '', array $options = array()): PageArray`](method-prevall.md)
- [`nextUntil(Page $page, string|Page|array|Selectors $selector = '', string|array $filter = '', array $options = array()): PageArray`](method-nextuntil.md)
- [`prevUntil(Page $page, string|Page|array $selector = '', string|array $filter = '', array $options = array()): PageArray`](method-prevuntil.md)
- [`urlOptions(Page $page, array|int|string|bool|Language $options = array()): string`](method-urloptions.md)
- [`urls(Page $page, array $options = array()): array`](method-urls.md)
- [`editUrl(Page $page, array|bool|string $options = array()): string`](method-editurl.md)
- [`httpUrl(Page $page, array $options = array()): string`](method-httpurl.md)
- [`references(Page $page, string|bool $selector = '', Field|string $field = '', bool $getCount = false): PageArray|array|int`](method-references.md)
- [`hasReferences(Page $page, string $selector = '', string|Field|bool $field = ''): int|array`](method-hasreferences.md)
- [`numReferences(Page $page, string $selector = '', string|Field|bool $field = ''): int|array`](method-numreferences.md)
- [`referencing(Page $page, bool|Field|string|int $field = false, bool $getCount = false): PageArray|int|array`](method-referencing.md)
- [`numReferencing(Page $page, bool $field = false): int|array`](method-numreferencing.md)
- [`links(Page $page, string $selector = '', bool|string|Field $field = false, array $options = array()): PageArray|array|int`](method-links.md)
- [`numLinks(Page $page, bool $field = false): int`](method-numlinks.md)
- [`hasLinks(Page $page, bool $field = false): array|int|PageArray`](method-haslinks.md)
- [`nextSibling(Page $page, $selector = '', ?PageArray $siblings = null)`](method-nextsibling.md)
- [`nextSibling(Page $page, string|array $selector = '', ?PageArray $siblings = null): Page|NullPage`](method-nextsibling.md)
- [`prevSibling(Page $page, string|array $selector = '', ?PageArray $siblings = null): Page|NullPage`](method-prevsibling.md)
- [`nextAllSiblings(Page $page, string|array $selector = '', ?PageArray $siblings = null): PageArray`](method-nextallsiblings.md)
- [`prevAllSiblings(Page $page, string|array $selector = '', ?PageArray $siblings = null): PageArray`](method-prevallsiblings.md)
- [`nextUntilSiblings(Page $page, string|Page|array $selector = '', string|array $filter = '', ?PageArray $siblings = null): PageArray`](method-nextuntilsiblings.md)
- [`prevUntilSiblings(Page $page, string|Page|array $selector = '', string|array $filter = '', ?PageArray $siblings = null): PageArray`](method-prevuntilsiblings.md)
