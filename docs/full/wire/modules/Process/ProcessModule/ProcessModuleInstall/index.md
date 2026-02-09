# ProcessModuleInstall

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Inherits: `Wire`

Installation helper for ProcessModule

Provides methods for internative module installation for ProcessModule

Methods:
- [`getTempDir(): string|bool`](method-gettempdir.md)
- [`canUploadDownload(bool $notify = true, string $type = ''): bool`](method-canuploaddownload.md)
- [`canInstallFromFileUpload(bool $notify = true): bool`](method-caninstallfromfileupload.md)
- [`canInstallFromDownloadUrl(bool $notify = true): bool`](method-caninstallfromdownloadurl.md)
- [`canInstallFromDirectory(bool $notify = true): bool`](method-caninstallfromdirectory.md)
- [`findModuleFiles(string $path = '', int $maxLevel = 4): array`](method-findmodulefiles.md)
- [`determineDestinationDir(array $files, string $modulePath = ''): bool|string`](method-determinedestinationdir.md)
- [`unzipModule(string $zipFile, string $destinationDir = ''): bool|string`](method-unzipmodule.md)
- [`backupDir(string $moduleDir): bool`](method-backupdir.md)
- [`restoreDir(string $moduleDir): bool`](method-restoredir.md)
- [`uploadModule(string $inputName = 'upload_module', string $destinationDir = ''): bool|string`](method-uploadmodule.md)
- [`downloadModule(string $url, string $destinationDir = '', string $type = 'download'): bool|string`](method-downloadmodule.md)
- [`downloadModuleFromUrl(string $url, string $destinationDir = ''): bool|string`](method-downloadmodulefromurl.md)
- [`downloadModuleFromDirectory(string $url, string $destinationDir = ''): bool|string`](method-downloadmodulefromdirectory.md)
- [`installDisabledLabel(string $type): string`](method-installdisabledlabel.md)
