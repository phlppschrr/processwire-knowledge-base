# $tfa->render(): string

Source: `wire/core/Tfa.php`

Render the code input form

“Please enter your authentication code to complete login”

## Usage

~~~~~
// basic usage
$string = $tfa->render();
~~~~~

## Return value

- `string`

## Hooking

- Hookable method name: `render`
- Implementation: `___render`
- Hook with: `Tfa::render`

### Hooking Before

~~~~~
$this->addHookBefore('Tfa::render', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Tfa::render', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
