# WireFuelable

Source: `wire/core/Interfaces.php`

Interface that indicates a class supports API variable dependency injection and retrieval

## wire()

Get or inject a ProcessWire API variable or fuel a new object instance

See Wire::wire() for explanation of all options.

@param string|WireFuelable $name Name of API variable to retrieve, set, or omit to retrieve entire Fuel object.

@param null|mixed $value Value to set if using this as a setter, otherwise omit.

@param bool $lock When using as a setter, specify true if you want to lock the value from future changes (default=false)

@return mixed|Fuel

@throws WireException

## setWire()

Set the ProcessWire instance

@param ProcessWire $wire

## getWire()

Get the ProcessWire instance

@return ProcessWire
