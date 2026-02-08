# $pagesRaw->cols($pageId, $cols = array(), array $options = array()): array

Source: `wire/core/PagesRaw.php`

Get native pages table columns (plural) for given page ID

This can only be used for native 'pages' table columns,
i.e. id, name, templates_id, status, parent_id, etc.

## Arguments

- `$pageId` `int|array` Page ID or array of page IDs
- `$cols` (optional) `array|string` Names of columns to get or omit to get all columns
- `$options` (optional) `array` - `cache` (bool): Allow use of memory cache to retrieve column value when available? (default=true) Used only if $pageId is an integer (not used when array of page IDs).

## Return value

array Returns associative array on success or empty array if not found If $pageId argument was an array then it returns a page ID indexed array of associative arrays, one for each page.

## Throws

- WireException

## Since

3.0.190
