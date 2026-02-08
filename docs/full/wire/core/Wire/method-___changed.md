# Wire::___changed()

Source: `wire/core/Wire.php`

Hookable method that is called whenever a property has changed while change tracking is enabled.

- Enables hooks to monitor changes to the object.
- Do not call this method directly, as the `Wire::trackChange()` method already does so.
- Descending classes should call `$this->trackChange('name', $oldValue, $newValue);` when a property they are tracking has changed.


@param string $what Name of property that changed

@param mixed $old Previous value before change

@param mixed $new New value

@see Wire::trackChange()
