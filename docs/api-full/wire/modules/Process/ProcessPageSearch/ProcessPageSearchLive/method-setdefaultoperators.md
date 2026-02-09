# $processPageSearchLive->setDefaultOperators($singleWordOperator, $multiWordOperator = '')

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Set default operators to use for searches (if query does not specify operator)

## Usage

~~~~~
// basic usage
$result = $processPageSearchLive->setDefaultOperators($singleWordOperator);

// usage with all arguments
$result = $processPageSearchLive->setDefaultOperators($singleWordOperator, $multiWordOperator = '');
~~~~~

## Arguments

- `$singleWordOperator` `string`
- `$multiWordOperator` (optional) `string`
