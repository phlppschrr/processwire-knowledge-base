# WireShutdown

Source: `wire/core/WireShutdown.php`

ProcessWire shutdown handler

ProcessWire 3.x, Copyright 2025 by Ryan Cramer

Look for errors at shutdown and log them, plus echo the error if the page is editable

https://processwire.com

## other

@method void fatalError(array $error)

## defaultFatalErrorHTML

Default HTML to use for error message

Can be overridden with $config->fatalErrorHTML in /site/config.php

## defaultEmailBody

Default email body for emailed fatal errors

## __construct()

Construct and register shutdown function

@param Config $config

## setFatalErrorResponse()

Set fatal error response info including http code, optional extra headers, and more

@param array $options
 - `code` (int): http code to send, or omit to use default (500)
 - `headers` (array): Optional additional headers to send, in format [ "Header-Name: Header-Value" ]
 - `emailTo` (string): Administrator email address to send error to (default=$config->adminEmail)
 - `emailFrom` (string): From email address for email to administrator (default=$config->wireMail['from'])
 - `emailFromName` (string): From “name” for email to administrator (default=$config->wireMail['fromName'])
 - `emailSubject` (string): Override email subject (default=use built-in translatable subject)
 - `emailBody` (string): Override default email body (text-only). Should have {url}, {user} and {message} placeholders.
 - `emailModule` (string): Name of WireMail module to use or leave blank for automatic.
 - `words` (array): Spicy but calming words to prepend to visible error messages.

@since 3.0.166

## prepareLabels()

Setup our translation labels

## getErrorMessage()

Create more informative error message from $error array

@param array $error Error array from PHP’s error_get_last()

@return string

## getWireInput()

Get WireInput instance and create it if not already present in the API

@return WireInput

## getCurrentUrl()

Get the current request URL or "/?/" if it cannot be determined

@return string

## amendErrorMessage()

Add helpful info or replace error message with something better, when possible

@param string $message

@return string

## sendErrorMessage()

Render an error message and reason why

@param string $message

@param string $why

@param bool $useHTML

## simplifyErrorMessageHTML()

Simplify error message HTML for output (inclusive of simplifyErrorMessageText also)

@param string $html

@return string

@since 3.0.175

## simplifyErrorMessageText()

Simplify error message to remove unnecessary or redundant information

@param string $text

@return string

@since 3.0.175

## seasonErrorMessage()

Provide additional seasoning for error message during debug mode output

@param string $message

@return string

## sendFatalHeader()

Send fatal error http header and return error code sent

@return int

## sendFatalError()

Send a fatal error

This is a public fatal error that doesn’t reveal anything specific.

@param string $message Message to indicate who error was also sent to

@param bool $useHTML Output for a web browser?

## sendExistingOutput()

Send any existing output while removing PHP’s error message from it (to avoid duplication)

@return bool Returns true if there was existing output, false if not

## ___fatalError()

Hook called when fatal error received by shutdown()

@param array $error

@since 3.0.173

## setFatalError()

Set shutdown fatal error

Used only for index version >= 302

@param \Throwable $e

@param string $message

@since 3.0.253

## getError()

Get last error

@return array

@since 3.0.253

## shutdown()

Shutdown function registered with PHP

@return bool

## getReasonsWhy()

Get reasons why a fatal error message is shown

If error details should not be shown then return a blank array

@return array

## saveFatalLog()

Save fatal error to log

@param string $url

@param string $userName

@param string $message

@return bool

## sendFatalEmail()

Send fatal error email

@param string $url

@param string $userName

@param string $message

@return bool

## shutdownExternal()

Secondary shutdown call when ProcessWire booted externally
