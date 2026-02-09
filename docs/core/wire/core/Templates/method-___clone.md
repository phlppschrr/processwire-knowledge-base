# $templates->clone(Saveable $item, $name = ''): bool|Template

Source: `wire/core/Templates.php`

Clone the given Template

Note that this also clones the Fieldgroup if the template being cloned has its own named fieldgroup.

## Usage

~~~~~
// basic usage
$bool = $templates->clone($item);

// usage with all arguments
$bool = $templates->clone(Saveable $item, $name = '');
~~~~~

## Hookable

- Hookable method name: `clone`
- Implementation: `___clone`
- Hook with: `$templates->clone()`

## Hooking Before

~~~~~
$this->addHookBefore('Templates::clone', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $name = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $name);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Templates::clone', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $name = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Template|Saveable` Template to clone
- `$name` (optional) `string` Name of new template that will be created, or omit to auto-assign.

## Return value

- `bool|Template` $item Returns the new Template on success, or false on failure

## Details

- @todo: clone the fieldgroup context settings too.
