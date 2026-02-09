# Debug

Source: `wire/core/Debug.php`

ProcessWire Debug

Provides methods useful for debugging or development.

Currently only provides timer capability.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/


~~~~~
$timer = Debug::startTimer();
execute_some_code();
$elapsed = Debug::stopTimer($timer);
~~~~~
