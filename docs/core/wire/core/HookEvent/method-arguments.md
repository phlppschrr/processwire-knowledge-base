# HookEvent::arguments()

Source: `wire/core/HookEvent.php`

Retrieve or set a hooked function argument

~~~~~
// Retrieve first argument by index (0=first)
$page = $event->arguments(0);

// Retrieve array of all arguments
$arguments = $event->arguments();

// Retrieve argument by name
$page = $event->arguments('page');

// Set first argument by index
$event->arguments(0, $page);

// Set first argument by name
$event->arguments('page', $page);
~~~~~

@param int $n Zero based number of the argument you want to retrieve, where 0 is the first.
	 May also be a string containing the argument name.
  Omit to return array of all arguments.

@param mixed $value Value that you want to set to this argument, or omit to only return the argument.

@return array|null|mixed
