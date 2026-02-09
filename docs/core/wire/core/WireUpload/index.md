# WireUpload

Source: `wire/core/WireUpload.php`

Inherits: `Wire`

ProcessWire WireUpload

Saves uploads of single or multiple files, saving them to the destination path.
If the destination path does not exist, it will be created.

Methods:
- [`__construct(string $name)`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`init()`](method-init.md)
- [`__destruct()`](method-__destruct.md)
- [`execute(): array`](method-execute.md)
- [`getPhpFiles(): array|bool`](method-getphpfiles.md)
- [`getUploadDir(): string`](method-getuploaddir.md)
- [`getPhpFilesAjax(): array|bool`](method-getphpfilesajax.md)
- [`isValidExtension(string $name): bool`](method-isvalidextension.md)
- [`isValidUpload(string $name, int $size, int $error): bool`](method-isvalidupload.md)
- [`checkDestinationPath(): bool`](method-checkdestinationpath.md)
- [`getUniqueFilename(string $destination): string`](method-getuniquefilename.md)
- [`validateFilename(string $value, array $extensions = array()): bool|string`](method-validatefilename.md)
- [`saveUpload(string $tmp_name, string $filename, bool $ajax = false): array|bool|string`](method-saveupload.md)
- [`saveUploadZip(string $zipFile): array|bool`](method-saveuploadzip.md)
- [`getCompletedFilenames(): array`](method-getcompletedfilenames.md)
- [`addUploadedFilename(string $completedFilename, string $originalFilename)`](method-adduploadedfilename.md)
- [`getOriginalFilenames(): array`](method-getoriginalfilenames.md)
- [`setTargetFilename($filename)`](method-settargetfilename.md)
- [`getTargetFilename(string $filename): string`](method-gettargetfilename.md)
- [`setOverwriteFilename(string $filename): $this`](method-setoverwritefilename.md)
- [`setValidExtensions(array $extensions): $this`](method-setvalidextensions.md)
- [`setMaxFiles(int $maxFiles): $this`](method-setmaxfiles.md)
- [`setMaxFileSize(int $bytes): $this`](method-setmaxfilesize.md)
- [`setOverwrite(bool $overwrite): $this`](method-setoverwrite.md)
- [`setDestinationPath(string $destinationPath): $this`](method-setdestinationpath.md)
- [`setExtractArchives(bool $extract = true): $this`](method-setextractarchives.md)
- [`setName(string $name): $this`](method-setname.md)
- [`setLowercase(bool $lowercase = true): $this`](method-setlowercase.md)
- [`setAllowAjax(bool $allowAjax = true): $this`](method-setallowajax.md)
- [`error(array|Wire|string $text, int $flags = 0): Wire|WireUpload`](method-error.md)
- [`getErrors(bool $clear = false): array`](method-geterrors.md)
- [`getOverwrittenFiles(): array`](method-getoverwrittenfiles.md)
- [`isAjaxUploading(): bool`](method-isajaxuploading.md)
