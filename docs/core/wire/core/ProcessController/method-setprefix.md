# $processController->setPrefix($prefix)

Source: `wire/core/ProcessController.php`

Set the class name prefix used by all related Processes

This is prepended to the class name determined from the URL.
For example, if the URL indicates a process name is "PageEdit", then we would need a prefix of "Admin"
to fully resolve the class name.

## Arguments

- string $prefix
