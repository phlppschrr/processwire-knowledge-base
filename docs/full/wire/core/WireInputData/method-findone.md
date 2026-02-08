# WireInputData::findOne()

Source: `wire/core/WireInputData.php`

Find one input var that matches given pattern in name (or optionally value)

@param string $pattern Wildcard string or PCRE regular expression

@param array|int|string $options
 - `type` (string): Specify "value" to match input value (rather input name), OR prefix pattern with "value=".
 - `sanitizer` (string): Name of sanitizer to run values through (default='', none)
 - `arrays` (bool): Also find on input varibles that are arrays? (default=false)

@return string|int|float|array|null $value Returns value if found or null if not.

@since 3.0.163
