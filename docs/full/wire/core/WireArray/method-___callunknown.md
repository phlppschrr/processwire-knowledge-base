# $wireArray->callUnknown($method, $arguments): null|mixed

Source: `wire/core/WireArray.php`

Handler for when an unknown/unhooked method call is executed

If interested in hooking this, please see the `Wire::callUnknown()` method for more
details on the purpose and potential hooking implementation of this method.

The implementation built-in to WireArray provides a couple of handy capabilities to all
WireArray derived classes (assuming that `$items` is an instance of any WireArray):

- It enables you to call `$items->foobar()` and receive a regular PHP array
  containing the value of the "foobar" property from each item in this WireArray.
  It is equivalent to calling `$items->explode('foobar')`. Of course, substitute
  "foobar" with the name of any property present on items in the WireArray.

- It enables you to call `$items->foobar(", ")` and receive a string containing
  the value of the "foobar" property from each item, delimited by the string you
  provided as an argument (a comma and space ", " in this case). This is equivalent
  to calling `$items->implode(", ", "foobar")`.

- Also note that if you call `$items->foobar(", ", $options)` where $options is an
  array, it is equivalent to `$items->implode(", ", "foobar", $options)`.

## Example

~~~~~
// Get array of all "title" values from each item
$titlesArray = $items->title();

// Get a newline separated string of all "title" values from each item
$titlesString = $items->title("\n");
~~~~~

## Usage

~~~~~
// basic usage
$wireArray->callUnknown($method, $arguments);
~~~~~

## Hookable

- Hookable method name: `callUnknown`
- Implementation: `___callUnknown`
- Hook with: `$wireArray->callUnknown()`

## Arguments

- `$method` `string` Requested method name
- `$arguments` `array` Arguments provided to the method

## Return value

- `null|mixed`

## Exceptions

- `WireException`
