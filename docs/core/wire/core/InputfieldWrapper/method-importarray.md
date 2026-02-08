# $inputfieldWrapper->importArray(array $a, ?InputfieldWrapper $inputfields = null): $this

Source: `wire/core/InputfieldWrapper.php`

Import an array of Inputfield definitions to to this InputfieldWrapper instance

Your array should be an array of associative arrays, with each element describing an Inputfield.
The following properties are required for each Inputfield definition:

- `type` Which Inputfield module to use (may optionally exclude the "Inputfield" prefix).
- `name` Name attribute to use for the Inputfield.
- `label` Text label that appears above the Inputfield.

~~~~~
// Example array for Inputfield definitions
array(
  array(
    'name' => 'fullname',
    'type' => 'text',
    'label' => 'Field label'
    'columnWidth' => 50,
    'required' => true,
  ),
  array(
    'name' => 'color',
    'type' => 'select',
    'label' => 'Your favorite color',
    'description' => 'Select your favorite color or leave blank if you do not have one.',
    'columnWidth' => 50,
    'options' => array(
       'red' => 'Brilliant Red',
       'orange' => 'Citrus Orange',
       'blue' => 'Sky Blue'
    )
  ),
  // alternative usage: associative array where name attribute is specified as key
  'my_fieldset' => array(
    'type' => 'fieldset',
    'label' => 'My Fieldset',
    'children' => array(
      'some_field' => array(
        'type' => 'text',
        'label' => 'Some Field',
      )
    )
);
// Note: you may alternatively use associative arrays where the keys are assumed to
// be the 'name' attribute.See the last item 'my_fieldset' above for an example.
~~~~~

## Arguments

- array $a Array of Inputfield definitions
- InputfieldWrapper|null $inputfields Specify the wrapper you want them added to, or omit to use current.

## Return value

$this
