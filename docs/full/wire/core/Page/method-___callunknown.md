# Page::___callUnknown()

Source: `wire/core/Page.php`

If method call resulted in no handler, this hookable method is called.

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


@param string $method Requested method name

@param array $arguments Arguments provided

@return null|mixed Return value of method (if applicable)

@throws WireException

@see Wire::callUnknown()
