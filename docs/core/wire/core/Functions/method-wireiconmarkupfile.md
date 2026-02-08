# $functions->wireIconMarkupFile($filename, $class = ''): string

Source: `wire/core/Functions.php`

Get the markup or class name for an icon that can represent the given filename

## Example

~~~~~
// Outputs: "<i class='fa fa-pdf-o'></i>"
echo wireIconMarkupFile('file.pdf');
~~~~~

## Usage

~~~~~
// basic usage
$string = $functions->wireIconMarkupFile($filename);

// usage with all arguments
$string = $functions->wireIconMarkupFile($filename, $class = '');
~~~~~

## Arguments

- `$filename` `string` Can be any type of filename (with or without path).
- `$class` (optional) `string|bool` Additional class attributes, i.e. "fw" for fixed-width (optional). Or specify boolean TRUE to get just the icon class name (no markup).

## Return value

- `string`
