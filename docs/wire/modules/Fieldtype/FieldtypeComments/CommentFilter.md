# CommentFilter

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentFilter.php`

ProcessWire FieldtypeComments > CommentFilter

A base class for filtering comments from an external service.

Primarily for Akismet (and CommentFilterAkismet), but kept as a base abstract class to
serve as an interface for adding more in the future.

Note that portions of code in here arefrom Akismet API examples.

ProcessWire 3.x, Copyright 2016 by Ryan Cramer
https://processwire.com

## other

@property string $appUserAgent

@property string $charset

@property string $homeURL @deprecated

@property string $apiKey

## httpPost()

Send an HTTP POST request

@param $request

@param $host

@param $path

@param int $port

@return array|string

@deprecated no longer in use (replaced with WireHttp)
