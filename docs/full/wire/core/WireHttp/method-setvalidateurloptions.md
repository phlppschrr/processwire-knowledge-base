# $wireHttp->setValidateURLOptions(array $options = array()): array

Source: `wire/core/WireHttp.php`

Set options array given to $sanitizer->url()

It should not be necessary to call this unless you are dealing with an unusual URL that is causing
errors with the default options in WireHttp. Note that the “allowSchemes” option is set separately
with the setAllowSchemes() method in this class.

To return current validate URL options, omit the $options argument.

## Arguments

- `$options` (optional) `array` Options to set, see the $sanitizer->url() method for details on options.

## Return value

array Always returns current options
