# $field->getTags($getString = false): array|string

Source: `wire/core/Field.php`

Get tags

## Usage

~~~~~
// basic usage
$array = $field->getTags();

// usage with all arguments
$array = $field->getTags($getString = false);
~~~~~

## Arguments

- `$getString` (optional) `bool|string` Optionally specify true for space-separated string, or delimiter string (default=false)

## Return value

- `array|string` Returns array of tags unless $getString option is requested

## Since

3.0.106
