# $session->___init()

Source: `wire/core/Session.php`

Start the session

Provided here in any case anything wants to hook in before session_start()
is called to provide an alternate save handler.

## Usage

~~~~~
// basic usage
$result = $session->___init();
~~~~~
