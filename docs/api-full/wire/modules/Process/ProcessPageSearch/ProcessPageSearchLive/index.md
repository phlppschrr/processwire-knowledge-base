# ProcessPageSearchLive

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Inherits: `Wire`

## Summary

ProcessPageSearch: Live Search (for PW admin)

Common methods:
- [`setSearchTypesOrder()`](method-setsearchtypesorder.md)
- [`setNoSearchTypes()`](method-setnosearchtypes.md)
- [`setDefaultOperators()`](method-setdefaultoperators.md)
- [`init()`](method-init.md)
- [`execute()`](method-___execute.md)

Groups:
Group: [other](group-other.md)

@todo support searching repeaters

## Methods
- [`__construct(?Process $process = null, array $liveSearch = array())`](method-__construct.md) Construct
- [`setSearchTypesOrder(array $types)`](method-setsearchtypesorder.md) Set order of search types
- [`setNoSearchTypes(array $types)`](method-setnosearchtypes.md) Set types that should be excluded unless specifically asked for
- [`setDefaultOperators(string $singleWordOperator, string $multiWordOperator = '')`](method-setdefaultoperators.md) Set default operators to use for searches (if query does not specify operator)
- [`init(array $presets = array()): array`](method-init.md) Initialize live search
- [`execute(bool $getJSON = true): string|array`](method-___execute.md) (hookable) Execute live search and return JSON result
- [`executeViewAll(): string`](method-executeviewall.md) Render output for landing page to view all items of a particular type
- [`find(array &$liveSearch): array`](method-find.md) Perform find of types, pages, modules
- [`findPages(array &$liveSearch): array`](method-findpages.md) Find pages for live search
- [`useType(string $type, string $requestType = ''): bool`](method-usetype.md) Allow this search type?
- [`findModules(array &$liveSearch, array &$modulesInfo): array`](method-findmodules.md) Find modules matching query
- [`convertItemsFormat(array $items): array`](method-convertitemsformat.md) Convert items from native live search format (v2) to v1 format
- [`makeDebugItem(array $liveSearch): array`](method-makedebugitem.md) Make a search result item that displays debugging info
- [`makeHelpItems(array $result, string $type): array`](method-makehelpitems.md) Make a search result item that displays property info
- [`makeViewAllItem(array &$liveSearch, string $type, string $group, int $total, string $url = ''): array`](method-makeviewallitem.md) Make a search result item that displays a “view all” link
- [`renderList(array $items, string $prefix = 'pw-search', string $class = 'list'): string`](method-___renderlist.md) (hookable) Render “view all” list
- [`renderItem(array $item, string $prefix = 'pw-search', string $class = 'item'): string`](method-___renderitem.md) (hookable) Render an item for the “view all” list
- [`findCustom(array $data): bool`](method-___findcustom.md) (hookable) Hookable method to find custom search results
- [`addResult(string $group, string $title, string $url = '', array $data = array()): true`](method-addresult.md) Add a custom search result
- [`addResults(string $group, array $results): true`](method-addresults.md) Add multiple results at once
- [`addHelp(string $group, array $examples): true`](method-addhelp.md) Add help examples for when the help results are displayed
- [`getDefaultPageSearchFields(): array`](method-___getdefaultpagesearchfields.md) (hookable) Get the names of fields that should be used when searching pages
