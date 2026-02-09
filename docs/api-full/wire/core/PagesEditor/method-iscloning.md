# $pagesEditor->isCloning($getDepth = false): bool|int

Source: `wire/core/PagesEditor.php`

Are we currently in a page clone?

## Usage

~~~~~
// basic usage
$bool = $pagesEditor->isCloning();

// usage with all arguments
$bool = $pagesEditor->isCloning($getDepth = false);
~~~~~

## Arguments

- `$getDepth` (optional) `bool` Get depth (int) rather than state (bool)?

## Return value

- `bool|int`
