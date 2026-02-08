# $functions->wire404($message = '')

Source: `wire/core/Functions.php`

Stop execution with a 404 unless redirect URL available (for front-end use)

This is an alternative to using a manual `throw new Wire404Exception()` and is recognized by
PW as a front-end 404 where PagePathHistory (or potentially other modules) are still allowed
to change the behavior of the request from a 404 to something else (like a 301 redirect).

## Arguments

- string $message Optional message to send to Exception message argument (not used in output by default)

## Throws

- Wire404Exception

## Meta

- @since 3.0.146
