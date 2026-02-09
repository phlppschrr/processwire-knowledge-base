# $languageParser->buildMatch(array $m, $key, $text): array

Source: `wire/modules/LanguageSupport/LanguageParser.php`

Build the match abstracted away from the preg_match result

## Usage

~~~~~
// basic usage
$array = $languageParser->buildMatch($m, $key, $text);

// usage with all arguments
$array = $languageParser->buildMatch(array $m, $key, $text);
~~~~~

## Arguments

- `$m` `array`
- `$key` `int`
- `$text` `string`

## Return value

- `array`
