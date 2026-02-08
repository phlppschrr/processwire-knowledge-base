# $pagesLoader->getNativeColumnValue($id, $column): int|string|bool

Source: `wire/core/PagesLoader.php`

Get value of of a native column in pages table for given page ID

## Arguments

- `$id` `int|Page` Page ID
- `$column` `string`

## Return value

int|string|bool Returns int/string value on success or boolean false if no matching row

## Throws

- \PDOException|WireException

## Since

3.0.156
