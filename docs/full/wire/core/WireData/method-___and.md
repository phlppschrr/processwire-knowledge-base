# $wireData->___and($items = null): WireArray

Source: `wire/core/WireData.php`

Take the current item and append the given item(s), returning a new WireArray

This is for syntactic convenience in fluent interfaces.

## Example

~~~~~
if($page->and($page->parents)->has("featured=1")) {
   // page or one of its parents has a featured property with value of 1
}
~~~~~

## Usage

~~~~~
// basic usage
$items = $wireData->___and();

// usage with all arguments
$items = $wireData->___and($items = null);
~~~~~

## Arguments

- `$items` (optional) `WireArray|WireData|string|null` May be any of the following: - `WireData` object (or derivative) - `WireArray` object (or derivative) - Name of any property from this object that returns one of the above. - Omit argument to simply return this object in a WireArray

## Return value

- `WireArray` Returns a WireArray of this object *and* the one(s) given.

## Exceptions

- `WireException` If invalid argument supplied.
