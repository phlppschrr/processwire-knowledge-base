# $pageFinder->count($selectors, $options = array()): int

Source: `wire/core/PageFinder.php`

Return a count of pages that match

## Usage

~~~~~
// basic usage
$int = $pageFinder->count($selectors);

// usage with all arguments
$int = $pageFinder->count($selectors, $options = array());
~~~~~

## Arguments

- `$selectors` `Selectors|string|array` Selectors object, selector string or selector array
- `$options` (optional) `array`

## Return value

- `int`

## Since

3.0.121
