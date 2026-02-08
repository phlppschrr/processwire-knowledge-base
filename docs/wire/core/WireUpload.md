# WireUpload

Source: `wire/core/WireUpload.php`

ProcessWire WireUpload

Saves uploads of single or multiple files, saving them to the destination path.
If the destination path does not exist, it will be created.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## __construct()

Construct with the given input name

@param string $name

## wired()

Wired to API

## init()

Initialize

## __destruct()

Destruct by removing overwritten backup files (if applicable)

## execute()

Execute/process the upload

@return array of uploaded filenames

@throws WireException

## getPhpFiles()

Returns PHP's $_FILES or one constructed from an ajax upload

@return array|bool

@throws WireException

## getUploadDir()

Get the directory where files should upload to

@return string

@throws WireException If no suitable upload directory can be found

## getPhpFilesAjax()

Handles an ajax file upload and constructs a resulting $_FILES

@return array|bool

@throws WireException

## isValidExtension()

Does the given filename have a valid extension?

@param string $name

@return bool

## isValidUpload()

Is the given upload information valid?

Also populates $this->errors

@param string $name Filename

@param int $size Size in bytes

@param int $error Error code from PHP

@return bool

## checkDestinationPath()

Check that the destination path exists and populate $this->errors with appropriate message if it doesn't

@return bool

## getUniqueFilename()

Given a filename/path destination, adjust it to ensure it is unique

@param string $destination

@return string

## validateFilename()

Sanitize/validate a given filename

@param string $value Filename

@param array $extensions Allowed file extensions

@return bool|string Returns boolean false if invalid or string of potentially modified filename if valid

## saveUpload()

Save the uploaded file

@param string $tmp_name Temporary filename (full path and filename)

@param string $filename Actual filename (basename)

@param bool $ajax Is this an AJAX upload?

@return array|bool|string Boolean false on fail, array of multiple filenames, or string of filename if maxFiles=1

## saveUploadZip()

Save and process an uploaded ZIP file

@param string $zipFile

@return array|bool Array of files in the ZIP or boolean false on fail

@throws WireException If ZIP is empty

## getCompletedFilenames()

Get array of uploaded filenames

@return array

## addUploadedFilename()

Add a completed upload file name and its original name

@param string $completedFilename Sanitized filename or basename that was used for saved file

@param string $originalFilename Unsanitized filename as uploaded

## getOriginalFilenames()

Get unsanitized array of original filenames (basenames) indexed by completed basename

@return array

@since 3.0.212

## setTargetFilename()

Set the target filename, only useful for single uploads

@param $filename

## getTargetFilename()

Get target filename updated for extension

Given a filename, takes its extension and combines it with that if the targetFilename (if set).
Otehrwise returns the filename you gave it.

@param string $filename

@return string

## setOverwriteFilename()

Set the filename that may be overwritten (i.e. myphoto.jpg) for single uploads only

@param string $filename

@return $this

## setValidExtensions()

Set allowed file extensions

@param array $extensions Array of file extensions (strings), not including periods

@return $this

## setMaxFiles()

Set the max allowed number of uploaded files

@param int $maxFiles

@return $this

## setMaxFileSize()

Set the max allowed uploaded file size

@param int $bytes

@return $this

## setOverwrite()

Set whether or not overwrite is allowed

@param bool $overwrite

@return $this

## setDestinationPath()

Set the destination path for uploaded files

@param string $destinationPath Include a trailing slash

@return $this

## setExtractArchives()

Set whether or not ZIP files may be extracted

@param bool $extract

@return $this

## setName()

Set the upload field name (same as that provided to the constructor)

@param string $name

@return $this

## setLowercase()

Set whether or not lowercase is enforced

@param bool $lowercase

@return $this

## setAllowAjax()

Set whether or not AJAX uploads are allowed

@param bool $allowAjax

@return $this

## error()

Record an error message

@param array|Wire|string $text

@param int $flags

@return Wire|WireUpload

## getErrors()

Get error messages

@param bool $clear Clear the list of error messages? (default=false)

@return array of strings

## getOverwrittenFiles()

Get files that were overwritten (for overwrite mode only)

WireUpload keeps a temporary backup of replaced files. The backup will be removed at __destruct()
You may retrieve backed up files temporarily if needed.

@return array associative array of ('backup path/file' => 'replaced basename')

## isAjaxUploading()

Is an ajax upload request currently in progress?

@return bool

@since 3.0.131
