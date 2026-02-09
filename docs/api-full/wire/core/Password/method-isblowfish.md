# $password->isBlowfish($str = ''): bool

Source: `wire/core/Password.php`

Returns whether the given string is blowfish hashed

## Usage

~~~~~
// basic usage
$bool = $password->isBlowfish();

// usage with all arguments
$bool = $password->isBlowfish($str = '');
~~~~~

## Arguments

- `$str` (optional) `string`

## Return value

- `bool`
