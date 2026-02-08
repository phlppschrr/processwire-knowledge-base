# $pagesLoader->getNativeColumnValue($id, $column): int|string|bool

Source: `wire/core/PagesLoader.php`

Get value of of a native column in pages table for given page ID

## Usage

~~~~~
// basic usage
$int = $pagesLoader->getNativeColumnValue($id, $column);
~~~~~

## Arguments

- `$id` `int|Page` Page ID
- `$column` `string`

## Return value

- `int|string|bool` Returns int/string value on success or boolean false if no matching row

## Exceptions

- `\PDOException|WireException`

## Since

3.0.156
