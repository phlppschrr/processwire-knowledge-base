# $wire->__call($method, $arguments): mixed

Source: `wire/core/Wire.php`

Provides the gateway for calling hooks in ProcessWire

When a non-existant method is called, this checks to see if any hooks have been defined and sends the call to them.

Hooks are defined by preceding the "hookable" method in a descending class with 3 underscores, like __myMethod().
When the API calls $myObject->myMethod(), it gets sent to $myObject->___myMethod() after any 'before' hooks have been called.
Then after the ___myMethod() call, any "after" hooks are then called. "after" hooks have the opportunity to change the return value.

Hooks can also be added for methods that don't actually exist in the class, allowing another class to add methods to this class.

See the Wire::runHooks() method for the full implementation of hook calls.

## Arguments

- string $method
- array $arguments

## Return value

mixed

## Throws

- WireException
