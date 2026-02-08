# WireNumberTools

Source: `wire/core/WireNumberTools.php`

Tools for working with numbers

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

@since 3.0.213

## uniqueNumber()

Generate and return an installation unique number/ID (integer)

- Numbers returned by this method are incrementing, starting from 1.
- Unique number counter stored in the database so is unique aross all time/requests.
- Returned number is guaranteed to be unique among other calls to this method.
- When using the `namespace` option, it will generate a new DB table for that namespace.
- Use the `reset` option to delete a namespace when no longer needed.
- You cannot reset the default namespace, so any caller is always assured a unique number.
- This method creates table names that begin with `unique_num`.

@param array|string $options Array of options or string for the namespace option.
 - `namespace` (string): Optional namespace for unique numbers, in table name format [_a-zA-Z0-9] (default='')
 - `getLast` (bool): Get last unique number rather than generating new one? (default=false)
 - `reset` (bool): Reset numbers in namespace by deleting its table? Namespace required (default=false)

@return int Returns unique number,
 or returns 0 if `reset` option is used,
 or returns 0 if `getLast` option is used and no numbers exist.

@throws WireException

@since 3.0.213

## randomInteger()

Return a random integer (cryptographically secure when available)

@param int $min Minimum value (default=0)

@param int $max Maximum value (default=PHP_INT_MAX)

@param bool $throw Throw WireException if we cannot achieve a cryptographically secure random number? (default=false)

@return int

@since 3.0.214

## strToBytes()

Given a value like "1M", "2MB", "3 kB", "4 GB", "5tb" etc. return quantity of bytes

Spaces, commas and case in given value do not matter. Only the first character of the unit is
taken into account, whether it appears in the given value, or is given in the $unit argument.
Meaning a unit like megabytes (for example) can be specified as 'm', 'mb', 'megabytes', etc.

@param string|int|float $value

@param string|null $unit Optional unit that given value is in (b, kb, mb, gb, tb), or omit to auto-detect

@return int

@since 3.0.214

## bytesToStr()

Given a quantity of bytes (int), return readable string that refers to quantity in bytes, kB, MB, GB and TB

@param int|string $bytes Quantity in bytes (int) or any string accepted by strToBytes method.

@param array|int $options Options to modify default behavior, or if an integer then `decimals` option is assumed:
 - `decimals` (int|null): Number of decimals to use in returned value or NULL for auto (default=null).
    When null (auto) a decimal value of 1 is used when appropriate, for megabytes and higher (3.0.214+).
 - `decimal_point` (string|null): Decimal point character, or null to detect from locale (default=null).
 - `thousands_sep` (string|null): Thousands separator, or null to detect from locale (default=null).
 - `small` (bool|int): Make returned string as small as possible? false=no, true=yes, 1=yes with space (default=false)
 - `labels` (array): Labels to use for units, indexed by: b, byte, bytes, k, m, g, t
 - `type` (string): To force return value as specific type, specify one of: bytes, kilobytes, megabytes,
    gigabytes, terabytes; or just: b, k, m, g, t. (3.0.148+ only, terabytes 3.0.214+).

@return string

@since 3.0.214 All versions can also use the wireBytesStr() function

## locale()

Get a number formatting property from current locale

In multi-language environments, this method’s return values are affected by the
current language locale.

@param string $key Property to get or omit to get all properties. Properties include:
 - `decimal_point`: Decimal point character
 - `thousands_sep`: Thousands separator
 - `currency_symbol`: Local currency symbol (i.e. $)
 - `int_curr_symbol`: International currency symbol (i.e. USD)
 - `mon_decimal_point`: Monetary decimal point character
 - `mon_thousands_sep`: Monetary thousands separator
 - `positive_sign`: Sign for positive values
 - `negative_sign`: Sign for negative values
 - `clear`: Clear any cached values for current language/locale.
 - See <https://www.php.net/manual/en/function.localeconv.php> for more.

@return array|string|int|null
