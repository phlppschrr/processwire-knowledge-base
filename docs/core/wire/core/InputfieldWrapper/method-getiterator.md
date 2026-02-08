# $inputfieldWrapper->getIterator(): InputfieldsArray

Source: `wire/core/InputfieldWrapper.php`

Enables foreach() of the children of this class

Per the InteratorAggregate interface, make the Inputfield children iterable.

## Usage

~~~~~
// basic usage
$inputfieldsArray = $inputfieldWrapper->getIterator();
~~~~~

## Return value

- `InputfieldsArray`
