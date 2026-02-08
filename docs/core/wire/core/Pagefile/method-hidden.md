# $pagefile->hidden($set = null)

Source: `wire/core/Pagefile.php`

Get or set hidden state of this file

Files that are hidden do not appear in the formatted field value,
but do appear in the unformatted value.

## Usage

~~~~~
// basic usage
$result = $pagefile->hidden();

// usage with all arguments
$result = $pagefile->hidden($set = null);
~~~~~

## Arguments

- `$set` (optional) `bool|null`

## Since

3.0.237
