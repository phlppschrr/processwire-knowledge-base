# SystemUpdaterChecks

Source: `wire/modules/System/SystemUpdater/SystemUpdaterChecks.php`

Inherits: `Wire`

Class to check for potential issues in the system that may require updates from the admin

All check* methods in this class return true if the check was a success and there are no problem,
or they return false if the check failed and there is a potential issue to resolve.

Methods:
- [`setShowNotices(bool $showNotices = true)`](method-setshownotices.md)
- [`setTestAll(bool $testAll = true)`](method-settestall.md)
- [`execute(): array`](method-execute.md)
- [`checkIndexFile(): bool`](method-checkindexfile.md)
- [`checkHtaccessFile(): bool`](method-checkhtaccessfile.md)
- [`checkOtherHtaccessFiles(): bool`](method-checkotherhtaccessfiles.md)
- [`checkWelcome(): bool`](method-checkwelcome.md)
- [`checkInstallerFiles(): bool`](method-checkinstallerfiles.md)
- [`checkFilePermissions(): bool`](method-checkfilepermissions.md)
- [`checkPublishedField(): bool`](method-checkpublishedfield.md)
- [`checkLocale(): bool`](method-checklocale.md)
- [`checkDebugMode()`](method-checkdebugmode.md)
- [`checkMemoryLimit(): bool`](method-checkmemorylimit.md)
- [`getMemoryLimit(string $getInUnit = 'M'): int|float`](method-getmemorylimit.md)
- [`checkSystemTimes(): bool`](method-checksystemtimes.md)
- [`warning($text, $flags = 0)`](method-warning.md)
