# ModulesDuplicates

Source: `wire/core/ModulesDuplicates.php`

Inherits: `Wire`

ProcessWire Modules Duplicates

Provides functions for managing sitautions where more than one
copy of the same module is intalled. This is a helper for the Modules class.

Methods:
- [`numNewDuplicates(): int`](method-numnewduplicates.md) Return quantity of new duplicates found while loading modules
- [`getCurrent($className): string|null`](method-getcurrent.md) Get the current duplicate in use (string) or null if not specified
- [`hasDuplicate(string $className, string $pathname = ''): bool`](method-hasduplicate.md) Does the given module class have a duplicate?
- [`addDuplicate($className, $pathname, bool $current = false)`](method-addduplicate.md) Add a duplicate to the list
- [`addDuplicates($className, array $files)`](method-addduplicates.md) Add multiple duplicates
- [`addFromConfigData($className, array $data)`](method-addfromconfigdata.md) Add duplicates from module config data
- [`getDuplicates(string|Module|int $className = ''): array`](method-getduplicates.md) Return a list of duplicate modules that were found
- [`setUseDuplicate(string $className, string $pathname)`](method-setuseduplicate.md) For a module that has duplicates, tell it which file to use
- [`updateDuplicates()`](method-updateduplicates.md) Update the database so that modules have information on their duplicates
- [`recordDuplicate(string $basename, string $pathname, string $pathname2, array &$installed)`](method-recordduplicate.md) Record a duplicate at runtime
- [`getDuplicatesConfigData($className, array $configData = array()): array`](method-getduplicatesconfigdata.md) Populate duplicates info into config data, when applicable
