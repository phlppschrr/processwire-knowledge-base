# $adminTheme->init()

Source: `wire/core/AdminTheme.php`

Initialize the admin theme system and determine which admin theme should be used

All admin themes must call this init() method to register themselves.

Note: this should be called after API ready.

## Usage

~~~~~
// basic usage
$result = $adminTheme->init();
~~~~~
