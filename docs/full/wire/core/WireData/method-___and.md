# WireData::___and()

Source: `wire/core/WireData.php`

Take the current item and append the given item(s), returning a new WireArray

This is for syntactic convenience in fluent interfaces.
~~~~~
if($page->and($page->parents)->has("featured=1")) {
   // page or one of its parents has a featured property with value of 1
}
~~~~~


@param WireArray|WireData|string|null $items May be any of the following:
  - `WireData` object (or derivative)
  - `WireArray` object (or derivative)
  - Name of any property from this object that returns one of the above.
  - Omit argument to simply return this object in a WireArray

@return WireArray Returns a WireArray of this object *and* the one(s) given.

@throws WireException If invalid argument supplied.
