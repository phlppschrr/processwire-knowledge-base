# $inputfieldWrapper->add($item): Inputfield|InputfieldWrapper|$this

Source: `wire/core/InputfieldWrapper.php`

Add an Inputfield item as a child (also accepts array definition)

Since 3.0.110: If given a string value, it is assumed to be an Inputfield type that you
want to add. In that case, it will create the Inputfield and return it instead of $this.

## Usage

~~~~~
// basic usage
$inputfield = $inputfieldWrapper->add($item);
~~~~~

## Arguments

- `$item` `Inputfield|array|string`

## Return value

- `Inputfield|InputfieldWrapper|$this`

## See Also

- [InputfieldWrapper::import()](method-import.md)
