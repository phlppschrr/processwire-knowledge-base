# $databaseQuerySelectFulltext->getBooleanModeAlternateWords($word, &$booleanValue, $minWordLength, array $options): array

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Helper for getBooleanModeWords to handle population of alternate words in boolean value

## Arguments

- string $word Word to find alternates for
- string &$booleanValue Existing boolean value which will be updated
- int $minWordLength
- array $options

## Return value

array

## Meta

- @since 3.0.162
