# $wireTextTools->truncateSentenceTests($str, array &$tests, array $endSentenceChars, array $options)

Source: `wire/core/WireTextTools.php`

Helper to truncate() method, generate tests/positions for where sentences end

## Usage

~~~~~
// basic usage
$result = $wireTextTools->truncateSentenceTests($str, $tests, $endSentenceChars, $options);

// usage with all arguments
$result = $wireTextTools->truncateSentenceTests($str, array &$tests, array $endSentenceChars, array $options);
~~~~~

## Arguments

- `$str` `string`
- `$tests` `array` Tests to append found positions to
- `$endSentenceChars` `array`
- `$options` `array` Options provided to truncate method
