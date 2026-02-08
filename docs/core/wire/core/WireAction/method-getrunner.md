# $wireAction->getRunner(): Wire|null

Source: `wire/core/WireAction.php`

Get the object instance that is running this action

Actions should not generally depend on a particular runner, but should take advantage
of a specific runner if it benefits the action.

## Return value

Wire|null Returns null if no runner has been set
