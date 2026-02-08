# WireInput::requestMethod()

Source: `wire/core/WireInput.php`

Return the current request method (i.e. GET, POST, etc.) or blank if not known

Possible return values are:
- GET
- POST
- HEAD
- PUT
- DELETE
- OPTIONS
- or blank if not known

@param string $method Optionally enter the request method to return bool if current method matches

@return string|bool

@since 3.0.39
