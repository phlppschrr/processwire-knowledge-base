# $functionsAPI->pageId($value): int|false

Source: `wire/core/FunctionsAPI.php`

Return id for given page or false if it’s not a page

Returns positive int (page id) for page that exists, 0 for NullPage,
or false if given $value is not a Page.

## Usage

~~~~~
// basic usage
$int = $functionsAPI->pageId($value);
~~~~~

## Arguments

- `$value` `Page|mixed`

## Return value

- `int|false`

## Since

3.0.224
