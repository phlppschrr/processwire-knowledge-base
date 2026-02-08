# SystemUpdate::execute()

Source: `wire/modules/System/SystemUpdater/SystemUpdate.php`

Execute a system update

@return int|bool True if successful, false if not.
		Or return integer 0 if SystemUpdate[n].php will handle updating the system version when it is ready.
		When false or 0 is returned, updates will stop being applied for that request.
