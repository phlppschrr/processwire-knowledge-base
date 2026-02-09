# $pageFinder->getPageArrayData(?PageArray $pageArray = null): array

Source: `wire/core/PageFinder.php`

Get data that should be populated back to any resulting PageArray’s data() method

## Usage

~~~~~
// basic usage
$array = $pageFinder->getPageArrayData();

// usage with all arguments
$array = $pageFinder->getPageArrayData(?PageArray $pageArray = null);
~~~~~

## Arguments

- `$pageArray` (optional) `PageArray|null` Optionally populate given PageArray

## Return value

- `array`
