# $databaseQuery->getUniqueBindKey(array $options = array()): string

Source: `wire/core/DatabaseQuery.php`

Get a unique key to use for bind value

Note if you given a `key` option, it will only be used if it is determined unique,
otherwise it’ll auto-generate one. When using your specified key, it is the only
option that applies, unless it is not unique and the method has to auto-generate one.

## Arguments

- array $options - `key` (string): Preferred bind key, or omit (blank) to auto-generate (digit only keys not accepted) - `value` (string|int): Value to use as part of the generated key - `prefix` (string): Prefix to override default - `global` (bool): Require globally unique among all instances?

## Return value

string Returns bind key/name in format ":name" (with leading colon)

## Meta

- @since 3.0.156
