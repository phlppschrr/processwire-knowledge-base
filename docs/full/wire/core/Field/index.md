# Field

Source: `wire/core/Field.php`

Inherits: `WireData`
Implements: `Saveable`, `Exportable`


Groups:
Group: [access](group-access.md)
Group: [properties](group-properties.md)

ProcessWire Field

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

Methods:
- [`set(string $key, mixed $value): Field|WireData`](method-set.md)
- [`setFlags(int $value)`](method-setflags.md)
- [`addFlag(int $flag): $this`](method-addflag.md)
- [`removeFlag(int $flag): $this`](method-removeflag.md)
- [`hasFlag(int $flag): bool`](method-hasflag.md)
- [`get(string $key): mixed`](method-get.md)
- [`setName(string $name): Field`](method-setname.md)
- [`setFieldtype(string|Fieldtype $type): Field`](method-setfieldtype.md)
- [`getFieldtype(): Fieldtype|null|string`](method-getfieldtype.md)
- [`getContext(Page|Template|Fieldgroup|string $for, string $namespace = '', bool $has = false): Field|bool`](method-getcontext.md)
- [`hasContext(Page|Template|Fieldgroup|string $for, string $namespace = ''): Field|bool`](method-hascontext.md)
- [`getContexts(): array`](method-getcontexts.md)
- [`setRoles(string $type, PageArray|array|null $roles)`](method-setroles.md)
- [`viewable(?Page $page = null, ?User $user = null): bool`](method-___viewable.md) (hookable)
- [`editable(?Page $page = null, ?User $user = null): bool`](method-___editable.md) (hookable)
- [`save(): bool`](method-save.md)
- [`numFieldgroups(): int`](method-numfieldgroups.md)
- [`getFieldgroups(bool $getCount = false): FieldgroupsArray|int`](method-getfieldgroups.md)
- [`getTemplates(bool $getCount = false): TemplatesArray|int`](method-gettemplates.md)
- [`getInputfield(Page $page, string $contextStr = ''): Inputfield|null`](method-___getinputfield.md) (hookable)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable)
- [`getTable(): string`](method-gettable.md)
- [`setTable(null|string $table = null)`](method-settable.md)
- [`__toString()`](method-__tostring.md)
- [`__isset(string $key): bool`](method-__isset.md)
- [`getText(string $property, Page|Language $language = null): string`](method-gettext.md)
- [`setText(string $property, string $value, Page|Language $language = null)`](method-settext.md)
- [`getLabel(Page|Language $language = null): string`](method-getlabel.md)
- [`getDescription(Page|Language $language = null): string`](method-getdescription.md)
- [`getNotes(Page|Language $language = null): string`](method-getnotes.md)
- [`getIcon(bool $prefix = false): mixed|string`](method-geticon.md)
- [`setLabel(string $text, Language|string|int|null $language = null)`](method-setlabel.md)
- [`setDescription(string $text, Language|string|int|null $language = null)`](method-setdescription.md)
- [`setNotes(string $text, Language|string|int|null $language = null)`](method-setnotes.md)
- [`setIcon(string $icon): $this`](method-seticon.md)
- [`getTags(bool|string $getString = false): array|string`](method-gettags.md)
- [`addTag(string $tag): array`](method-addtag.md)
- [`hasTag(string $tag): bool`](method-hastag.md)
- [`removeTag(string $tag): array`](method-removetag.md)
- [`editUrl(array|bool|string $options = array()): string`](method-editurl.md)
- [`setSetupName(string $setupName = null): string`](method-setsetupname.md)
- [`__debugInfo(): array`](method-__debuginfo.md)

Constants:
- [`flagAutojoin`](const-flagautojoin.md)
- [`flagGlobal`](const-flagglobal.md)
- [`flagSystem`](const-flagsystem.md)
- [`flagPermanent`](const-flagpermanent.md)
- [`flagAccess`](const-flagaccess.md)
- [`flagAccessAPI`](const-flagaccessapi.md)
- [`flagAccessEditor`](const-flagaccesseditor.md)
- [`flagUnique`](const-flagunique.md)
- [`flagFieldgroupContext`](const-flagfieldgroupcontext.md)
- [`flagSystemOverride`](const-flagsystemoverride.md)
