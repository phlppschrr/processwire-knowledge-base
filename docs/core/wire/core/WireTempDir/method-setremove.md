# WireTempDir::setRemove()

Source: `wire/core/WireTempDir.php`

Call this with 'false' to prevent temp dir from being removed automatically when object is destructed

If you do this, then you accept responsibility for removing the directory by calling $tempDir->remove();
If you do not remove it yourself, WireTempDir will remove as part of the daily maintenance.

@param bool $remove

@return $this
