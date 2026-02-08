# $pageFinder->findParentIDs($selectors, $options = array()): array

Source: `wire/core/PageFinder.php`

Same as findIDs() but returns the parent IDs of the pages that matched

## Usage

~~~~~
// basic usage
$array = $pageFinder->findParentIDs($selectors);

// usage with all arguments
$array = $pageFinder->findParentIDs($selectors, $options = array());
~~~~~

## Arguments

- `$selectors` `Selectors|string|array` Selectors object, selector string or selector array
- `$options` (optional) `array`

## Return value

- `array` of page parent IDs
