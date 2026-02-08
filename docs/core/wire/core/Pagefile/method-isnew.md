# $pagefile->isNew($set = null): bool

Source: `wire/core/Pagefile.php`

Get or set “new” status of the Pagefile

This is true with a Pagefile that was created during this request and not loaded from DB.

## Usage

~~~~~
// basic usage
$bool = $pagefile->isNew();

// usage with all arguments
$bool = $pagefile->isNew($set = null);
~~~~~

## Arguments

- `$set` (optional) `bool|null`

## Return value

- `bool`
