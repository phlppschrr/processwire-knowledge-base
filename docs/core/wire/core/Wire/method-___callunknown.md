# $wire->___callUnknown($method, $arguments): null|mixed

Source: `wire/core/Wire.php`

If method call resulted in no handler, this hookable method is called.

This standard implementation just throws an exception. This is a template method, so the reason it
exists is so that other classes can override and provide their own handler. Classes that provide
their own handler should not do a `parent::__callUnknown()` unless they also fail, as that will
cause an exception to be thrown.

If you want to override this method with a hook, see the example below.
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

## Arguments

- `$method` `string` Requested method name
- `$arguments` `array` Arguments provided

## Return value

null|mixed Return value of method (if applicable)

## Throws

- WireException
