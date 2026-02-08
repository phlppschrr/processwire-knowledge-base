# DatabaseQuerySelectFulltext::forceLike()

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Call forceLike(true) to force use of LIKE, or omit argument to get current setting

This forces LIKE only for matching operators that have a LIKE equivalent.
This includes these operators: `*=`, `^=`, `$=`, `~=`, `~|=`.

@param bool|null $forceLike

@return bool

@since 3.0.182
