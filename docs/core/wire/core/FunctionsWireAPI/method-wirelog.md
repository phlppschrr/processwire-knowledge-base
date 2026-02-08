# $functionsWireAPI->wireLog($logName = '', $message = ''): WireLog|bool

Source: `wire/core/FunctionsWireAPI.php`

Access the $log API variable as a function

Default behavior is to return the $log API variable.
If both arguments are provided, it assumes you want to log a message.

## Arguments

- string $logName If logging a message, specify the name of the log.
- string $message If logging a message, specify the message text.

## Return value

WireLog|bool Returns bool if saving log entry, WireLog otherwise.
