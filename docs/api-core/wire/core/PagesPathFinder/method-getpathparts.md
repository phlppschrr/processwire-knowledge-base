# $pagesPathFinder->getPathParts($path): array

Source: `wire/core/PagesPathFinder.php`

Prepare $path and convert to array of $parts

If language segment detected then remove it and populate language to result

## Usage

~~~~~
// basic usage
$array = $pagesPathFinder->getPathParts($path);
~~~~~

## Arguments

- `$path` `string`

## Return value

- `array`
