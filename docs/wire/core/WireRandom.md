# WireRandom

Source: `wire/core/WireRandom.php`

Random generators for ProcessWire

Includes methods for random strings, numbers, arrays and passwords.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

@since 3.0.111

Usage example
~~~~~
$random = new WireRandom();
$s = $random->alphanumeric(10);
$i = $random->integer(0, 10);
~~~~~

## alphanumeric()

Return random alphanumeric, alpha or numeric string

This method uses cryptographically secure random generation unless you specify `true` for
the `fast` option, in which case it will use cryptographically secure method only if PHP is
version 7+ or the mcrypt library is available.

**Note about the `allow` option:**
If this option is used, it overrides the `alpha` and `numeric` options and creates a
string that has only the given characters. If given characters are not ASCII alpha or
numeric, then the `fast` option is always used, as the crypto-secure option does not
support non-alphanumeric characters. When the `allow` option is used, the `strict`
option does not apply.

@param int $length Required length of string, or 0 for random length

@param array $options Options to modify default behavior:
 - `alpha` (bool): Allow ASCII alphabetic characters? (default=true)
 - `upper` (bool): Allow uppercase ASCII alphabetic characters? (default=true)
 - `lower` (bool): Allow lowercase ASCII alphabetic characters? (default=true)
 - `numeric` (bool): Allow numeric characters 0123456789? (default=true)
 - `strict` (bool): Require that at least 1 character representing each true option above is present? (default=false)
 - `allow` (array|string): Only allow these ASCII alpha or digit characters, see notes. (default='')
 - `disallow` (array|string): Do not allow these characters. (default='')
 - `require` (array|string): Require that these character(s) are present. (default='')
 - `extras` (array|string): Also allow these non-alphanumeric extra characters. (default='')
 - `minLength` (int): If $length argument is 0, minimum length of returned string. (default=10)
 - `maxLength` (int): If $length argument is 0, maximum length of returned string. (default=40)
 - `noRepeat` (bool): Prevent same character from appearing more than once in sequence? (default=false)
 - `noStart` (string|array): Do not start string with these characters. (default='')
 - 'noEnd` (string|array): Do not end string with these characters. (default='')
 - `fast` (bool): Use faster method? (default=true if PHP7 or mcrypt available, false if not)

@return string

@throws WireException

@since 3.0.111

## string1()

Generate a random string using faster method

@param int $length Required length

@param string $allowed Characters allowed

@param array $options
 - `noRepeat` (bool): True if two of the same character may not be repeated in sequence.

@return string

## string2()

Generate random string using method that pulls from the base64 method

@param int $length Required length

@param string $allowed Allowed characters

@param array $options See options for alphanumeric() method

@return string

## alpha()

Return string of random ASCII alphabetical letters

@param int $length Required length of string or 0 for random length

@param array $options See options for alphanumeric() method

@return string

@since 3.0.111

## numeric()

Return string of random numbers/digits

@param int $length Required length of string or 0 for random length

@param array $options See options for alphanumeric() method

@return string

@since 3.0.111

## string()

Generate a random string using given characters

@param int $length Length of string or specify 0 for random length

@param string $characters Charaacters to use for random string or omit for partial ASCII set

@param array $options
 - `minLength` (int): Minimum allowed length if length argument is 0 (default=10)
 - `maxLength` (int): Maximum allowed length if length argument is 0 (default=40)
 - `fast` (bool): Use a faster randomization method? (default=false)

@return string

@since 3.0.251

## integer()

Get a random integer

@param int $min Minimum allowed value (default=0).

@param int $max Maximum allowed value (default=PHP_INT_MAX).

@param array $options
 - `info` (bool): Return array of [value, type] indicating what type of random generator was used? (default=false).
 - `cryptoSecure` (bool): Throw WireException if cryptographically secure type not available (default=false).

@return int|array Returns integer, or will return array if $info option specified.

@throws WireException

## arrayItem()

Get a random item (or items, key or keys) from the given array

- Given array may be regular or associative.

