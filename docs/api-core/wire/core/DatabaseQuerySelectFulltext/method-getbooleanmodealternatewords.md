# $databaseQuerySelectFulltext->getBooleanModeAlternateWords($word, &$booleanValue, $minWordLength, array $options): array

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Helper for getBooleanModeWords to handle population of alternate words in boolean value

## Usage

~~~~~
// basic usage
$array = $databaseQuerySelectFulltext->getBooleanModeAlternateWords($word, $booleanValue, $minWordLength, $options);

// usage with all arguments
$array = $databaseQuerySelectFulltext->getBooleanModeAlternateWords($word, &$booleanValue, $minWordLength, array $options);
~~~~~

## Arguments

- `$word` `string` Word to find alternates for
- string &$booleanValue Existing boolean value which will be updated
- `$minWordLength` `int`
- `$options` `array`

## Return value

- `array`

## Since

3.0.162
