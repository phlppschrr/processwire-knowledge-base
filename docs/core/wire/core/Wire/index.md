# Wire

Source: `wire/core/Wire.php`

ProcessWire Base Class "Wire"

Wire is the base class for most ProcessWire classes and modules.
Wire derived classes have a `$this->wire()` method that provides access to ProcessWire’s API variables.
API variables can also be accessed as local properties in most cases. Wire also provides basic methods
for tracking changes and managing runtime notices specific to the instance.

Wire derived classes can specify which methods are “hookable” by precending the method name with
3 underscores like this: `___myMethod()`. Other classes can then hook either before or after that method,
modifying arguments or return values. Several other hook methods are also provided for Wire derived
classes that are hooking into others.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com



API variables accessible as properties (unless $useFuel has been set to false):


The following map API variables to function names and apply only if another function in the class does not
already have the same name, which would override. All defined API variables can be accessed as functions
that return the API variable, whether documented below or not.


Other standard hookable methods

Groups:
Group: [api-helpers](group-api-helpers.md)
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [__clone()](method-__clone.md)
Method: [getInstanceNum()](method-getinstancenum.md)
Method: [className()](method-classname.md)
Method: [className()](method-classname.md)
Method: [__toString()](method-__tostring.md)
Method: [_wireHooks()](method-_wirehooks.md)
Method: [__call()](method-__call.md)
Method: [___callUnknown()](method-___callunknown.md)
Method: [getHooks()](method-gethooks.md)
Method: [hasHook()](method-hashook.md)
Method: [addHookBefore()](method-addhookbefore.md)
Method: [addHookAfter()](method-addhookafter.md)
Method: [addHookProperty()](method-addhookproperty.md)
Method: [addHookMethod()](method-addhookmethod.md)
Method: [removeHook()](method-removehook.md)
Method: [isChanged()](method-ischanged.md)
Method: [___changed()](method-___changed.md)
Method: [trackChange()](method-trackchange.md)
Method: [untrackChange()](method-untrackchange.md)
Method: [setTrackChanges()](method-settrackchanges.md)
Method: [trackChanges()](method-trackchanges.md)
Method: [resetTrackChanges()](method-resettrackchanges.md)
Method: [getChanges()](method-getchanges.md)
Method: [_notice()](method-_notice.md)
Method: [message()](method-message.md)
Method: [warning()](method-warning.md)
Method: [error()](method-error.md)
Method: [___trackException()](method-___trackexception.md)
Method: [errors()](method-errors.md)
Method: [warnings()](method-warnings.md)
Method: [messages()](method-messages.md)
Method: [___log()](method-___log.md)
Method: [_()](method-_.md)
Method: [_()](method-_.md)
Method: [_x()](method-_x.md)
Method: [_n()](method-_n.md)
Method: [wire()](method-wire.md)
Method: [__get()](method-__get.md)
Method: [__debugInfo()](method-__debuginfo.md)

Constants:
Const: [trackChangesOn](const-trackchangeson.md)
Const: [trackChangesOn](const-trackchangeson.md)
Const: [trackChangesValues](const-trackchangesvalues.md)
