# InputfieldWrapper::add()

Source: `wire/core/InputfieldWrapper.php`

Add an Inputfield item as a child (also accepts array definition)

Since 3.0.110: If given a string value, it is assumed to be an Inputfield type that you
want to add. In that case, it will create the Inputfield and return it instead of $this.


@param Inputfield|array|string $item

@return Inputfield|InputfieldWrapper|$this

@see InputfieldWrapper::import()
