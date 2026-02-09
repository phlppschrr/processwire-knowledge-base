# Wire

Source: `wire/core/Wire.php`

Implements: `WireTranslatable`, `WireFuelable`, `WireTrackable`


Groups:
Group: [api-helpers](group-api-helpers.md)
Group: [other](group-other.md)

ProcessWire Base Class "Wire"

Wire is the base class for most ProcessWire classes and modules.
Wire derived classes have a `$this->wire()` method that provides access to ProcessWire’s API variables.
API variables can also be accessed as local properties in most cases. Wire also provides basic methods
for tracking changes and managing runtime notices specific to the instance.

Wire derived classes can specify which methods are “hookable” by precending the method name with
3 underscores like this: `___myMethod()`. Other classes can then hook either before or after that method,
modifying arguments or return values. Several other hook methods are also provided for Wire derived
classes that are hooking into others.




API variables accessible as properties (unless $useFuel has been set to false):


The following map API variables to function names and apply only if another function in the class does not
already have the same name, which would override. All defined API variables can be accessed as functions
that return the API variable, whether documented below or not.


Other standard hookable methods

Methods:
- [`__construct()`](method-__construct.md)
- [`__clone()`](method-__clone.md)
- [`getInstanceNum(bool $getTotal = false): int`](method-getinstancenum.md)
- [`className($options = null)`](method-classname.md)
- [`className(array|bool|null $options = null): string`](method-classname.md)
- [`__toString(): string`](method-__tostring.md)
- [`_wireHooks(): WireHooks|null`](method-_wirehooks.md)
- [`__call(string $method, array $arguments): mixed`](method-__call.md)
- [`callUnknown(string $method, array $arguments): null|mixed`](method-___callunknown.md) (hookable)
- [`getHooks(string $method = '', int $type = 0): array`](method-gethooks.md)
- [`hasHook(string $name): bool`](method-hashook.md)
- [`addHookBefore(string|array $method, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhookbefore.md)
- [`addHookAfter(string|array $method, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhookafter.md)
- [`addHookProperty(string|array $property, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhookproperty.md)
- [`addHookMethod(string $method, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhookmethod.md)
- [`removeHook(string|array|null $hookId): $this`](method-removehook.md)
- [`isChanged(string $what = ''): bool`](method-ischanged.md)
- [`changed(string $what, mixed $old = null, mixed $new = null)`](method-___changed.md) (hookable)
- [`trackChange(string $what, mixed $old = null, mixed $new = null): $this`](method-trackchange.md)
- [`untrackChange(string $what): $this`](method-untrackchange.md)
- [`setTrackChanges(bool|int $trackChanges = true): $this`](method-settrackchanges.md)
- [`trackChanges(bool $getMode = false): int`](method-trackchanges.md)
- [`resetTrackChanges(bool $trackChanges = true): $this`](method-resettrackchanges.md)
- [`getChanges(bool $getValues = false): array`](method-getchanges.md)
- [`_notice(string|array|Wire $text, int|string $flags, string $name, string $class): $this`](method-_notice.md)
- [`message(string|array|Wire $text, int|bool|string $flags = 0): $this`](method-message.md)
- [`warning(string|array|Wire $text, int|bool|string $flags = 0): $this`](method-warning.md)
- [`error(string|array|Wire $text, int|bool|string $flags = 0): $this`](method-error.md)
- [`trackException(\Throwable $e, bool|int $severe = true, string|array|object|true $text = null): $this`](method-___trackexception.md) (hookable)
- [`errors(string|array $options = array()): Notices|array|string`](method-errors.md)
- [`warnings(string|array $options = array()): Notices|array|string`](method-warnings.md)
- [`messages(string|array $options = array()): Notices|array|string`](method-messages.md)
- [`log(string $str = '', array $options = array()): WireLog`](method-___log.md) (hookable)
- [`_($text)`](method-_.md)
- [`_(string|array $text): string`](method-_.md)
- [`_x(string|array $text, string $context): string`](method-_x.md)
- [`_n(string $textSingular, string $textPlural, int $count): string`](method-_n.md)
- [`wire(string|object $name = '', null|mixed $value = null, bool $lock = false): ProcessWire|Wire|Session|Page|Pages|Modules|User|Users|Roles|Permissions|Templates|Fields|Fieldtypes|Sanitizer|Config|Notices|WireDatabasePDO|WireHooks|WireDateTime|WireFileTools|WireMailTools|WireInput|PagesVersions|string|mixed`](method-wire.md)
- [`__get(string $name): mixed|null`](method-__get.md)
- [`__debugInfo(): array`](method-__debuginfo.md)

Constants:
- [`trackChangesOn`](const-trackchangeson.md)
- [`trackChangesOn`](const-trackchangeson.md)
- [`trackChangesValues`](const-trackchangesvalues.md)
