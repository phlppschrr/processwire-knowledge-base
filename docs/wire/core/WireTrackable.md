# WireTrackable

Source: `wire/core/Interfaces.php`

For classes that need to track changes made by other objects.

## setTrackChanges()

Turn change tracking ON or OFF

@param bool|int $trackChanges True to turn on, false to turn off. Integer to specify bitmask.

@return $this

## trackChange()

Track a change to a property in this object

The change will only be recorded if self::$trackChanges is true.

@param string $what Name of property that changed

@param mixed $old Previous value before change

@param mixed $new New value

@return $this

## isChanged()

Has the given property changed?

Applicable only for properties you are tracking while $trackChanges is true.

@param string $what Name of property, or if left blank, check if any properties have changed.

@return bool

## getChanges()

Return an array of properties that have changed while change tracking was on.

@param bool $getValues If true, then an associative array will be retuned with field names and previous values.

@return array
