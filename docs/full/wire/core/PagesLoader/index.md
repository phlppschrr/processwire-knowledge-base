# PagesLoader

Source: `wire/core/PagesLoader.php`

Inherits: `Wire`

ProcessWire Pages Loader

Pages Loader
$pages->loader
Implements page finding/loading methods for the $pages API variable.
Please always use `$pages->method()` rather than `$pages->loader->method()` in cases where there is overlap.

Methods:
- [`__construct(Pages $pages)`](method-__construct.md)
- [`setOutputFormatting(bool $outputFormatting = true)`](method-setoutputformatting.md)
- [`getOutputFormatting(): bool`](method-getoutputformatting.md)
- [`setAutojoin(bool $autojoin = true)`](method-setautojoin.md)
- [`getAutojoin(): bool`](method-getautojoin.md)
- [`normalizeSelectorString(string $selector, bool $convertIDs = true): array|int|string`](method-normalizeselectorstring.md)
- [`normalizeSelector(string|int|array $selector, bool $convertIDs = true): array|int|string`](method-normalizeselector.md)
- [`isIdArray(array &$a): bool`](method-isidarray.md)
- [`findShortcut(string|array|Selectors $selector, array $options, array $loadOptions): bool|Page|PageArray`](method-findshortcut.md)
- [`find(string|int|array|Selectors $selector, array|string $options = array()): PageArray|array`](method-find.md)
- [`findMin(string|array|Selectors $selector, array $options = array()): PageArray`](method-findmin.md)
- [`findOne(string|int|array|Selectors $selector, array|string $options = array()): Page|NullPage`](method-findone.md)
- [`findCache(string|array|Selectors $selector, int|string|bool|null $expire = 60, array $options = array()): PageArray|array`](method-findcache.md)
- [`get(string|int|array|Selectors $selector, array $options = array()): Page|NullPage`](method-get.md)
- [`has(string|int|array|Selectors $selector, bool $verbose = false, array $options = array()): array|int`](method-has.md)
- [`getById(array|WireArray|string|int $_ids, Template|array|string|int|null $template = null, int|null $parent_id = null): PageArray|Page|NullPage`](method-getbyid.md)
- [`findByName(string $name, array $options = array()): array|NullPage|Page|PageArray`](method-findbyname.md)
- [`getPath(int|Page $id, null|array|Language|int|string $options = array()): string`](method-getpath.md)
- [`getByPath(string $path, array|bool $options = array()): Page|int`](method-getbypath.md)
- [`getFresh(Page|string|array|Selectors|int $selectorOrPage, array $options = array()): Page|NullPage`](method-getfresh.md)
- [`getNumChildren(int|Page $page): int`](method-getnumchildren.md)
- [`count(string|array|Selectors $selector = '', array|string $options = array()): int`](method-count.md)
- [`preloadFields(Page $page, array $fieldNames, array $options = array()): array`](method-preloadfields.md)
- [`preloadAllFields(Page $page, array $options = array()): array`](method-preloadallfields.md)
- [`skipPreloadField(Page $page, Field $field, array $options): string`](method-skippreloadfield.md)
- [`filterListable(PageArray $items, string $includeMode = '', array $options = array()): PageArray`](method-filterlistable.md)
- [`getNativeColumns(): array`](method-getnativecolumns.md)
- [`getNativeColumnValue(int|Page $id, string $column): int|string|bool`](method-getnativecolumnvalue.md)
- [`isNativeColumn($columnName): bool`](method-isnativecolumn.md)
- [`debug(bool|null $debug = null): bool`](method-debug.md)
- [`getTotalPagesLoaded(): int`](method-gettotalpagesloaded.md)
- [`getLastPageFinder(): PageFinder|null`](method-getlastpagefinder.md)
- [`isLoading(): bool`](method-isloading.md)
