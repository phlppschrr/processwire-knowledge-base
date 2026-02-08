# $pagefile->hash(): string

Source: `wire/core/Pagefile.php`

Return a unique MD5 hash representing this Pagefile.

This hash can be counted on to be unique among all files on a given page, regardless of field.

## Usage

~~~~~
// basic usage
$string = $pagefile->hash();
~~~~~

## Return value

- `string`
