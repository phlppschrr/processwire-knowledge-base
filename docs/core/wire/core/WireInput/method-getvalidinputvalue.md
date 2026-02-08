# WireInput::getValidInputValue()

Source: `wire/core/WireInput.php`

Provides the implementation for get/post/cookie method validation and fallback features

@param WireInputData $input

@param string $key Name of variable to pull from $input

@param array|string|callable|mixed|null $valid String containing name of Sanitizer method, or array of allowed values.

@param string|array|int|mixed $fallback Return this value rather than null if input value is not present or not valid.

@return array|int|mixed|null|WireInputData|string

@throws WireException if given unknown Sanitizer method or some other invalid arguments.
