# $wireRandom->pass(array $options = array()): string

Source: `wire/core/WireRandom.php`

Generate and return a random password

Default settings of this method are to generate a random but readable password without characters that
tend to have readability issues, and using only ASCII characters (for broadest keyboard compatibility).

## Usage

~~~~~
// basic usage
$string = $wireRandom->pass();

// usage with all arguments
$string = $wireRandom->pass(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` Specify any of the following options (all optional): - `minLength` (int): Minimum lenth of returned value (default=7). - `maxLength` (int): Maximum lenth of returned value, will be exceeded if needed to meet other options (default=15). - `minLower` (int): Minimum number of lowercase characters required (default=1). - `minUpper` (int): Minimum number of uppercase characters required (default=1). - `maxUpper` (int): Maximum number of uppercase characters allowed (0=any, -1=none, default=3). - `minDigits` (int): Minimum number of digits required (default=1). - `maxDigits` (int): Maximum number of digits allowed (0=any, -1=none, default=0). - `minSymbols` (int): Minimum number of non-alpha, non-digit symbols required (default=0). - `maxSymbols` (int): Maximum number of non-alpha, non-digit symbols to allow (0=any, -1=none, default=3). - `useSymbols` (array): Array of characters to use as "symbols" in returned value (see method for default). - `disallow` (array): Disallowed characters that may be confused with others (default=O,0,I,1,l).

## Return value

- `string`
