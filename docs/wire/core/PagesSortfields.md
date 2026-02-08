# PagesSortfields

Source: `wire/core/PagesSortfields.php`

ProcessWire PagesSortfields

Pages Sortfields
Manages the table for the sortfield property for Page children.

ProcessWire 3.x, Copyright 2021 by Ryan Cramer
https://processwire.com

## get()

Get sortfield for given Page from DB

@param int|Page $page Page or page ID

@return string

@since 3.0.172

## save()

Save the sortfield for a given Page

@param Page

@return bool

## delete()

Delete the sortfield for a given Page

@param Page

@return bool

## decode()

Decodes a sortfield from a signed integer or string to a field name

The returned fieldname is preceded with a dash if the sortfield is reversed.

@param string|int $sortfield

@param string $default Default sortfield name (default='sort')

@return string

## encode()

Encodes a sortfield from a fieldname to a signed integer (ID) representing a custom field, or native field name

The returned value will be a negative value (or string preceded by a dash) if the sortfield is reversed.

@param string $sortfield

@param string $default Default sortfield name (default='sort')

@return string|int
