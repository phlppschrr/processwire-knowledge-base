# $pagesLoader->getNativeColumnValue($id, $column): int|string|bool

Source: `wire/core/PagesLoader.php`

Get value of of a native column in pages table for given page ID

## Arguments

- int|Page $id Page ID
- string $column

## Return value

int|string|bool Returns int/string value on success or boolean false if no matching row

## Throws

- \PDOException|WireException

## Meta

- @since 3.0.156
