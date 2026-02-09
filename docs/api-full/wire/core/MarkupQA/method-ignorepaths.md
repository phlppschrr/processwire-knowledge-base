# $markupQA->ignorePaths($paths = null, $replace = false): array

Source: `wire/core/MarkupQA.php`

Get or set paths to ignore for link abstraction

To get ignored paths call function with no arguments. Otherwise you are setting them.

## Usage

~~~~~
// basic usage
$array = $markupQA->ignorePaths();

// usage with all arguments
$array = $markupQA->ignorePaths($paths = null, $replace = false);
~~~~~

## Arguments

- `$paths` (optional) `array|string|null` Array of paths or string of one path, or CSV or newline separated string of multiple paths.
- `$replace` (optional) `bool` True to replace all existing paths, or false to merge with existing paths (default=false)

## Return value

- `array` Returns array of current ignore paths

## Exceptions

- `WireException` if given invalid $paths argument
