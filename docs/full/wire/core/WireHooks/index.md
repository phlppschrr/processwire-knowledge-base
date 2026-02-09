# WireHooks

Source: `wire/core/WireHooks.php`

ProcessWire Hooks Manager

This class is for internal use. You should manipulate hooks from Wire-derived classes instead.

Methods:
- [`__construct(ProcessWire $wire, Config $config)`](method-__construct.md)
- [`getHooks(Wire $object, string $method = '', int $getHooks = self::getHooksAll): array`](method-gethooks.md)
- [`isHooked(string $method, ?Wire $instance = null): bool`](method-ishooked.md)
- [`isHookedOrParents(string|Wire $class, string $method, string $type = 'either'): bool`](method-ishookedorparents.md)
- [`isMethodHooked(string|Wire $class, string $method): bool`](method-ismethodhooked.md)
- [`isPropertyHooked(string|Wire $class, string $property): bool`](method-ispropertyhooked.md)
- [`hasHook(Wire $object, string $method): bool`](method-hashook.md)
- [`getClassParents(Wire|string $object, bool $cache = true): array`](method-getclassparents.md)
- [`addHook(Wire $object, string|array $method, object|null|callable $toObject, string|array $toMethod = null, array $options = array()): string`](method-addhook.md)
- [`addHooks(Wire $object, array|string $methods, object|null|callable $toObject, string|array|null $toMethod = null, array $options = array()): string`](method-addhooks.md)
- [`addPathHook(Wire $object, string $path, Wire|null|callable $toObject, string $toMethod, array $options = array()): string`](method-addpathhook.md)
- [`runHooks(Wire $object, string $method, array $arguments, string|array $type = 'method'): array`](method-runhooks.md)
- [`prepareArgMatch(string $argMatch): array`](method-prepareargmatch.md)
- [`conditionalArgMatch(Selectors|string $argMatch, mixed $argVal, $argMatchType): bool`](method-conditionalargmatch.md)
- [`allowRunPathHook(string $id, array &$arguments): bool`](method-allowrunpathhook.md)
- [`filterHooks(array $hooks, string $property, string|bool|int $value): array`](method-filterhooks.md)
- [`hookTimer(Wire $object, String $method, array $arguments): string`](method-hooktimer.md)
- [`removeHook(Wire $object, string|array|null $hookID): Wire`](method-removehook.md)
- [`removeHooks(Wire $object, array|string $hookIDs): Wire`](method-removehooks.md)
- [`getAllLocalHooks(): array`](method-getalllocalhooks.md)
- [`getAllPathHooks(): array`](method-getallpathhooks.md)
- [`hasPathHooks(string $requestPath = ''): bool`](method-haspathhooks.md)
- [`filterPathHooks(string $requestPath, bool $has = false): array|bool`](method-filterpathhooks.md)
- [`allowPathHooks(bool|null $allow = null): bool`](method-allowpathhooks.md)
- [`getPathHookRedirect(): string`](method-getpathhookredirect.md)
- [`className(): string`](method-classname.md)

Constants:
- [`___debug`](const-___debug.md)
- [`getHooksAll`](const-gethooksall.md)
- [`getHooksLocal`](const-gethookslocal.md)
- [`getHooksStatic`](const-gethooksstatic.md)
