# ProcessModuleInstall

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Inherits: `Wire`

Installation helper for ProcessModule

Provides methods for internative module installation for ProcessModule

Methods:
- [`getTempDir(): string|bool`](method-gettempdir.md) Returns a temporary directory (path) for use by this object
- [`canUploadDownload(bool $notify = true, string $type = ''): bool`](method-canuploaddownload.md) Check that the system supports direct upload and download of modules
- [`canInstallFromFileUpload(bool $notify = true): bool`](method-caninstallfromfileupload.md) Module upload allowed?
- [`canInstallFromDownloadUrl(bool $notify = true): bool`](method-caninstallfromdownloadurl.md) Module download from URL allowed?
- [`canInstallFromDirectory(bool $notify = true): bool`](method-caninstallfromdirectory.md) Module install/upgrade from directory allowed?
- [`findModuleFiles(string $path = '', int $maxLevel = 4): array`](method-findmodulefiles.md) Find all module files, recursively in Path
- [`determineDestinationDir(array $files, string $modulePath = ''): bool|string`](method-determinedestinationdir.md) Given a list of files from a module (and their temp dir) return the recommended directory name for it to live in
- [`unzipModule(string $zipFile, string $destinationDir = ''): bool|string`](method-unzipmodule.md) Unzip the module file to tempDir and then copy to destination directory
- [`backupDir(string $moduleDir): bool`](method-backupdir.md) Create a backup of a module directory
- [`restoreDir(string $moduleDir): bool`](method-restoredir.md) Restore a module directory
- [`uploadModule(string $inputName = 'upload_module', string $destinationDir = ''): bool|string`](method-uploadmodule.md) Process a module upload
- [`downloadModule(string $url, string $destinationDir = '', string $type = 'download'): bool|string`](method-downloadmodule.md) Given a URL to a ZIP file, download it, unzip it, and move to /site/modules/[ModuleName]
- [`downloadModuleFromUrl(string $url, string $destinationDir = ''): bool|string`](method-downloadmodulefromurl.md) Download module from URL
- [`downloadModuleFromDirectory(string $url, string $destinationDir = ''): bool|string`](method-downloadmodulefromdirectory.md) Download module from directory
- [`installDisabledLabel(string $type): string`](method-installdisabledlabel.md) Return label to indicate option is disabled and how to enable it
