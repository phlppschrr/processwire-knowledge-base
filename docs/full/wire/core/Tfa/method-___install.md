# $tfa->install()

Source: `wire/core/Tfa.php`

Module module and other assets required to execute it

Please note: Tfa modules with their own install method must also call parent::___install()

## Usage

~~~~~
// basic usage
$result = $tfa->install();
~~~~~

## Hookable

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `$tfa->install()`

## Hooking Before

~~~~~
$this->addHookBefore('Tfa::install', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Tfa::install', function(HookEvent $event) {
  $tfa = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