- If given a `qty` other than 1 (default) then the `getArray` option is assumed true, unless a
  different value for the `getArray` option was manually specified.

- When using the `getArray` option, returned array will have keys retained, except when `qty`
  option exceeds the number of items in given array `$a`, then keys will not be retained.

@param array $a Array to get random item from

@param array $options Options to modify behavior:
 - `qty` (int): Return this quantity of item(s) (default=1).
 - `getKey` (bool): Return item key(s) rather than values.
 - `getArray` (bool): Return array (with original keys) rather than value (default=false if qty==1, true if not).

@return mixed|array|null

## arrayValue()

Get a random value from given array

@param array $a Array to get random value from

@return mixed|null

## arrayValues()

Return a random version of given array or a quantity of random items

Array keys are retained in return value, unless requested $qty exceeds
the quantity of items in given array.

@param array $a Array to get random items from.

@param int $qty Quantity of items, or 0 to return all (default=0).

@return array

## arrayKey()

Get a random key from given array

@param array $a

@return string|int

## arrayKeys()

Get a random version of all keys in given array (or a specified quantity of them)

@param array $a Array to get random keys from.

@param int $qty Quantity of unique keys to return or 0 for all (default=0)

@return array

## shuffle()

Shuffle a string or an array

Unlike PHP’s shuffle() function, this method:

- Accepts strings or arrays and returns the same type.
- Maintains array keys, if given an array.
- Returns a copy of the value rather than modifying the given value directly.
- Is cryptographically secure if PHP7 or mcrypt available.

@param string|array $value

@return string|array

## pass()

Generate and return a random password

Default settings of this method are to generate a random but readable password without characters that
tend to have readability issues, and using only ASCII characters (for broadest keyboard compatibility).

@param array $options Specify any of the following options (all optional):
 - `minLength` (int): Minimum lenth of returned value (default=7).
 - `maxLength` (int): Maximum lenth of returned value, will be exceeded if needed to meet other options (default=15).
 - `minLower` (int): Minimum number of lowercase characters required (default=1).
 - `minUpper` (int): Minimum number of uppercase characters required (default=1).
 - `maxUpper` (int): Maximum number of uppercase characters allowed (0=any, -1=none, default=3).
 - `minDigits` (int): Minimum number of digits required (default=1).
 - `maxDigits` (int): Maximum number of digits allowed (0=any, -1=none, default=0).
 - `minSymbols` (int): Minimum number of non-alpha, non-digit symbols required (default=0).
 - `maxSymbols` (int): Maximum number of non-alpha, non-digit symbols to allow (0=any, -1=none, default=3).
 - `useSymbols` (array): Array of characters to use as "symbols" in returned value (see method for default).
 - `disallow` (array): Disallowed characters that may be confused with others (default=O,0,I,1,l).

@return string

## passCreate()

Create a password (for password method)

@param array $options

@return string

## passTrunc()

Truncate password to requested maxLength without removing required options (for password method)

@param string $value

@param array $options See options from password() method

@return string

## base64()

Generate a truly random base64 string of a certain length

This is largely taken from Anthony Ferrara's password_compat library:
https://github.com/ircmaxell/password_compat/blob/master/lib/password.php
Modified for camelCase, variable names, and function-based context by Ryan.

@param int $requiredLength Length of string you want returned (default=22)

@param array|bool $options Specify array of options or boolean to specify only `fast` option.
 - `fast` (bool): Use fastest, not cryptographically secure method (default=false).
 - `test` (bool|array): Return tests in a string (bool true), or specify array(true) to return tests array (default=false).
   Note that if the test option is used, then the fast option is disabled.

@return string|array Returns only array if you specify array for $test argument, otherwise returns string

## randomBufferToSalt()

Given random buffer string of bytes return base64 encoded salt

@param string $buffer

@param int $requiredLength

@return string

## cryptoSecure()

Is a crypto secure method of generating numbers available?

@return bool

## _strlen()

Return string length, using mb_strlen() when available, or strlen() when not

@param string $s

@return int
