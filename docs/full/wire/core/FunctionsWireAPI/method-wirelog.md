# $functionsWireAPI->wireLog($logName = '', $message = ''): WireLog|bool

Source: `wire/core/FunctionsWireAPI.php`

Access the $log API variable as a function

Default behavior is to return the $log API variable.
If both arguments are provided, it assumes you want to log a message.

## Arguments

- `$logName` (optional) `string` If logging a message, specify the name of the log.
- `$message` (optional) `string` If logging a message, specify the message text.

## Return value

WireLog|bool Returns bool if saving log entry, WireLog otherwise.
