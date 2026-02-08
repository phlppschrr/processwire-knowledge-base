# $functions->wireIsCallable($var, $syntaxOnly = false, &$callableName = ''): bool

Source: `wire/core/Functions.php`

Is the given $var callable as a function?

ProcessWire namespace aware version of PHP’s is_callable() function

## Usage

~~~~~
// basic usage
$bool = $functions->wireIsCallable($var);

// usage with all arguments
$bool = $functions->wireIsCallable($var, $syntaxOnly = false, &$callableName = '');
~~~~~

## Arguments

- `$var` `string|callable`
- `$syntaxOnly` (optional) `bool`

## Return value

- `bool`

## Details

- @var string $callableName
