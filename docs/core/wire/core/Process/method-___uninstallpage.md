# Process::___uninstallPage()

Source: `wire/core/Process.php`

Uninstall (trash) dedicated pages for this Process module

If there is more than one page using this Process, it will trash them all.

To be called by the Process module's ___uninstall() method.


@return int Number of pages trashed
