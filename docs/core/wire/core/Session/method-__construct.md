# $session->__construct(ProcessWire $wire)

Source: `wire/core/Session.php`

Start the session and set the current User if a session is active

Assumes that you have already performed all session-specific ini_set() and session_name() calls

## Usage

~~~~~
// basic usage
$result = $session->__construct($wire);

// usage with all arguments
$result = $session->__construct(ProcessWire $wire);
~~~~~

## Arguments

- `$wire` `ProcessWire`

## Exceptions

- `WireException`
