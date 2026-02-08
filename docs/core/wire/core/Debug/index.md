# Debug

Source: `wire/core/Debug.php`

ProcessWire Debug

Provides methods useful for debugging or development.

Currently only provides timer capability.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

~~~~~
$timer = Debug::startTimer();
execute_some_code();
$elapsed = Debug::stopTimer($timer);
~~~~~
