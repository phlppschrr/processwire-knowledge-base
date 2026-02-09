# Notification

Source: `wire/modules/System/SystemNotifications/Notification.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

An individual notification item to be part of a NotificationArray for a Page

@class Notification


data encoded vars, all optional
===============================

- $id: int unique ID (among others the user may have)
- $text: string extended text
- $html: string extended text as HTML markup
- $from: string "from" text where applicable, like a class name
- $icon: string fa-icon when applicable
- $href: string clicking notification goes to this URL
- $progress: int progress percent 0-100
- $expires: int datetime after which will automatically be deleted

Methods:
Method: [__construct()](method-__construct.md)
Method: [is()](method-is.md)
Method: [flagNameToFlag()](method-flagnametoflag.md)
Method: [flagNamesToFlags()](method-flagnamestoflags.md)
Method: [setFlag()](method-setflag.md)
Method: [addFlag()](method-addflag.md)
Method: [removeFlag()](method-removeflag.md)
Method: [setFlags()](method-setflags.md)
Method: [set()](method-set.md)
Method: [getID()](method-getid.md)
Method: [getHash()](method-gethash.md)
Method: [get()](method-get.md)
Method: [isExpired()](method-isexpired.md)
Method: [__toString()](method-__tostring.md)

Constants:
Const: [flagDebug](const-flagdebug.md)
