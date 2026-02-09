# $inputfieldWrapper->processInput(WireInputData $input): $this

Source: `wire/core/InputfieldWrapper.php`

Process input for all children

## Usage

~~~~~
// basic usage
$result = $inputfieldWrapper->processInput($input);

// usage with all arguments
$result = $inputfieldWrapper->processInput(WireInputData $input);
~~~~~

## Arguments

- `$input` `WireInputData`

## Return value

- `$this`

## Hooking

- Hookable method name: `processInput`
- Implementation: `___processInput`
- Hook with: `InputfieldWrapper::processInput`

### Hooking Before

~~~~~
$this->addHookBefore('InputfieldWrapper::processInput', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Get arguments
  $input = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $input);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('InputfieldWrapper::processInput', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Get arguments
  $input = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
