# $password->randomBase64String($requiredLength = 22, $options = array()): string|array

Source: `wire/core/Password.php`

Generate a truly random base64 string of a certain length

See WireRandom::base64() for details

## Usage

~~~~~
// basic usage
$string = $password->randomBase64String();

// usage with all arguments
$string = $password->randomBase64String($requiredLength = 22, $options = array());
~~~~~

## Arguments

- `$requiredLength` (optional) `int` Length of string you want returned (default=22)
- `$options` (optional) `array|bool` Specify array of options or boolean to specify only `fast` option. - `fast` (bool): Use fastest, not cryptographically secure method (default=false). - `test` (bool|array): Return tests in a string (bool true), or specify array(true) to return tests array (default=false). Note that if the test option is used, then the fast option is disabled.

## Return value

- `string|array` Returns only array if you specify array for $test argument, otherwise returns string
