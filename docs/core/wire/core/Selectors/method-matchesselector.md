# $selectors->matchesSelector(Selector $selector, Wire $item): bool

Source: `wire/core/Selectors.php`

Does the given Wire match these Selector (single)?

## Usage

~~~~~
// basic usage
$bool = $selectors->matchesSelector($selector, $item);

// usage with all arguments
$bool = $selectors->matchesSelector(Selector $selector, Wire $item);
~~~~~

## Arguments

- `$selector` `Selector`
- `$item` `Wire`

## Return value

- `bool`

## Since

3.0.330
