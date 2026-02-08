# $wireInputData->findOne($pattern, $options = array()): string|int|float|array|null

Source: `wire/core/WireInputData.php`

Find one input var that matches given pattern in name (or optionally value)

## Usage

~~~~~
// basic usage
$string = $wireInputData->findOne($pattern);

// usage with all arguments
$string = $wireInputData->findOne($pattern, $options = array());
~~~~~

## Arguments

- `$pattern` `string` Wildcard string or PCRE regular expression
- `$options` (optional) `array|int|string` - `type` (string): Specify "value" to match input value (rather input name), OR prefix pattern with "value=". - `sanitizer` (string): Name of sanitizer to run values through (default='', none) - `arrays` (bool): Also find on input varibles that are arrays? (default=false)

## Return value

- `string|int|float|array|null` $value Returns value if found or null if not.

## Since

3.0.163
