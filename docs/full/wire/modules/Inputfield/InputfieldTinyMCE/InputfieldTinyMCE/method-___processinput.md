# $inputfieldTinyMCE->processInput(WireInputData $input): $this

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Process input

## Usage

~~~~~
// basic usage
$result = $inputfieldTinyMCE->processInput($input);

// usage with all arguments
$result = $inputfieldTinyMCE->processInput(WireInputData $input);
~~~~~

## Arguments

- `$input` `WireInputData`

## Return value

- `$this`

## Hooking

- Hookable method name: `processInput`
- Implementation: `___processInput`
- Hook with: `InputfieldTinyMCE::processInput`

### Hooking Before

~~~~~
$this->addHookBefore('InputfieldTinyMCE::processInput', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Get arguments
  $input = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $input);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('InputfieldTinyMCE::processInput', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Get arguments
  $input = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
