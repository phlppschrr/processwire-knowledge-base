# $inputfield->getConfigInputfields(): InputfieldWrapper

Source: `wire/core/Inputfield.php`

Get any custom configuration fields for this Inputfield

- Intended to be extended by each Inputfield as needed to add more config options.

- The returned InputfieldWrapper ultimately ends up as the "Input" tab in the fields editor (admin).

- Descending Inputfield classes should first call this method from the parent class to get the
  default configuration fields and the InputfieldWrapper they can add to.

- Returned Inputfield instances with a name attribute that starts with an underscore, i.e. "_myname"
  are assumed to be for runtime use and are NOT stored in the database.

- If you prefer, you may instead implement the `Inputfield::getConfigArray()` method as an alternative.

~~~~
// Example getConfigInputfields() implementation
public function ___getConfigInputfields() {
  // Get the defaults and $inputfields wrapper we can add to
  $inputfields = parent::___getConfigInputfields();
  // Add a new Inputfield to it
  $f = $this->wire('modules')->get('InputfieldText');
  $f->attr('name', 'first_name');
  $f->attr('value', $this->get('first_name'));
  $f->label = 'Your First Name';
  $inputfields->add($f);
  return $inputfields;
}
~~~~

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $inputfield->getConfigInputfields();
~~~~~

## Hookable

- Hookable method name: `getConfigInputfields`
- Implementation: `___getConfigInputfields`
- Hook with: `$inputfield->getConfigInputfields()`

## Return value

- `InputfieldWrapper` Populated with Inputfield instances

## See Also

- [Inputfield::getConfigArray()](method-___getconfigarray.md)
