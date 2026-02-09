# Field

Source: `wire/core/Field.php`

ProcessWire Field

The Field class corresponds to a record in the fields database table
and is managed by the 'Fields' class.

Field represents a custom field that is used on a Page.
$field
$field = $fields->get('field_name');
Field objects are managed by the `$fields` API variable.



Common Inputfield properties that Field objects store:

- $required: int|bool|null Whether or not this field is required during input

- $requiredIf: string|null A selector-style string that defines the conditions under which input is required

- $showIf: string|null A selector-style string that defines the conditions under which the Inputfield is shown

- $columnWidth: int|null The Inputfield column width (percent) 10-100.

- $collapsed: int|null The Inputfield 'collapsed' value (see Inputfield collapsed constants).

- $textFormat: int|null The Inputfield 'textFormat' value (see Inputfield textFormat constants).

- [viewable(Page $page = null, User $user = null): bool](method-___viewable.md) Is the field viewable on the given $page by the given $user?

- [editable(Page $page = null, User $user = null): bool](method-___editable.md) Is the field editable on the given $page by the given $user?

- [getInputfield(Page $page, $contextStr = ''): Inputfield](method-___getinputfield.md) Get instance of the Inputfield module that collects input for this field.

- [getConfigInputfields(): InputfieldWrapper](method-___getconfiginputfields.md) Get Inputfields needed to configure this field in the admin.

@todo add modified date property

Groups:
Group: [access](group-access.md)
Group: [properties](group-properties.md)

Methods:
Method: [set()](method-set.md)
Method: [setFlags()](method-setflags.md)
Method: [addFlag()](method-addflag.md)
Method: [removeFlag()](method-removeflag.md)
Method: [hasFlag()](method-hasflag.md)
Method: [get()](method-get.md)
Method: [setName()](method-setname.md)
Method: [setFieldtype()](method-setfieldtype.md)
Method: [getFieldtype()](method-getfieldtype.md)
Method: [getContext()](method-getcontext.md)
Method: [hasContext()](method-hascontext.md)
Method: [getContexts()](method-getcontexts.md)
Method: [setRoles()](method-setroles.md)
Method: [viewable()](method-___viewable.md) (hookable)
Method: [editable()](method-___editable.md) (hookable)
Method: [save()](method-save.md)
Method: [numFieldgroups()](method-numfieldgroups.md)
Method: [getFieldgroups()](method-getfieldgroups.md)
Method: [getTemplates()](method-gettemplates.md)
Method: [getInputfield()](method-___getinputfield.md) (hookable)
Method: [getConfigInputfields()](method-___getconfiginputfields.md) (hookable)
Method: [getTable()](method-gettable.md)
Method: [setTable()](method-settable.md)
Method: [__toString()](method-__tostring.md)
Method: [__isset()](method-__isset.md)
Method: [getText()](method-gettext.md)
Method: [setText()](method-settext.md)
Method: [getLabel()](method-getlabel.md)
Method: [getDescription()](method-getdescription.md)
Method: [getNotes()](method-getnotes.md)
Method: [getIcon()](method-geticon.md)
Method: [setLabel()](method-setlabel.md)
Method: [setDescription()](method-setdescription.md)
Method: [setNotes()](method-setnotes.md)
Method: [setIcon()](method-seticon.md)
Method: [getTags()](method-gettags.md)
Method: [addTag()](method-addtag.md)
Method: [hasTag()](method-hastag.md)
Method: [removeTag()](method-removetag.md)
Method: [editUrl()](method-editurl.md)
Method: [setSetupName()](method-setsetupname.md)
Method: [__debugInfo()](method-__debuginfo.md)

Constants:
Const: [flagAutojoin](const-flagautojoin.md)
Const: [flagGlobal](const-flagglobal.md)
Const: [flagSystem](const-flagsystem.md)
Const: [flagPermanent](const-flagpermanent.md)
Const: [flagAccess](const-flagaccess.md)
Const: [flagAccessAPI](const-flagaccessapi.md)
Const: [flagAccessEditor](const-flagaccesseditor.md)
Const: [flagUnique](const-flagunique.md)
Const: [flagFieldgroupContext](const-flagfieldgroupcontext.md)
Const: [flagSystemOverride](const-flagsystemoverride.md)
