# WireTrackable::trackChange()

Source: `wire/core/Interfaces.php`

Track a change to a property in this object

The change will only be recorded if self::$trackChanges is true.

@param string $what Name of property that changed

@param mixed $old Previous value before change

@param mixed $new New value

@return $this
