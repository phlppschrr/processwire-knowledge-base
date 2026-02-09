# $inputfield->getConfigArray(): array

Source: `wire/core/Inputfield.php`

Alternative method for configuration that allows for array definition

- This method is typically used instead of the `Inputfield::getConfigInputfields` method
  for module authors that prefer to use the array definition.

- If both `getConfigInputfields()` and `getConfigArray()` are implemented, both will be used.

- See comments for `InputfieldWrapper::importArray()` for example of array definition.

## Example

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

## Usage

~~~~~
// basic usage
$array = $inputfield->getConfigArray();
~~~~~

## Return value

- `array`

## Hooking

- Hookable method name: `getConfigArray`
- Implementation: `___getConfigArray`
- Hook with: `Inputfield::getConfigArray`

### Hooking Before

~~~~~
$this->addHookBefore('Inputfield::getConfigArray', function(HookEvent $event) {
  $inputfield = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Inputfield::getConfigArray', function(HookEvent $event) {
  $inputfield = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
