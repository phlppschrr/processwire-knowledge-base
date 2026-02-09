# $wireAction->getConfigInputfields(): InputfieldWrapper

Source: `wire/core/WireAction.php`

Return any Inputfields needed to configure this action

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $wireAction->getConfigInputfields();
~~~~~

## Return value

- `InputfieldWrapper`

## Hooking

- Hookable method name: `getConfigInputfields`
- Implementation: `___getConfigInputfields`
- Hook with: `WireAction::getConfigInputfields`

### Hooking Before

~~~~~
$this->addHookBefore('WireAction::getConfigInputfields', function(HookEvent $event) {
  $wireAction = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireAction::getConfigInputfields', function(HookEvent $event) {
  $wireAction = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
