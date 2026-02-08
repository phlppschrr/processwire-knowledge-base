# $wireCache->deleteAll(): int

Source: `wire/core/WireCache.php`

Delete all caches (where allowed)

This method deletes all caches other than those with `WireCache::expireReserved` status.

## Usage

~~~~~
// basic usage
$int = $wireCache->deleteAll();
~~~~~

## Return value

- `int` Quantity of caches deleted

## Since

3.0.130
