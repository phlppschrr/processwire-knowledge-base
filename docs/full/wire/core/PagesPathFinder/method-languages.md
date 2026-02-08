# $pagesPathFinder->languages($getArray = false): Languages|Language[]

Source: `wire/core/PagesPathFinder.php`

Return Languages if installed w/languageSupportPageNames module or blank array if not

## Usage

~~~~~
// basic usage
$languages = $pagesPathFinder->languages();

// usage with all arguments
$languages = $pagesPathFinder->languages($getArray = false);
~~~~~

## Arguments

- `$getArray` (optional) `bool` Force return value as an array indexed by language name

## Return value

- `Languages|Language[]`
