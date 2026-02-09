# Notice

Source: `wire/core/Notice.php`

ProcessWire Notice

Notice
Manages notifications in the ProcessWire admin, primarily for internal use.
Base class that holds a message, source class, and timestamp.
Contains individual notices/messages used by the application to display to the user.
Notice items come in three different classes: NoticeMessage, NoticeWarning and NoticeError.
They are all identical in terms of API, with the only difference being that they render as
informational messages, warnings, or errors.

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [set()](method-set.md)
Method: [get()](method-get.md)
Method: [flags()](method-flags.md)
Method: [flag()](method-flag.md)
Method: [flagNames()](method-flagnames.md)
Method: [addFlag()](method-addflag.md)
Method: [removeFlag()](method-removeflag.md)
Method: [hasFlag()](method-hasflag.md)
Method: [getName()](method-getname.md)
Method: [viewable()](method-viewable.md)

Constants:
Const: [prepend](const-prepend.md)
Const: [debug](const-debug.md)
Const: [log](const-log.md)
Const: [logOnly](const-logonly.md)
Const: [allowMarkup](const-allowmarkup.md)
Const: [markup](const-markup.md)
Const: [anonymous](const-anonymous.md)
Const: [noGroup](const-nogroup.md)
Const: [separate](const-separate.md)
Const: [login](const-login.md)
Const: [admin](const-admin.md)
Const: [superuser](const-superuser.md)
Const: [allowMarkdown](const-allowmarkdown.md)
Const: [markdown](const-markdown.md)
Const: [allowDuplicate](const-allowduplicate.md)
Const: [duplicate](const-duplicate.md)
