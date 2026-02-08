# $selectors->matchesOrGroups(array $orGroups, Wire $item): bool

Source: `wire/core/Selectors.php`

Do the given OR-groups match the given Wire?

## Usage

~~~~~
// basic usage
$bool = $selectors->matchesOrGroups($orGroups, $item);

// usage with all arguments
$bool = $selectors->matchesOrGroups(array $orGroups, Wire $item);
~~~~~

## Arguments

- `$orGroups` `array|string[]|array[]`
- `$item` `Wire`

## Return value

- `bool`

## Since

3.0.330
