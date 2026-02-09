# $pagesPathFinder->applyPagesRow(array $parts, $row): string

Source: `wire/core/PagesPathFinder.php`

Apply a found pages table row to the $result and return corresponding path

## Usage

~~~~~
// basic usage
$string = $pagesPathFinder->applyPagesRow($parts, $row);

// usage with all arguments
$string = $pagesPathFinder->applyPagesRow(array $parts, $row);
~~~~~

## Arguments

- `$parts` `array`
- `$row` `array|null`

## Return value

- `string` Path string
