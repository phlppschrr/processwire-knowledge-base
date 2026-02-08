# PagesExportImport::cleanupFiles()

Source: `wire/core/PagesExportImport.php`

Remove files and directories in /site/assets/backups/PagesExportImport/ that are older than $maxAge


@param int $maxAge Maximum age in seconds (default=3600)

@return int Number of files/dirs removed
