# $selectors->extractValueQuick(&$str, $openingQuote, $closingQuote): false|string|string[]

Source: `wire/core/Selectors.php`

Early-exit optimizations for extractValue

## Usage

~~~~~
// basic usage
$result = $selectors->extractValueQuick($str, $openingQuote, $closingQuote);

// usage with all arguments
$result = $selectors->extractValueQuick(&$str, $openingQuote, $closingQuote);
~~~~~

## Arguments

- `$str` `string` String to extract value from, $str will be modified if extraction successful
- `$openingQuote` `string` Opening quote character, if string has them, blank string otherwise
- `$closingQuote` `string` Closing quote character, if string has them, blank string otherwise

## Return value

- `false|string|string[]` Returns found value if successful, boolean false if not
