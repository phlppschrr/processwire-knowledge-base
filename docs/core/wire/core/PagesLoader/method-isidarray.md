# $pagesLoader->isIdArray(array &$a): bool

Source: `wire/core/PagesLoader.php`

Is this an array of IDs? Also sanitizes to all integers when true

## Usage

~~~~~
// basic usage
$bool = $pagesLoader->isIdArray($a);

// usage with all arguments
$bool = $pagesLoader->isIdArray(array &$a);
~~~~~

## Arguments

- `$a` `array`

## Return value

- `bool`
