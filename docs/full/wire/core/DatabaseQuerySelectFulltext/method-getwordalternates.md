# $databaseQuerySelectFulltext->getWordAlternates($word, $minLength = null): array

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Get other variations of given word to search (such as plural, singular, lemmas, etc.)

## Usage

~~~~~
// basic usage
$array = $databaseQuerySelectFulltext->getWordAlternates($word);

// usage with all arguments
$array = $databaseQuerySelectFulltext->getWordAlternates($word, $minLength = null);
~~~~~

## Arguments

- `$word` `string`
- `$minLength` (optional) `int|null` Minimum length for returned words

## Return value

- `array`
