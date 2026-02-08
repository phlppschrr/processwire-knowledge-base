# WireRandom::base64()

Source: `wire/core/WireRandom.php`

Generate a truly random base64 string of a certain length

This is largely taken from Anthony Ferrara's password_compat library:
https://github.com/ircmaxell/password_compat/blob/master/lib/password.php
Modified for camelCase, variable names, and function-based context by Ryan.

@param int $requiredLength Length of string you want returned (default=22)

@param array|bool $options Specify array of options or boolean to specify only `fast` option.
 - `fast` (bool): Use fastest, not cryptographically secure method (default=false).
 - `test` (bool|array): Return tests in a string (bool true), or specify array(true) to return tests array (default=false).
   Note that if the test option is used, then the fast option is disabled.

@return string|array Returns only array if you specify array for $test argument, otherwise returns string
