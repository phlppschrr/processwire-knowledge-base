# $pageComparison->isEqual(Page $page, $key, $value1, $value2): bool

Source: `wire/core/PageComparison.php`

Is $value1 equal to $value2?

## Usage

~~~~~
// basic usage
$bool = $pageComparison->isEqual($page, $key, $value1, $value2);

// usage with all arguments
$bool = $pageComparison->isEqual(Page $page, $key, $value1, $value2);
~~~~~

## Arguments

- `$key` `string` Name of the key that triggered the check (see WireData::set)
- `$value1` `mixed`
- `$value2` `mixed`

## Return value

- `bool`
