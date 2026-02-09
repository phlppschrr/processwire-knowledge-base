# $page->callUnknown($method, $arguments): null|mixed

Source: `wire/core/Page.php`

If method call resulted in no handler, this hookable method is called.

If you want to override this method with a hook, see the example below.

## Example

~~~~~
$wire->addHookBefore('Wire::callUnknown', function(HookEvent $event) {
  // Get information about unknown method that was called
  $methodObject = $event->object;
  $methodName = $event->arguments(0); // string
  $methodArgs = $event->arguments(1); // array
  // The replace option replaces the method and blocks the exception
  $event->replace = true;
  // Now do something with the information you have, for example
  // you might want to populate a value to $event->return if
  // you want the unknown method to return a value.
});
~~~~~

## Usage

~~~~~
// basic usage
$page->callUnknown($method, $arguments);
~~~~~

## Hookable

- Hookable method name: `callUnknown`
- Implementation: `___callUnknown`
- Hook with: `$page->callUnknown()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::callUnknown', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $method = $event->arguments(0);
  $arguments = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $method);
  $event->arguments(1, $arguments);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Page::callUnknown', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $method = $event->arguments(0);
  $arguments = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$method` `string` Requested method name
- `$arguments` `array` Arguments provided

## Return value

- `null|mixed` Return value of method (if applicable)

## Exceptions

- `WireException`

## See Also

- [Wire::callUnknown()](../Wire/method-___callunknown.md)
