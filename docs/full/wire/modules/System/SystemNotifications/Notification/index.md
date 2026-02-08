# Notification

Source: `wire/modules/System/SystemNotifications/Notification.php`

An individual notification item to be part of a NotificationArray for a Page

@class Notification


data encoded vars, all optional
===============================

@property int $id  unique ID (among others the user may have)

@property string $text  extended text

@property string $html  extended text as HTML markup

@property string $from  "from" text where applicable, like a class name

@property string $icon  fa-icon when applicable

@property string $href  clicking notification goes to this URL

@property int $progress  progress percent 0-100

@property int $expires  datetime after which will automatically be deleted

Groups:
Group: [other](group-other.md)

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
