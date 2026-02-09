# $field->getInputfield(Page $page, $contextStr = ''): Inputfield|null

Source: `wire/core/Field.php`

Get the Inputfield module used to collect input for this field.

## Usage

~~~~~
// basic usage
$inputfield = $field->getInputfield($page);

// usage with all arguments
$inputfield = $field->getInputfield(Page $page, $contextStr = '');
~~~~~

## Hookable

- Hookable method name: `getInputfield`
- Implementation: `___getInputfield`
- Hook with: `$field->getInputfield()`

## Hooking Before

~~~~~
$this->addHookBefore('Field::getInputfield', function(HookEvent $event) {
  $field = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $contextStr = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $contextStr);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Field::getInputfield', function(HookEvent $event) {
  $field = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $contextStr = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page that the Inputfield is for.
- `$contextStr` (optional) `string` Optional context string to append to the Inputfield's name/id (for repeaters and such).

## Return value

- `Inputfield|null`
