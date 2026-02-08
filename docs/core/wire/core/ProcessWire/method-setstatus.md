# ProcessWire::setStatus()

Source: `wire/core/ProcessWire.php`

Set the system status to one of the ProcessWire::status* constants

This also triggers init/ready functions for modules, when applicable.

@param int $status

@param array $data Associative array of any extra data to pass along to include files as locally scoped vars (3.0.142+)
