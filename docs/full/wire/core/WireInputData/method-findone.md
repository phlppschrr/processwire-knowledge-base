# $wireInputData->findOne($pattern, $options = array()): string|int|float|array|null

Source: `wire/core/WireInputData.php`

Find one input var that matches given pattern in name (or optionally value)

## Arguments

- string $pattern Wildcard string or PCRE regular expression
- array|int|string $options - `type` (string): Specify "value" to match input value (rather input name), OR prefix pattern with "value=". - `sanitizer` (string): Name of sanitizer to run values through (default='', none) - `arrays` (bool): Also find on input varibles that are arrays? (default=false)

## Return value

string|int|float|array|null $value Returns value if found or null if not.

## Meta

- @since 3.0.163
