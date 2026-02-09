# ProcessPageSearchLive

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessPageSearch: Live Search (for PW admin)


@todo support searching repeaters

Methods:
- [`__construct(?Process $process = null, array $liveSearch = array())`](method-__construct.md)
- [`setSearchTypesOrder(array $types)`](method-setsearchtypesorder.md)
- [`setNoSearchTypes(array $types)`](method-setnosearchtypes.md)
- [`setDefaultOperators(string $singleWordOperator, string $multiWordOperator = '')`](method-setdefaultoperators.md)
- [`init(array $presets = array()): array`](method-init.md)
- [`execute(bool $getJSON = true): string|array`](method-___execute.md) (hookable)
- [`executeViewAll(): string`](method-executeviewall.md)
- [`find(array &$liveSearch): array`](method-find.md)
- [`findPages(array &$liveSearch): array`](method-findpages.md)
- [`useType(string $type, string $requestType = ''): bool`](method-usetype.md)
- [`findModules(array &$liveSearch, array &$modulesInfo): array`](method-findmodules.md)
- [`convertItemsFormat(array $items): array`](method-convertitemsformat.md)
- [`makeDebugItem(array $liveSearch): array`](method-makedebugitem.md)
- [`makeHelpItems(array $result, string $type): array`](method-makehelpitems.md)
- [`makeViewAllItem(array &$liveSearch, string $type, string $group, int $total, string $url = ''): array`](method-makeviewallitem.md)
- [`renderList(array $items, string $prefix = 'pw-search', string $class = 'list'): string`](method-___renderlist.md) (hookable)
- [`renderItem(array $item, string $prefix = 'pw-search', string $class = 'item'): string`](method-___renderitem.md) (hookable)
- [`findCustom(array $data): bool`](method-___findcustom.md) (hookable)
- [`addResult(string $group, string $title, string $url = '', array $data = array()): true`](method-addresult.md)
- [`addResults(string $group, array $results): true`](method-addresults.md)
- [`addHelp(string $group, array $examples): true`](method-addhelp.md)
- [`getDefaultPageSearchFields(): array`](method-___getdefaultpagesearchfields.md) (hookable)
