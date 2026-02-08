# WireData::setQuietly()

Source: `wire/core/WireData.php`

Same as set() but without change tracking

- If `$this->trackChanges()` is false, then this is no different than set(), since changes aren't being tracked.
- If `$this->trackChanges()` is true, then the value will be set quietly (i.e. not recorded in the changes list).


@param string $key Name of property you want to set

@param mixed $value Value of property

@return $this

@see Wire::trackChanges(), WireData::set()
