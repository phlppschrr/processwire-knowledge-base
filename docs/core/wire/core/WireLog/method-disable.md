# WireLog::disable()

Source: `wire/core/WireLog.php`

Disable the given log name temporarily so that save() calls do not record entries during this request

@param string $name Log name or specify '*' to disable all

@return self

@since 3.0.148

@see WireLog::enable()
