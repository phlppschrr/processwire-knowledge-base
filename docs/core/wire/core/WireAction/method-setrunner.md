# WireAction::setRunner()

Source: `wire/core/WireAction.php`

Set the object instance that is running this action

If an action knows that it only accepts a certain type of runner, then
it should throw a WireException if the given runner is not valid.

@param Wire $runner
