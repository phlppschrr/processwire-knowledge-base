# FunctionsWireAPI::wireLog()

Source: `wire/core/FunctionsWireAPI.php`

Access the $log API variable as a function

Default behavior is to return the $log API variable.
If both arguments are provided, it assumes you want to log a message.

@param string $logName If logging a message, specify the name of the log.

@param string $message If logging a message, specify the message text.

@return WireLog|bool Returns bool if saving log entry, WireLog otherwise.
