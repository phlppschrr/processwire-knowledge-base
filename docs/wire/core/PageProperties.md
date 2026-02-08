# PageProperties

Source: `wire/core/PageProperties.php`

ProcessWire Page properties helper

For static runtime property detection by the base Page class.
The properties/methods in this class were originally in the base Page class
but have been moved here for Page class load time optimization purposes.
Except where indicated, please treat these properties as private to the
Page class.

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## statusToNames()

Given a status (flags int) return array of status names

@param int $status

@return array
