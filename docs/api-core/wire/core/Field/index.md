# Field

Source: `wire/core/Field.php`

Inherits: `WireData`
Implements: `Saveable`, `Exportable`

## Summary

ProcessWire Field

Common methods:
- [`set()`](method-set.md)
- [`setRawSetting()`](method-setrawsetting.md)
- [`setFlags()`](method-setflags.md)
- [`addFlag()`](method-addflag.md)
- [`removeFlag()`](method-removeflag.md)

Groups:
Group: [access](group-access.md)
Group: [properties](group-properties.md)

The Field class corresponds to a record in the fields database table
and is managed by the 'Fields' class.

Field represents a custom field that is used on a Page.
$field
$field = $fields->get('field_name');
Field objects are managed by the `$fields` API variable.



Common Inputfield properties that Field objects store:

- `$required: int|bool|null` Whether or not this field is required during input
- `$requiredIf: string|null` A selector-style string that defines the conditions under which input is required
- `$showIf: string|null` A selector-style string that defines the conditions under which the Inputfield is shown
- `$columnWidth: int|null` The Inputfield column width (percent) 10-100.
- `$collapsed: int|null` The Inputfield 'collapsed' value (see Inputfield collapsed constants).
- `$textFormat: int|null` The Inputfield 'textFormat' value (see Inputfield textFormat constants).
- [`viewable(Page $page = null, User $user = null): bool`](method-___viewable.md) Is the field viewable on the given $page by the given $user?
- [`editable(Page $page = null, User $user = null): bool`](method-___editable.md) Is the field editable on the given $page by the given $user?
- [`getInputfield(Page $page, $contextStr = ''): Inputfield`](method-___getinputfield.md) Get instance of the Inputfield module that collects input for this field.
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) Get Inputfields needed to configure this field in the admin.

@todo add modified date property

## Methods
- [`set(string $key, mixed $value): Field|WireData`](method-set.md) Set a native setting or a dynamic data property for this Field
- [`setFlags(int $value)`](method-setflags.md) Set the bitmask of flags for the field
- [`addFlag(int $flag): $this`](method-addflag.md) Add the given bitmask flag
- [`removeFlag(int $flag): $this`](method-removeflag.md) Remove the given bitmask flag
- [`hasFlag(int $flag): bool`](method-hasflag.md) Does this field have the given bitmask flag?
- [`get(string $key): mixed`](method-get.md) Get a Field setting or dynamic data property
- [`setName(string $name): Field`](method-setname.md) Set the field’s name
- [`setFieldtype(string|Fieldtype $type): Field`](method-setfieldtype.md) Set what type of field this is (Fieldtype).
- [`getFieldtype(): Fieldtype|null|string`](method-getfieldtype.md) Return the Fieldtype module representing this field’s type.
- [`getContext(Page|Template|Fieldgroup|string $for, string $namespace = '', bool $has = false): Field|bool`](method-getcontext.md) Get this field in context of a Page/Template
- [`hasContext(Page|Template|Fieldgroup|string $for, string $namespace = ''): Field|bool`](method-hascontext.md) Does this field have context settings for given Page/Template?
- [`getContexts(): array`](method-getcontexts.md) Get all contexts this field is used in
- [`setRoles(string $type, PageArray|array|null $roles)`](method-setroles.md) Set the roles that are allowed to view or edit this field on pages.
- [`viewable(?Page $page = null, ?User $user = null): bool`](method-___viewable.md) (hookable) Is this field viewable?
- [`editable(?Page $page = null, ?User $user = null): bool`](method-___editable.md) (hookable) Is this field editable?
- [`save(): bool`](method-save.md) Save this field’s settings and data in the database.
- [`numFieldgroups(): int`](method-numfieldgroups.md) Return the number of Fieldgroups this field is used in.
- [`getFieldgroups(bool $getCount = false): FieldgroupsArray|int`](method-getfieldgroups.md) Return the list of Fieldgroups using this field.
- [`getTemplates(bool $getCount = false): TemplatesArray|int`](method-gettemplates.md) Return the list of of Templates using this field.
- [`getInputfield(Page $page, string $contextStr = ''): Inputfield|null`](method-___getinputfield.md) (hookable) Get the Inputfield module used to collect input for this field.
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable) Get any Inputfields needed to configure the field in the admin.
- [`getTable(): string`](method-gettable.md) Get the database table used by this field.
- [`setTable(null|string $table = null)`](method-settable.md) Set an override table name, or omit (or null) to restore default table name
- [`__toString()`](method-__tostring.md) The string value of a Field is always it's name
- [`__isset(string $key): bool`](method-__isset.md) Isset
- [`getText(string $property, Page|Language $language = null): string`](method-gettext.md) Return field label, description or notes for language
- [`setText(string $property, string $value, Page|Language $language = null)`](method-settext.md) Set a field label, description or notes for language
- [`getLabel(Page|Language $language = null): string`](method-getlabel.md) Get field label for current language, or another specified language.
- [`getDescription(Page|Language $language = null): string`](method-getdescription.md) Return field description for current language, or another specified language.
- [`getNotes(Page|Language $language = null): string`](method-getnotes.md) Return field notes for current language, or another specified language.
- [`getIcon(bool $prefix = false): mixed|string`](method-geticon.md) Return the icon used by this field, or blank if none.
- [`setLabel(string $text, Language|string|int|null $language = null)`](method-setlabel.md) Set label, optionally for a specific language
- [`setDescription(string $text, Language|string|int|null $language = null)`](method-setdescription.md) Set description, optionally for a specific language
- [`setNotes(string $text, Language|string|int|null $language = null)`](method-setnotes.md) Set notes, optionally for a specific language
- [`setIcon(string $icon): $this`](method-seticon.md) Set the icon for this field
- [`getTags(bool|string $getString = false): array|string`](method-gettags.md) Get tags
- [`addTag(string $tag): array`](method-addtag.md) Add one or more tags
- [`hasTag(string $tag): bool`](method-hastag.md) Return true if this field has the given tag or false if not
- [`removeTag(string $tag): array`](method-removetag.md) Remove a tag
- [`editUrl(array|bool|string $options = array()): string`](method-editurl.md) Get URL to edit field in the admin
- [`setSetupName(string $setupName = null): string`](method-setsetupname.md) Set setup name from Fieldtype to apply when field is saved
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method

## Constants
- [`flagAutojoin = 1`](const-flagautojoin.md)
- [`flagGlobal = 4`](const-flagglobal.md)
- [`flagSystem = 8`](const-flagsystem.md)
- [`flagPermanent = 16`](const-flagpermanent.md)
- [`flagAccess = 32`](const-flagaccess.md)
- [`flagAccessAPI = 64`](const-flagaccessapi.md)
- [`flagAccessEditor = 128`](const-flagaccesseditor.md)
- [`flagUnique = 256`](const-flagunique.md)
- [`flagFieldgroupContext = 2048`](const-flagfieldgroupcontext.md)
- [`flagSystemOverride = 32768`](const-flagsystemoverride.md)
