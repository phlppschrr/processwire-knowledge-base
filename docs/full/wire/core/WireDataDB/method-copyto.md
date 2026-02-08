# WireDataDB::copyTo()

Source: `wire/core/WireDataDB.php`

Copy all data to a new source ID

Useful to call on the source object after a clone has been created from it.

@param int $newSourceID

@throws WireException

@return int Number of rows copied
