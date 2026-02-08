# $template->filename($filename = null): string

Source: `wire/core/Template.php`

Return corresponding template filename including path, or set template filename

## Usage

~~~~~
// basic usage
$string = $template->filename();

// usage with all arguments
$string = $template->filename($filename = null);
~~~~~

## Arguments

- `$filename` (optional) `string` Specify basename or path+basename to set, or omit to get filename. This argument added 3.0.143.

## Return value

- `string`

## Exceptions

- `WireException`
