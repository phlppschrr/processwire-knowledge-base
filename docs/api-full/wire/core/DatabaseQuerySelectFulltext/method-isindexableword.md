# $databaseQuerySelectFulltext->isIndexableWord($word): bool

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Is given word not a stopword and long enough to be indexed?

## Usage

~~~~~
// basic usage
$bool = $databaseQuerySelectFulltext->isIndexableWord($word);
~~~~~

## Arguments

- `$word` `string`

## Return value

- `bool`
