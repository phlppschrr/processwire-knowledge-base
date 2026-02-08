# $databaseQuerySelectFulltext->forceLike($forceLike = null): bool

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Call forceLike(true) to force use of LIKE, or omit argument to get current setting

This forces LIKE only for matching operators that have a LIKE equivalent.
This includes these operators: `*=`, `^=`, `$=`, `~=`, `~|=`.

## Arguments

- `$forceLike` (optional) `bool|null`

## Return value

bool

## Since

3.0.182
