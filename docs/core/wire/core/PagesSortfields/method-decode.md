# $pagesSortfields->decode($sortfield, $default = 'sort'): string

Source: `wire/core/PagesSortfields.php`

Decodes a sortfield from a signed integer or string to a field name

The returned fieldname is preceded with a dash if the sortfield is reversed.

## Usage

~~~~~
// basic usage
$string = $pagesSortfields->decode($sortfield);

// usage with all arguments
$string = $pagesSortfields->decode($sortfield, $default = 'sort');
~~~~~

## Arguments

- `$sortfield` `string|int`
- `$default` (optional) `string` Default sortfield name (default='sort')

## Return value

- `string`
