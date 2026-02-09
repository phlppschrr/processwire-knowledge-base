# $page->getInputfields($fieldName = ''): null|InputfieldWrapper

Source: `wire/core/Page.php`

Hookable version of getInputfields() method.

See the getInputfields() method above for documentation details.

## Usage

~~~~~
// basic usage
$page->getInputfields();

// usage with all arguments
$page->getInputfields($fieldName = '');
~~~~~

## Arguments

- `$fieldName` (optional) `string|array`

## Return value

- `null|InputfieldWrapper` Returns an InputfieldWrapper array of Inputfield objects, or NULL on failure.

## Hooking

- Hookable method name: `getInputfields`
- Implementation: `___getInputfields`
- Hook with: `Page::getInputfields`

### Hooking Before

~~~~~
$this->addHookBefore('Page::getInputfields', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $fieldName = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fieldName);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::getInputfields', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $fieldName = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
