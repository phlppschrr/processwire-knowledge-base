# WireUpload

Source: `wire/core/WireUpload.php`

Inherits: `Wire`

ProcessWire WireUpload

Saves uploads of single or multiple files, saving them to the destination path.
If the destination path does not exist, it will be created.

Methods:
- [`__construct(string $name)`](method-__construct.md) Construct with the given input name
- [`wired()`](method-wired.md) Wired to API
- [`init()`](method-init.md) Initialize
- [`__destruct()`](method-__destruct.md) Destruct by removing overwritten backup files (if applicable)
- [`execute(): array`](method-execute.md) Execute/process the upload
- [`getPhpFiles(): array|bool`](method-getphpfiles.md) Returns PHP's $_FILES or one constructed from an ajax upload
- [`getUploadDir(): string`](method-getuploaddir.md) Get the directory where files should upload to
- [`getPhpFilesAjax(): array|bool`](method-getphpfilesajax.md) Handles an ajax file upload and constructs a resulting $_FILES
- [`isValidExtension(string $name): bool`](method-isvalidextension.md) Does the given filename have a valid extension?
- [`isValidUpload(string $name, int $size, int $error): bool`](method-isvalidupload.md) Is the given upload information valid?
- [`checkDestinationPath(): bool`](method-checkdestinationpath.md) Check that the destination path exists and populate $this->errors with appropriate message if it doesn't
- [`getUniqueFilename(string $destination): string`](method-getuniquefilename.md) Given a filename/path destination, adjust it to ensure it is unique
- [`validateFilename(string $value, array $extensions = array()): bool|string`](method-validatefilename.md) Sanitize/validate a given filename
- [`saveUpload(string $tmp_name, string $filename, bool $ajax = false): array|bool|string`](method-saveupload.md) Save the uploaded file
- [`saveUploadZip(string $zipFile): array|bool`](method-saveuploadzip.md) Save and process an uploaded ZIP file
- [`getCompletedFilenames(): array`](method-getcompletedfilenames.md) Get array of uploaded filenames
- [`addUploadedFilename(string $completedFilename, string $originalFilename)`](method-adduploadedfilename.md) Add a completed upload file name and its original name
- [`getOriginalFilenames(): array`](method-getoriginalfilenames.md) Get unsanitized array of original filenames (basenames) indexed by completed basename
- [`setTargetFilename($filename)`](method-settargetfilename.md) Set the target filename, only useful for single uploads
- [`getTargetFilename(string $filename): string`](method-gettargetfilename.md) Get target filename updated for extension
- [`setOverwriteFilename(string $filename): $this`](method-setoverwritefilename.md) Set the filename that may be overwritten (i.e. myphoto.jpg) for single uploads only
- [`setValidExtensions(array $extensions): $this`](method-setvalidextensions.md) Set allowed file extensions
- [`setMaxFiles(int $maxFiles): $this`](method-setmaxfiles.md) Set the max allowed number of uploaded files
- [`setMaxFileSize(int $bytes): $this`](method-setmaxfilesize.md) Set the max allowed uploaded file size
- [`setOverwrite(bool $overwrite): $this`](method-setoverwrite.md) Set whether or not overwrite is allowed
- [`setDestinationPath(string $destinationPath): $this`](method-setdestinationpath.md) Set the destination path for uploaded files
- [`setExtractArchives(bool $extract = true): $this`](method-setextractarchives.md) Set whether or not ZIP files may be extracted
- [`setName(string $name): $this`](method-setname.md) Set the upload field name (same as that provided to the constructor)
- [`setLowercase(bool $lowercase = true): $this`](method-setlowercase.md) Set whether or not lowercase is enforced
- [`setAllowAjax(bool $allowAjax = true): $this`](method-setallowajax.md) Set whether or not AJAX uploads are allowed
- [`error(array|Wire|string $text, int $flags = 0): Wire|WireUpload`](method-error.md) Record an error message
- [`getErrors(bool $clear = false): array`](method-geterrors.md) Get error messages
- [`getOverwrittenFiles(): array`](method-getoverwrittenfiles.md) Get files that were overwritten (for overwrite mode only)
- [`isAjaxUploading(): bool`](method-isajaxuploading.md) Is an ajax upload request currently in progress?
