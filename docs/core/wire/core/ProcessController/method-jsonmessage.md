# $processController->jsonMessage($msg, $error = false, $allowMarkup = false): string

Source: `wire/core/ProcessController.php`

Generate a message in JSON format, for use with AJAX output

## Arguments

- string|array $msg Message string or in 3.0.246+ also accepts an array of extra data When using an array, please include a 'message' index with text about the error or non-error.
- bool $error Is this in error message? Default is true, or specify false if not.
- bool $allowMarkup Allow markup in message? Applies only to $msg string or 'message' index of array (default=false)

## Return value

string JSON encoded string
