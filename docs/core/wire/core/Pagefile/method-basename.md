# $pagefile->basename($ext = true): string

Source: `wire/core/Pagefile.php`

Returns the basename of this Pagefile (name and extension, without disk path).

## Usage

~~~~~
// basic usage
$string = $pagefile->basename();

// usage with all arguments
$string = $pagefile->basename($ext = true);
~~~~~

## Arguments

- `$ext` (optional) `bool` Specify false to exclude the extension (default=true)

## Return value

- `string`
