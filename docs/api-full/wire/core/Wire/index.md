# Wire

Source: `wire/core/Wire.php`

Implements: `WireTranslatable`, `WireFuelable`, `WireTrackable`

## Summary

ProcessWire Base Class "Wire"

Common methods:
- [`getInstanceNum()`](method-getinstancenum.md)
- [`setFuel()`](method-setfuel.md)
- [`getFuel()`](method-getfuel.md)
- [`getAllFuel()`](method-getallfuel.md)
- [`fuel()`](method-fuel.md)

Groups:
Group: [api-helpers](group-api-helpers.md)
Group: [other](group-other.md)

Wire is the base class for most ProcessWire classes and modules.
Wire derived classes have a `$this->wire()` method that provides access to ProcessWire’s API variables.
API variables can also be accessed as local properties in most cases. Wire also provides basic methods
for tracking changes and managing runtime notices specific to the instance.

Wire derived classes can specify which methods are “hookable” by precending the method name with
3 underscores like this: `___myMethod()`. Other classes can then hook either before or after that method,
modifying arguments or return values. Several other hook methods are also provided for Wire derived
classes that are hooking into others.




API variables accessible as properties (unless `$useFuel` has been set to false):


The following map API variables to function names and apply only if another function in the class does not
already have the same name, which would override. All defined API variables can be accessed as functions
that return the API variable, whether documented below or not.


Other standard hookable methods

## Methods
- [`__construct()`](method-__construct.md) Construct
- [`__clone()`](method-__clone.md) Clone this Wire instance
- [`getInstanceNum(bool $getTotal = false): int`](method-getinstancenum.md) Get this Wire object’s instance number
- [`className(array|bool|null $options = null): string`](method-classname.md) Return this object’s class name
- [`__toString(): string`](method-__tostring.md) Unless overridden, classes descending from Wire return their class name when typecast as a string
- [`_wireHooks(): WireHooks|null`](method-_wirehooks.md)
- [`__call(string $method, array $arguments): mixed`](method-__call.md) Provides the gateway for calling hooks in ProcessWire
- [`callUnknown(string $method, array $arguments): null|mixed`](method-___callunknown.md) (hookable) If method call resulted in no handler, this hookable method is called.
- [`getHooks(string $method = '', int $type = 0): array`](method-gethooks.md) Return all hooks associated with this class instance or method (if specified)
- [`hasHook(string $name): bool`](method-hashook.md) Returns true if the method or property is hooked, false if it isn’t.
- [`addHookBefore(string|array $method, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhookbefore.md) Add a hook to be executed before the hooked method
- [`addHookAfter(string|array $method, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhookafter.md) Add a hook to be executed after the hooked method
- [`addHookProperty(string|array $property, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhookproperty.md) Add a hook that will be accessible as a new object property.
- [`addHookMethod(string $method, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhookmethod.md) Add a hook accessible as a new public method in a class (or object)
- [`removeHook(string|array|null $hookId): $this`](method-removehook.md) Given a Hook ID, remove the hook
- [`isChanged(string $what = ''): bool`](method-ischanged.md) Does the object have changes, or has the given property changed?
- [`changed(string $what, mixed $old = null, mixed $new = null)`](method-___changed.md) (hookable) Hookable method that is called whenever a property has changed while change tracking is enabled.
- [`trackChange(string $what, mixed $old = null, mixed $new = null): $this`](method-trackchange.md) Track a change to a property in this object
- [`untrackChange(string $what): $this`](method-untrackchange.md) Untrack a change to a property in this object
- [`setTrackChanges(bool|int $trackChanges = true): $this`](method-settrackchanges.md) Turn change tracking ON or OFF
- [`trackChanges(bool $getMode = false): int`](method-trackchanges.md) Returns true or 1 if change tracking is on, or false or 0 if it is not, or mode bitmask (int) if requested.
- [`resetTrackChanges(bool $trackChanges = true): $this`](method-resettrackchanges.md) Clears out any tracked changes and turns change tracking ON or OFF
- [`getChanges(bool $getValues = false): array`](method-getchanges.md) Return an array of properties that have changed while change tracking was on.
- [`_notice(string|array|Wire $text, int|string $flags, string $name, string $class): $this`](method-_notice.md) Record a Notice, internal use (contains the code for message, warning and error methods)
- [`message(string|array|Wire $text, int|bool|string $flags = 0): $this`](method-message.md) Record an informational or “success” message in the system-wide notices.
- [`warning(string|array|Wire $text, int|bool|string $flags = 0): $this`](method-warning.md) Record a warning error message in the system-wide notices.
- [`error(string|array|Wire $text, int|bool|string $flags = 0): $this`](method-error.md) Record an non-fatal error message in the system-wide notices.
- [`trackException(\Throwable $e, bool|int $severe = true, string|array|object|true $text = null): $this`](method-___trackexception.md) (hookable) Hookable method called when an Exception (or Error) occurs
- [`errors(string|array $options = array()): Notices|array|string`](method-errors.md) Return or manage errors recorded by just this object or all Wire objects
- [`warnings(string|array $options = array()): Notices|array|string`](method-warnings.md) Return or manage warnings recorded by just this object or all Wire objects
- [`messages(string|array $options = array()): Notices|array|string`](method-messages.md) Return or manage messages recorded by just this object or all Wire objects
- [`log(string $str = '', array $options = array()): WireLog`](method-___log.md) (hookable) Log a message for this class
- [`_(string|array $text): string`](method-_.md) Translate the given text string into the current language if available.
- [`_x(string|array $text, string $context): string`](method-_x.md) Perform a language translation in a specific context
- [`_n(string $textSingular, string $textPlural, int $count): string`](method-_n.md) Perform a language translation with singular and plural versions
- [`wire(string|object $name = '', null|mixed $value = null, bool $lock = false): ProcessWire|Wire|Session|Page|Pages|Modules|User|Users|Roles|Permissions|Templates|Fields|Fieldtypes|Sanitizer|Config|Notices|WireDatabasePDO|WireHooks|WireDateTime|WireFileTools|WireMailTools|WireInput|PagesVersions|string|mixed`](method-wire.md) Get an API variable, create an API variable, or inject dependencies.
- [`__get(string $name): mixed|null`](method-__get.md) Get an object property by direct reference or NULL if it doesn't exist
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method

## Constants
- [`trackChangesOn = 2`](const-trackchangeson.md)
- [`trackChangesValues = 4`](const-trackchangesvalues.md)
