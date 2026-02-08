# $wireInput->getValidInputValue(WireInputData $input, $key, $valid, $fallback): array|int|mixed|null|WireInputData|string

Source: `wire/core/WireInput.php`

Provides the implementation for get/post/cookie method validation and fallback features

## Arguments

- `$input` `WireInputData`
- `$key` `string` Name of variable to pull from $input
- `$valid` `array|string|callable|mixed|null` String containing name of Sanitizer method, or array of allowed values.
- `$fallback` `string|array|int|mixed` Return this value rather than null if input value is not present or not valid.

## Return value

array|int|mixed|null|WireInputData|string

## Throws

- WireException if given unknown Sanitizer method or some other invalid arguments.
