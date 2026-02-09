# $processController->jsonMessage($msg, $error = false, $allowMarkup = false): string

Source: `wire/core/ProcessController.php`

Generate a message in JSON format, for use with AJAX output

## Usage

~~~~~
// basic usage
$string = $processController->jsonMessage($msg);

// usage with all arguments
$string = $processController->jsonMessage($msg, $error = false, $allowMarkup = false);
~~~~~

## Arguments

- `$msg` `string|array` Message string or in 3.0.246+ also accepts an array of extra data When using an array, please include a 'message' index with text about the error or non-error.
- `$error` (optional) `bool` Is this in error message? Default is true, or specify false if not.
- `$allowMarkup` (optional) `bool` Allow markup in message? Applies only to $msg string or 'message' index of array (default=false)

## Return value

- `string` JSON encoded string
