# $wireCache->expireAll(): int

Source: `wire/core/WireCache.php`

Deletes all caches that have expiration dates (only)

This method does not delete caches that are expired by saving of resources or matching selectors.

## Usage

~~~~~
// basic usage
$int = $wireCache->expireAll();
~~~~~

## Return value

- `int`

## Since

3.0.130
