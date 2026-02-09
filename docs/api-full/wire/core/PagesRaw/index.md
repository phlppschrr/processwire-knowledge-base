# PagesRaw

Source: `wire/core/PagesRaw.php`

Inherits: `Wire`

## Summary

ProcessWire Pages Raw Tools

Common methods:
- [`find()`](method-find.md)
- [`get()`](method-get.md)
- [`col()`](method-col.md)
- [`cols()`](method-cols.md)

Pages Raw
$pages->raw
Methods for finding and loading raw page data

## Methods
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`find(string|array|Selectors $selector, string|array|Field $field = '', array $options = array()): array`](method-find.md) Find pages and return raw data from them in a PHP array
- [`get(string|array|Selectors $selector, string|Field|int|array $field = '', array|bool $options = array()): array`](method-get.md) Get page (no exclusions) and return raw data from it in a PHP array
- [`col(int|array $pageId, string|array $col, array $options = array()): int|string|array|null`](method-col.md) Get native pages table column value for given page ID
- [`cols(int|array $pageId, array|string $cols = array(), array $options = array()): array`](method-cols.md) Get native pages table columns (plural) for given page ID
