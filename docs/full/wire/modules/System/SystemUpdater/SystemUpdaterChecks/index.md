# SystemUpdaterChecks

Source: `wire/modules/System/SystemUpdater/SystemUpdaterChecks.php`

Inherits: `Wire`

Class to check for potential issues in the system that may require updates from the admin

All check* methods in this class return true if the check was a success and there are no problem,
or they return false if the check failed and there is a potential issue to resolve.

Methods:
- [`setShowNotices(bool $showNotices = true)`](method-setshownotices.md) Set whether or not to show verbose notices
- [`setTestAll(bool $testAll = true)`](method-settestall.md) Set whether or not to test all checks (as if all checks failed)
- [`execute(): array`](method-execute.md) Run all system checks and return array of results
- [`checkIndexFile(): bool`](method-checkindexfile.md) Check that index.php file is the correct version
- [`checkHtaccessFile(): bool`](method-checkhtaccessfile.md) Check that main htaccess file is the correct version
- [`checkOtherHtaccessFiles(): bool`](method-checkotherhtaccessfiles.md) Check that other useful htaccess files are present
- [`checkWelcome(): bool`](method-checkwelcome.md) Check if this is the first call to checkWelcome and show a welcome message and add an active.php file if so
- [`checkInstallerFiles(): bool`](method-checkinstallerfiles.md) Check if unnecessary installer files are present
- [`checkFilePermissions(): bool`](method-checkfilepermissions.md) Check for insecure file permissions
- [`checkPublishedField(): bool`](method-checkpublishedfield.md) Check if there is a field named 'published' that should not be present
- [`checkLocale(): bool`](method-checklocale.md) Check locale setting
- [`checkDebugMode()`](method-checkdebugmode.md) Check for debug mode
- [`checkMemoryLimit(): bool`](method-checkmemorylimit.md) Check PHP memory_limit setting
- [`getMemoryLimit(string $getInUnit = 'M'): int|float`](method-getmemorylimit.md) Get memory limit
- [`checkSystemTimes(): bool`](method-checksystemtimes.md) Check that database time and PHP time match
