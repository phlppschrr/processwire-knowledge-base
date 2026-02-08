# $pagefileExtra->url($fallback = true): string

Source: `wire/core/PagefileExtra.php`

Return the URL to the extra file, creating it if it does not already exist

## Usage

~~~~~
// basic usage
$string = $pagefileExtra->url();

// usage with all arguments
$string = $pagefileExtra->url($fallback = true);
~~~~~

## Arguments

- `$fallback` (optional) `bool` Allow falling back to source Pagefile URL when appropriate?

## Return value

- `string`
