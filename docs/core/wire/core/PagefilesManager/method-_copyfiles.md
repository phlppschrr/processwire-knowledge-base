# PagefilesManager::_copyFiles()

Source: `wire/core/PagefilesManager.php`

Recursively copy all files in $fromPath to $toPath, for internal use

@param string $fromPath Path to copy from

@param string $toPath Path to copy to

@param bool $rename Rename files rather than copy? (makes this perform like a move rather than copy)

@return int Number of files copied
