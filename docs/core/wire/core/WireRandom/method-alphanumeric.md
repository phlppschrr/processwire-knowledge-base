# $wireRandom->alphanumeric($length = 0, array $options = array()): string

Source: `wire/core/WireRandom.php`

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

## Arguments

- `$length` (optional) `int` Required length of string, or 0 for random length
- `$options` (optional) `array` Options to modify default behavior: - `alpha` (bool): Allow ASCII alphabetic characters? (default=true) - `upper` (bool): Allow uppercase ASCII alphabetic characters? (default=true) - `lower` (bool): Allow lowercase ASCII alphabetic characters? (default=true) - `numeric` (bool): Allow numeric characters 0123456789? (default=true) - `strict` (bool): Require that at least 1 character representing each true option above is present? (default=false) - `allow` (array|string): Only allow these ASCII alpha or digit characters, see notes. (default='') - `disallow` (array|string): Do not allow these characters. (default='') - `require` (array|string): Require that these character(s) are present. (default='') - `extras` (array|string): Also allow these non-alphanumeric extra characters. (default='') - `minLength` (int): If $length argument is 0, minimum length of returned string. (default=10) - `maxLength` (int): If $length argument is 0, maximum length of returned string. (default=40) - `noRepeat` (bool): Prevent same character from appearing more than once in sequence? (default=false) - `noStart` (string|array): Do not start string with these characters. (default='') - 'noEnd` (string|array): Do not end string with these characters. (default='') - `fast` (bool): Use faster method? (default=true if PHP7 or mcrypt available, false if not)

## Return value

string

## Throws

- WireException

## Since

3.0.111
