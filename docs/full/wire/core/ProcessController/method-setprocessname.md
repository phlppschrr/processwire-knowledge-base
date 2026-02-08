# ProcessController::setProcessName()

Source: `wire/core/ProcessController.php`

Set the name of the Process to execute.

No need to call this unless you want to override the one auto-determined from the URL.

If overridden, then make sure the name includes the prefix, and don't bother calling the setPrefix() method.

@param string $processName
