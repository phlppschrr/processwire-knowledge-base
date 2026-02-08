# $pagesPathFinder->addResultError($name, $message, $force = false)

Source: `wire/core/PagesPathFinder.php`

Add named error message to result

## Usage

~~~~~
// basic usage
$result = $pagesPathFinder->addResultError($name, $message);

// usage with all arguments
$result = $pagesPathFinder->addResultError($name, $message, $force = false);
~~~~~

## Arguments

- `$name` `string`
- `$message` `string`
- `$force` (optional) `bool` Force add even if not in verbose mode? (default=false)
