# $wireRandom->string($length = 0, $characters = '', array $options = []): string

Source: `wire/core/WireRandom.php`

Generate a random string using given characters

## Arguments

- int $length Length of string or specify 0 for random length
- string $characters Charaacters to use for random string or omit for partial ASCII set
- array $options - `minLength` (int): Minimum allowed length if length argument is 0 (default=10) - `maxLength` (int): Maximum allowed length if length argument is 0 (default=40) - `fast` (bool): Use a faster randomization method? (default=false)

## Return value

string

## Meta

- @since 3.0.251
