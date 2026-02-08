# $pagefilesManager->___save()

Source: `wire/core/PagefilesManager.php`

For hooks to listen to on page save action, for file-specific operations

Executed before a page draft/published assets are moved around, when changes to files may be best to execute.

There are no arguments or return values here.
Hooks may retrieve the Page object being saved from `$event->object->page`.

## Usage

~~~~~
// basic usage
$result = $pagefilesManager->___save();
~~~~~
