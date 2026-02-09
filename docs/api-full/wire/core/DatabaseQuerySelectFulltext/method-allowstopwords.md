# $databaseQuerySelectFulltext->allowStopwords($allow = null): bool

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Get or set whether fulltext searches can fallback to LIKE searches to match stopwords

## Usage

~~~~~
// basic usage
$bool = $databaseQuerySelectFulltext->allowStopwords();

// usage with all arguments
$bool = $databaseQuerySelectFulltext->allowStopwords($allow = null);
~~~~~

## Arguments

- `$allow` (optional) `null|bool` Specify bool to set or omit to get

## Return value

- `bool`

## Since

3.0.162
