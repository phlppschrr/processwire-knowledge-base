# $databaseQuerySelectFulltext->getBooleanModeAlternateWords($word, &$booleanValue, $minWordLength, array $options): array

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Helper for getBooleanModeWords to handle population of alternate words in boolean value

## Arguments

- `$word` `string` Word to find alternates for
- string &$booleanValue Existing boolean value which will be updated
- `$minWordLength` `int`
- `$options` `array`

## Return value

array

## Since

3.0.162
