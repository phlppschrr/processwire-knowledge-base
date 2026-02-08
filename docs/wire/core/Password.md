# Password

Source: `wire/core/Password.php`

ProcessWire Password Fieldtype

Class to hold combined password/salt info. Uses Blowfish when possible.
Specially used by FieldtypePassword.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@method setPass($value) Protected internal use method

@property string $salt

@property string $hash

@property-write string $pass

## matches()

Does this Password match the given string?

@param string $pass Password to compare

@return bool

## __get()

Get a property via direct access ('salt' or 'hash')


@param string $name

@return mixed

## __set()

Set a property


@param string $key

@param mixed $value

## ___setPass()

Set the 'pass' to the given value

@param string $value

@throws WireException if given invalid $value

## salt()

Generate a random salt for the given hashType

@return string

## randomBase64String()

Generate a truly random base64 string of a certain length

See WireRandom::base64() for details

@param int $requiredLength Length of string you want returned (default=22)

@param array|bool $options Specify array of options or boolean to specify only `fast` option.
 - `fast` (bool): Use fastest, not cryptographically secure method (default=false).
 - `test` (bool|array): Return tests in a string (bool true), or specify array(true) to return tests array (default=false).
   Note that if the test option is used, then the fast option is disabled.

@return string|array Returns only array if you specify array for $test argument, otherwise returns string

## isBlowfish()

Returns whether the given string is blowfish hashed

@param string $str

@return bool

## supportsBlowfish()

Returns whether the current system supports Blowfish

@return bool

## hash()

Given an unhashed password, generate a hash of the password for database storage and comparison

Note: When blowfish, returns the entire blowfish string which has the salt as the first 28 characters.

@param string $pass Raw password

@return string

@throws WireException

## randomAlpha()

Return a pseudo-random alpha or alphanumeric character

This method may be deprecated at some point, so it is preferable to use the
`randomLetters()` or `randomAlnum()` methods instead, when you can count on
the PW version being 3.0.109 or higher.

@param int $qty Number of random characters requested

@param bool $alphanumeric Specify true to allow digits in return value

@param array $disallow Characters that may not be used in return value

@return string

@deprecated use WireRandom::alpha() instead

## randomAlnum()

Return cryptographically secure random alphanumeric, alpha or numeric string

@param int $length Required length of string, or 0 for random length

@param array $options See WireRandom::alphanumeric() for options

@return string

@throws WireException

@since 3.0.109

@deprecated use WireRandom::alphanumeric() instead

## randomLetters()

Return string of random letters

@param int $length Required length of string or 0 for random length

@param array $options See options for randomAlnum() method

@return string

@since 3.0.109

@deprecated use WireRandom::alpha() instead.

## randomDigits()

Return string of random digits

@param int $length Required length of string or 0 for random length

@param array $options See WireRandom::numeric() method

@return string

@since 3.0.109

@deprecated Use WireRandom::numeric() instead

## randomPass()

Generate and return a random password

See WireRandom::pass() method for details.

@param array $options See WireRandom::pass() for options

@return string

## random()

@return WireRandom
