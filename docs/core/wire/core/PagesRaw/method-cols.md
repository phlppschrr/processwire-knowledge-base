# $pagesRaw->cols($pageId, $cols = array(), array $options = array()): array

Source: `wire/core/PagesRaw.php`

Get native pages table columns (plural) for given page ID

This can only be used for native 'pages' table columns,
i.e. id, name, templates_id, status, parent_id, etc.

## Arguments

- int|array $pageId Page ID or array of page IDs
- array|string $cols Names of columns to get or omit to get all columns
- array $options - `cache` (bool): Allow use of memory cache to retrieve column value when available? (default=true) Used only if $pageId is an integer (not used when array of page IDs).

## Return value

array Returns associative array on success or empty array if not found If $pageId argument was an array then it returns a page ID indexed array of associative arrays, one for each page.

## Throws

- WireException

## Meta

- @since 3.0.190
