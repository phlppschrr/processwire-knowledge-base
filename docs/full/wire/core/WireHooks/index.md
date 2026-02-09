# WireHooks

Source: `wire/core/WireHooks.php`

ProcessWire Hooks Manager

This class is for internal use. You should manipulate hooks from Wire-derived classes instead.

Methods:
- [`__construct(ProcessWire $wire, Config $config)`](method-__construct.md) Construct WireHooks
- [`getHooks(Wire $object, string $method = '', int $getHooks = self::getHooksAll): array`](method-gethooks.md) Return all hooks associated with $object or method (if specified)
- [`isHooked(string $method, ?Wire $instance = null): bool`](method-ishooked.md) Returns true if the method/property hooked, false if it isn't.
- [`isHookedOrParents(string|Wire $class, string $method, string $type = 'either'): bool`](method-ishookedorparents.md) Similar to isHooked() method but also checks parent classes for the hooked method as well
- [`isMethodHooked(string|Wire $class, string $method): bool`](method-ismethodhooked.md) Similar to isHooked() method but also checks parent classes for the hooked method as well
- [`isPropertyHooked(string|Wire $class, string $property): bool`](method-ispropertyhooked.md) Similar to isHooked() method but also checks parent classes for the hooked property as well
- [`hasHook(Wire $object, string $method): bool`](method-hashook.md) Similar to isHooked(), returns true if the method or property hooked, false if it isn't.
- [`getClassParents(Wire|string $object, bool $cache = true): array`](method-getclassparents.md) Get an array of parent classes and interfaces for the given object
- [`addHook(Wire $object, string|array $method, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhook.md) Hook a function/method to a hookable method call in this object
- [`addHooks(Wire $object, array|string $methods, object|null|callable $toObject, string|array|null $toMethod = null, array $options = array()): string`](method-addhooks.md) Add a hooks to multiple methods at once
- [`addPathHook(Wire $object, string $path, Wire|null|callable $toObject, string $toMethod, array $options = array()): string`](method-addpathhook.md) Add a hook that handles a request path
- [`runHooks(Wire $object, string $method, array $arguments, string|array $type = 'method'): array`](method-runhooks.md) Provides the implementation for calling hooks in ProcessWire
- [`prepareArgMatch(string $argMatch): array`](method-prepareargmatch.md) Prepare argument match
- [`conditionalArgMatch(Selectors|string $argMatch, mixed $argVal, $argMatchType): bool`](method-conditionalargmatch.md) Does given value match given match condition?
- [`allowRunPathHook(string $id, array &$arguments): bool`](method-allowrunpathhook.md) Allow given path hook to run?
- [`filterHooks(array $hooks, string $property, string|bool|int $value): array`](method-filterhooks.md) Filter and return hooks matching given property and value
- [`hookTimer(Wire $object, String $method, array $arguments): string`](method-hooktimer.md) Start timing a hook and return the timer name
- [`removeHook(Wire $object, string|array|null $hookID): Wire`](method-removehook.md) Given a Hook ID provided by addHook() this removes the hook
- [`removeHooks(Wire $object, array|string $hookIDs): Wire`](method-removehooks.md) Given a hook ID or multiple hook IDs (in array or CSV string) remove the hooks
- [`getAllLocalHooks(): array`](method-getalllocalhooks.md) Return the "all local hooks" cache
- [`getAllPathHooks(): array`](method-getallpathhooks.md) Return all pending path hooks
- [`hasPathHooks(string $requestPath = ''): bool`](method-haspathhooks.md) Return whether or not any path hooks are pending
- [`filterPathHooks(string $requestPath, bool $has = false): array|bool`](method-filterpathhooks.md) Return path hooks that have potential to match given request path
- [`allowPathHooks(bool|null $allow = null): bool`](method-allowpathhooks.md) Get or set whether path hooks are allowed
- [`getPathHookRedirect(): string`](method-getpathhookredirect.md) Return redirect URL required by an applicable path hook, or blank otherwise
- [`className(): string`](method-classname.md)

Constants:
- [`___debug`](const-___debug.md)
- [`getHooksAll`](const-gethooksall.md)
- [`getHooksLocal`](const-gethookslocal.md)
- [`getHooksStatic`](const-gethooksstatic.md)
