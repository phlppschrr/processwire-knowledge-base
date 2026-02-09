# ModulesDuplicates

Source: `wire/core/ModulesDuplicates.php`

Inherits: `Wire`

ProcessWire Modules Duplicates

Provides functions for managing sitautions where more than one
copy of the same module is intalled. This is a helper for the Modules class.

Methods:
- [`numNewDuplicates(): int`](method-numnewduplicates.md)
- [`getCurrent($className): string|null`](method-getcurrent.md)
- [`hasDuplicate(string $className, string $pathname = ''): bool`](method-hasduplicate.md)
- [`addDuplicate($className, $pathname, bool $current = false)`](method-addduplicate.md)
- [`addDuplicates($className, array $files)`](method-addduplicates.md)
- [`addFromConfigData($className, array $data)`](method-addfromconfigdata.md)
- [`getDuplicates(string|Module|int $className = ''): array`](method-getduplicates.md)
- [`setUseDuplicate(string $className, string $pathname)`](method-setuseduplicate.md)
- [`updateDuplicates()`](method-updateduplicates.md)
- [`recordDuplicate(string $basename, string $pathname, string $pathname2, array &$installed)`](method-recordduplicate.md)
- [`getDuplicatesConfigData($className, array $configData = array()): array`](method-getduplicatesconfigdata.md)
