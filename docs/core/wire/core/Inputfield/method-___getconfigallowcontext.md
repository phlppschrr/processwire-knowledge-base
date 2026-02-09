# $inputfield->getConfigAllowContext($field): array

Source: `wire/core/Inputfield.php`

Return a list of config property names allowed for fieldgroup/template context

These should be the names of Inputfields returned by `Inputfield::getConfigInputfields()` or
`Inputfield::getConfigArray()` that are allowed in fieldgroup/template context.

The config property names specified here are allowed to be configured within the context
of a given `Fieldgroup`, enabling the user to configure them independently per template
in the admin.

This is the equivalent to the `Fieldtype::getConfigAllowContext()` method, but for the "Input"
tab rather than the "Details" tab.

## Usage

~~~~~
// basic usage
$array = $inputfield->getConfigAllowContext($field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `array` of Inputfield names

## Hooking

- Hookable method name: `getConfigAllowContext`
- Implementation: `___getConfigAllowContext`
- Hook with: `Inputfield::getConfigAllowContext`

### Hooking Before

~~~~~
$this->addHookBefore('Inputfield::getConfigAllowContext', function(HookEvent $event) {
  $inputfield = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Inputfield::getConfigAllowContext', function(HookEvent $event) {
  $inputfield = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## See Also

- [Fieldtype::getConfigAllowContext()](../Fieldtype/method-___getconfigallowcontext.md)
