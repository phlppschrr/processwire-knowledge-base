# $pagesRaw->col($pageId, $col, array $options = array()): int|string|array|null

Source: `wire/core/PagesRaw.php`

Get native pages table column value for given page ID

This can only be used for native 'pages' table columns,
i.e. id, name, templates_id, status, parent_id, etc.

## Arguments

- `$pageId` `int|array` Page ID or array of page IDs
- `$col` `string|array` Column name you want to get
- `$options` (optional) `array` - `cache` (bool): Allow use of memory cache to retrieve column value when available? (default=true) Used only if $pageId is an integer (not used when array of page IDs).

## Return value

int|string|array|null Returns column value or array of column values if $pageId was an array. When array is returned, it is indexed by page ID.

## Throws

- WireException

## Since

3.0.190
