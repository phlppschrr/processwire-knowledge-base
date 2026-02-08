# $wireNumberTools->uniqueNumber($options = array()): int

Source: `wire/core/WireNumberTools.php`

Generate and return an installation unique number/ID (integer)

- Numbers returned by this method are incrementing, starting from 1.
- Unique number counter stored in the database so is unique aross all time/requests.
- Returned number is guaranteed to be unique among other calls to this method.
- When using the `namespace` option, it will generate a new DB table for that namespace.
- Use the `reset` option to delete a namespace when no longer needed.
- You cannot reset the default namespace, so any caller is always assured a unique number.
- This method creates table names that begin with `unique_num`.

## Arguments

- `$options` (optional) `array|string` Array of options or string for the namespace option. - `namespace` (string): Optional namespace for unique numbers, in table name format [_a-zA-Z0-9] (default='') - `getLast` (bool): Get last unique number rather than generating new one? (default=false) - `reset` (bool): Reset numbers in namespace by deleting its table? Namespace required (default=false)

## Return value

int Returns unique number, or returns 0 if `reset` option is used, or returns 0 if `getLast` option is used and no numbers exist.

## Throws

- WireException

## Since

3.0.213
