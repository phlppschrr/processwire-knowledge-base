# WireMailInterface

Source: `wire/core/WireMailInterface.php`

ProcessWire WireMail Interface

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## to()

Set the email to address

Each added email addresses appends to any addresses already supplied, unless
you specify NULL as the email address, in which case it clears them all.

@param string|array|null $email Specify any ONE of the following:
	1. Single email address or "User Name <user@example.com>" string.
	2. CSV string of #1.
	3. Non-associative array of #1.
	4. Associative array of (email => name)
	5. NULL (default value, to clear out any previously set values)

@param string $name Optionally provide a FROM name, applicable
	only when specifying #1 (single email) for the first argument.

@return self

@throws WireException if any provided emails were invalid

## from()

Set the email from address

@param string Must be a single email address or "User Name <user@example.com>" string.

@param string|null An optional FROM name (same as setting/calling fromName)

@return self

@throws WireException if provided email was invalid

## subject()

Set the email subject

@param string $subject

@return self

## body()

Set the email message body (text only)

@param string $body in text only

@return self

## bodyHTML()

Set the email message body (HTML only)

@param string $body in HTML

@return self

## header()

Set any email header

@param string $key

@param string $value

@return self

## param()

Set any email param

See $additional_parameters at: http://www.php.net/manual/en/function.mail.php

@param string $value

@return self

## ___send()

Add a file to be attached to the email


@param string $value

@param string $filename

@return self

public function attachment($value, $filename = '');

## ___send()

Send the email

@return int Returns number of messages sent or 0 on failure
