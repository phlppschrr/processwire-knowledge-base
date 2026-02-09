# $pageComparison->selectorMatchesProperty(Page $page, Selector $selector, $property): bool

Source: `wire/core/PageComparison.php`

Return whether single property from individual Selector matches Page

## Usage

~~~~~
// basic usage
$bool = $pageComparison->selectorMatchesProperty($page, $selector, $property);

// usage with all arguments
$bool = $pageComparison->selectorMatchesProperty(Page $page, Selector $selector, $property);
~~~~~

## Arguments

- `$page` `Page`
- `$selector` `Selector`
- `$property` `string`

## Return value

- `bool`

## Since

3.0.231
