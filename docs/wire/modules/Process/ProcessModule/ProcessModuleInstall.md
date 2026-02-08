# ProcessModuleInstall

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Installation helper for ProcessModule

Provides methods for internative module installation for ProcessModule

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

## getTempDir()

Returns a temporary directory (path) for use by this object

@return string|bool Returns false if you specified $create=false, and the dir doesn't exist

@throws WireException If can't create temporary dir

## canUploadDownload()

Check that the system supports direct upload and download of modules

This primarily checks that needed dirs are writable and ZipArchive is available.

@param bool $notify Specify true to make it queue the relevant reason/error message if upload/download not supported. (default=false)

@param string $type One of 'upload' or 'download' or omit for general check

@return bool

## canInstallFromFileUpload()

Module upload allowed?

@param bool $notify

@return bool

## canInstallFromDownloadUrl()

Module download from URL allowed?

@param bool $notify

@return bool

## canInstallFromDirectory()

Module install/upgrade from directory allowed?

@param bool $notify

@return bool

## findModuleFiles()

Find all module files, recursively in Path

@param string $path Omit to use the default (/site/modules/)

@param int $maxLevel Max depth to pursue module files in (recursion level)

@return array of module classname => full pathname to module file

## determineDestinationDir()

Given a list of files from a module (and their temp dir) return the recommended directory name for it to live in

i.e. /site/modules/[ModuleDir]/

@param array $files Files found in the module's ZIP file

@param string $modulePath Path where module will live

@return bool|string Returns false if no module files found. Otherwise returns string with module path.

## unzipModule()

Unzip the module file to tempDir and then copy to destination directory

@param string $zipFile File to unzip

@param string $destinationDir Directory to copy completed files into. Optionally omit to determine automatically.

@return bool|string Returns destinationDir on success, false on failure

@throws WireException

## backupDir()

Create a backup of a module directory

@param string $moduleDir

@return bool

@throws WireException

## restoreDir()

Restore a module directory

@param string $moduleDir

@return bool

@throws WireException

## uploadModule()

Process a module upload

@param string $inputName Optionally specify the name of the $_FILES input to look for (default=upload_module)

@param string $destinationDir Optionally specify destination path for completed unzipped files

@return bool|string Returns destinationDir on success, false on failure.

## downloadModule()

Given a URL to a ZIP file, download it, unzip it, and move to /site/modules/[ModuleName]

@param string $url Download URL

@param string $destinationDir Optional destination path for files (omit to auto-determine)

@param string $type Specify type of 'download' or 'directory'

@return bool|string Returns destinationDir on success, false on failure.

## downloadModuleFromUrl()

Download module from URL

@param string $url

@param string $destinationDir

@return bool|string

@since 3.0.162

## downloadModuleFromDirectory()

Download module from directory

@param string $url

@param string $destinationDir

@return bool|string

@since 3.0.162

## installDisabledLabel()

Return label to indicate option is disabled and how to enable it

@param string $type

@return string

@since 3.0.162
