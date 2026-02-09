# PagesLoader

Source: `wire/core/PagesLoader.php`

Inherits: `Wire`

## Summary

ProcessWire Pages Loader

Common methods:
- [`setOutputFormatting()`](method-setoutputformatting.md)
- [`getOutputFormatting()`](method-getoutputformatting.md)
- [`setAutojoin()`](method-setautojoin.md)
- [`getAutojoin()`](method-getautojoin.md)
- [`normalizeSelectorString()`](method-normalizeselectorstring.md)

Pages Loader
`$pages->loader`
Implements page finding/loading methods for the `$pages` API variable.
Please always use `$pages->method()` rather than `$pages->loader->method()` in cases where there is overlap.

## Methods
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`setOutputFormatting(bool $outputFormatting = true)`](method-setoutputformatting.md) Set whether loaded pages have their outputFormatting turned on or off
- [`getOutputFormatting(): bool`](method-getoutputformatting.md) Get whether loaded pages have their outputFormatting turned on or off
- [`setAutojoin(bool $autojoin = true)`](method-setautojoin.md) Enable or disable use of autojoin for all queries
- [`getAutojoin(): bool`](method-getautojoin.md) Get whether autojoin is enabled for page loading queries
- [`normalizeSelectorString(string $selector, bool $convertIDs = true): array|int|string`](method-normalizeselectorstring.md) Normalize a selector string
- [`normalizeSelector(string|int|array $selector, bool $convertIDs = true): array|int|string`](method-normalizeselector.md) Normalize a selector
- [`isIdArray(array &$a): bool`](method-isidarray.md) Is this an array of IDs? Also sanitizes to all integers when true
- [`findShortcut(string|array|Selectors $selector, array $options, array $loadOptions): bool|Page|PageArray`](method-findshortcut.md) Helper for find() method to attempt to shortcut the find when possible
- [`find(string|int|array|Selectors $selector, array|string $options = array()): PageArray|array`](method-find.md) Given a Selector string, return the Page objects that match in a PageArray.
- [`findMin(string|array|Selectors $selector, array $options = array()): PageArray`](method-findmin.md) Minimal find for reduced or delayed overload in some circumstances
- [`findOne(string|int|array|Selectors $selector, array|string $options = array()): Page|NullPage`](method-findone.md) Like find() but returns only the first match as a Page object (not PageArray)
- [`findCache(string|array|Selectors $selector, int|string|bool|null $expire = 60, array $options = array()): PageArray|array`](method-findcache.md) Find pages and cache the result for specified period of time
- [`get(string|int|array|Selectors $selector, array $options = array()): Page|NullPage`](method-get.md) Returns the first page matching the given selector with no exclusions
- [`has(string|int|array|Selectors $selector, bool $verbose = false, array $options = array()): array|int`](method-has.md) Is there any page that matches the given $selector in the system? (with no exclusions)
- [`getById(array|WireArray|string|int $_ids, Template|array|string|int|null $template = null, int|null $parent_id = null): PageArray|Page|NullPage`](method-getbyid.md) Given an array or CSV string of Page IDs, return a PageArray
- [`findByName(string $name, array $options = array()): array|NullPage|Page|PageArray`](method-findbyname.md) Find page(s) by name
- [`getPath(int|Page $id, null|array|Language|int|string $options = array()): string`](method-getpath.md) Given an ID return a path to a page, without loading the actual page
- [`getByPath(string $path, array|bool $options = array()): Page|int`](method-getbypath.md) Get a page by its path, similar to $pages->get('/path/to/page/') but with more options
- [`getFresh(Page|string|array|Selectors|int $selectorOrPage, array $options = array()): Page|NullPage`](method-getfresh.md) Get a fresh, non-cached copy of a Page from the database
- [`getNumChildren(int|Page $page): int`](method-getnumchildren.md) Load total number of children from DB for given page
- [`count(string|array|Selectors $selector = '', array|string $options = array()): int`](method-count.md) Count and return how many pages will match the given selector string
- [`preloadFields(Page $page, array $fieldNames, array $options = array()): array`](method-preloadfields.md) Preload/Prefetch fields for page together as a group (experimental)
- [`preloadAllFields(Page $page, array $options = array()): array`](method-preloadallfields.md) Preload all supported fields for given page (experimental)
- [`skipPreloadField(Page $page, Field $field, array $options): string`](method-skippreloadfield.md) Skip preloading of this field or fieldtype?
- [`filterListable(PageArray $items, string $includeMode = '', array $options = array()): PageArray`](method-filterlistable.md) Remove pages from already-loaded PageArray aren't visible or accessible
- [`getNativeColumns(): array`](method-getnativecolumns.md) Returns an array of all columns native to the pages table
- [`getNativeColumnValue(int|Page $id, string $column): int|string|bool`](method-getnativecolumnvalue.md) Get value of of a native column in pages table for given page ID
- [`isNativeColumn($columnName): bool`](method-isnativecolumn.md) Is the given column name native to the pages table?
- [`debug(bool|null $debug = null): bool`](method-debug.md) Get or set debug state
- [`getTotalPagesLoaded(): int`](method-gettotalpagesloaded.md) Return the total quantity of pages loaded by getById()
- [`getLastPageFinder(): PageFinder|null`](method-getlastpagefinder.md) Get last used instance of PageFinder (for debugging purposes)
- [`isLoading(): bool`](method-isloading.md) Are we currently loading pages?
