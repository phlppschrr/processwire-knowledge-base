# $inputfield->___getConfigArray(): array

Source: `wire/core/Inputfield.php`

Alternative method for configuration that allows for array definition

- This method is typically used instead of the `Inputfield::getConfigInputfields` method
  for module authors that prefer to use the array definition.

- If both `getConfigInputfields()` and `getConfigArray()` are implemented, both will be used.

- See comments for `InputfieldWrapper::importArray()` for example of array definition.

~~~~~
// Example implementation
public function ___getConfigArray() {
  return [
    'test' => [
      'type' => 'text',
      'label' => 'This is a test',
      'value' => 'Test'
    ]
  ];
);
~~~~~

## Return value

array
