# SystemUpdaterChecks

Source: `wire/modules/System/SystemUpdater/SystemUpdaterChecks.php`

Class to check for potential issues in the system that may require updates from the admin

All check* methods in this class return true if the check was a success and there are no problem,
or they return false if the check failed and there is a potential issue to resolve.

Methods:
Method: [setShowNotices()](method-setshownotices.md)
Method: [setTestAll()](method-settestall.md)
Method: [execute()](method-execute.md)
Method: [checkIndexFile()](method-checkindexfile.md)
Method: [checkHtaccessFile()](method-checkhtaccessfile.md)
Method: [checkOtherHtaccessFiles()](method-checkotherhtaccessfiles.md)
Method: [checkWelcome()](method-checkwelcome.md)
Method: [checkInstallerFiles()](method-checkinstallerfiles.md)
Method: [checkFilePermissions()](method-checkfilepermissions.md)
Method: [checkPublishedField()](method-checkpublishedfield.md)
Method: [checkLocale()](method-checklocale.md)
Method: [checkDebugMode()](method-checkdebugmode.md)
Method: [checkMemoryLimit()](method-checkmemorylimit.md)
Method: [getMemoryLimit()](method-getmemorylimit.md)
Method: [checkSystemTimes()](method-checksystemtimes.md)
Method: [warning()](method-warning.md)
