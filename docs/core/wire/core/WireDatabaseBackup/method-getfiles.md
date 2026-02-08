# WireDatabaseBackup::getFiles()

Source: `wire/core/WireDatabaseBackup.php`

Return array of all backup files

To get additional info on any of them, call getFileInfo($basename) method


@param bool $getObjects Get SplFileInfo objects rather than basenames? (3.0.214+)

@return array|\SplFileInfo[] Array of strings (basenames), or array of SplFileInfo objects (when requested)
