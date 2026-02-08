# $pages->getOneById($id, array $options = array()): Page|NullPage

Source: `wire/core/Pages.php`

Get one page by ID

This is the same as `getById()` with the `getOne` option.

## Usage

~~~~~
// basic usage
$page = $pages->getOneById($id);

// usage with all arguments
$page = $pages->getOneById($id, array $options = array());
~~~~~

## Arguments

- `$id` `int`
- `$options` (optional) `array`

## Return value

- `Page|NullPage`

## Since

3.0.186
