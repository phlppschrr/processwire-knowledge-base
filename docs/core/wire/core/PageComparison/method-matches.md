# $pageComparison->matches(Page $page, $s, array $options = array()): bool

Source: `wire/core/PageComparison.php`

Given a Selectors object or a selector string, return whether this Page matches it

## Usage

~~~~~
// basic usage
$bool = $pageComparison->matches($page, $s);

// usage with all arguments
$bool = $pageComparison->matches(Page $page, $s, array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$s` `string|array|Selectors`
- `$options` (optional) `array` Options to modify behavior (3.0.225+ only): - `useDatabase` (bool|null): Use database for matching rather than in-memory? (default=false)

## Return value

- `bool`
