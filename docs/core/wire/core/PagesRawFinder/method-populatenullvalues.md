# $pagesRawFinder->populateNullValues(&$values)

Source: `wire/core/PagesRaw.php`

Populate null values for requested fields that were not present (the 'nulls' option)

Applies only if specific fields were requested.

## Usage

~~~~~
// basic usage
$result = $pagesRawFinder->populateNullValues($values);

// usage with all arguments
$result = $pagesRawFinder->populateNullValues(&$values);
~~~~~

## Since

3.0.198

## Details

- @var array $values
