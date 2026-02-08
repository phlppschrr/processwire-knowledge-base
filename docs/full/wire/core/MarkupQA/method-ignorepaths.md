# $markupQA->ignorePaths($paths = null, $replace = false): array

Source: `wire/core/MarkupQA.php`

Get or set paths to ignore for link abstraction

To get ignored paths call function with no arguments. Otherwise you are setting them.

## Arguments

- array|string|null $paths Array of paths or string of one path, or CSV or newline separated string of multiple paths.
- bool $replace True to replace all existing paths, or false to merge with existing paths (default=false)

## Return value

array Returns array of current ignore paths

## Throws

- WireException if given invalid $paths argument
