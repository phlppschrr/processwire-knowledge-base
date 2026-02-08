# $databaseQuerySelectFulltext->getBooleanModeWords($value, array $options = array()): array

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Get verbose data array of words identified and prepared for boolean mode

## Usage

~~~~~
// basic usage
$array = $databaseQuerySelectFulltext->getBooleanModeWords($value);

// usage with all arguments
$array = $databaseQuerySelectFulltext->getBooleanModeWords($value, array $options = array());
~~~~~

## Arguments

- `$value` `string`
- `$options` (optional) `array` - `required` (bool): Are given words required in the query? (default=true) - `partial` (bool): Is it okay to match a partial value? i.e. can "will" match "willy" (default=false) - `partialLast` (bool): Use partial only for last word? (default=null, auto-detect) - `partialLess` (bool): Weight partial match words less than full word match? (default=false) - `phrase` (bool): Is entire $value a full phrase to match? (default=auto-detect) - `useStopwords` (bool): Allow inclusion of stopwords? (default=null, auto-detect) - `alternates` (bool): Get word alternates? (default=null, auto-detect)

## Return value

- `array` Value provided to the function with boolean operators added, or verbose array.
