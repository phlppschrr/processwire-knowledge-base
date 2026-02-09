# $tfa->uninstall()

Source: `wire/core/Tfa.php`

Uninstall

Please note: Tfa modules with their own uninstall method must also call parent::___uninstall()

## Usage

~~~~~
// basic usage
$result = $tfa->uninstall();
~~~~~

## Hookable

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `$tfa->uninstall()`

## Hooking Before

~~~~~
$this->addHookBefore('Tfa::uninstall', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Tfa::uninstall', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
