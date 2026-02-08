# ProcessController::jsonMessage()

Source: `wire/core/ProcessController.php`

Generate a message in JSON format, for use with AJAX output

@param string|array $msg Message string or in 3.0.246+ also accepts an array of extra data
  When using an array, please include a 'message' index with text about the error or non-error.

@param bool $error Is this in error message? Default is true, or specify false if not.

@param bool $allowMarkup Allow markup in message? Applies only to $msg string or 'message' index of array (default=false)

@return string JSON encoded string
