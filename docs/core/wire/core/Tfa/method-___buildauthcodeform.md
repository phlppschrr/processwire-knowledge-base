# $tfa->buildAuthCodeForm(): InputfieldForm

Source: `wire/core/Tfa.php`

Build the form used for two-factor authentication

This form typically appears on the screen after the user has submitted their login info

At minimum it must have an Inputfield with name “tfa_code”

## Usage

~~~~~
// basic usage
$inputfieldForm = $tfa->buildAuthCodeForm();
~~~~~

## Hookable

- Hookable method name: `buildAuthCodeForm`
- Implementation: `___buildAuthCodeForm`
- Hook with: `$tfa->buildAuthCodeForm()`

## Hooking Before

~~~~~
$this->addHookBefore('Tfa::buildAuthCodeForm', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Tfa::buildAuthCodeForm', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `InputfieldForm`
