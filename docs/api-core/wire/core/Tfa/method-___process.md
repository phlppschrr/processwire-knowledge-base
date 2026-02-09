# $tfa->process(): User|bool

Source: `wire/core/Tfa.php`

Process two-factor authentication code input

This method processes the submission of the form containing “tfa_code”.
Note that this method will perform redirects as needed.

## Usage

~~~~~
// basic usage
$user = $tfa->process();
~~~~~

## Return value

- `User|bool` Returns logged-in user object on successful code completion, or false on fail

## Hooking

- Hookable method name: `process`
- Implementation: `___process`
- Hook with: `Tfa::process`

### Hooking Before

~~~~~
$this->addHookBefore('Tfa::process', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Tfa::process', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
