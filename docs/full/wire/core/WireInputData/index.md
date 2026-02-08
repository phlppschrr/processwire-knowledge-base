# WireInputData

Source: `wire/core/WireInputData.php`

WireInputData manages one of GET, POST, COOKIE, or whitelist

WireInputData and the WireInput class together form a simple
front end to PHP's $_GET, $_POST, and $_COOKIE superglobals.

Vars retrieved from here will not have to consider magic_quotes.
No sanitization or filtering is done, other than disallowing
multi-dimensional arrays in input.

WireInputData specifically manages one of: get, post, cookie or
whitelist, whereas the WireInput class provides access to the 3
InputData instances.

Each WireInputData is not instantiated unless specifically asked for.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

@link http://processwire.com/api/ref/input/ Offical $input API variable documentation

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [setArray()](method-setarray.md)
Method: [getArray()](method-getarray.md)
Method: [__set()](method-__set.md)
Method: [set()](method-set.md)
Method: [get()](method-get.md)
Method: [findOne()](method-findone.md)
Method: [find()](method-find.md)
Method: [cleanArray()](method-cleanarray.md)
Method: [setStripSlashes()](method-setstripslashes.md)
Method: [__get()](method-__get.md)
Method: [remove()](method-remove.md)
Method: [removeAll()](method-removeall.md)
Method: [callUnknown()](method-___callunknown.md) (hookable)
