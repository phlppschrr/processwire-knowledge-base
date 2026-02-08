# $pagefileExtra->exists($clear = false): bool

Source: `wire/core/PagefileExtra.php`

Does the extra file currently exist?

## Usage

~~~~~
// basic usage
$bool = $pagefileExtra->exists();

// usage with all arguments
$bool = $pagefileExtra->exists($clear = false);
~~~~~

## Arguments

- `$clear` (optional) `bool` Clear stat cache before checking? (default=false)

## Return value

- `bool`
