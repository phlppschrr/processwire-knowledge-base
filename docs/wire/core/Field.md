# Field

Source: `wire/core/Field.php`

ProcessWire Field

The Field class corresponds to a record in the fields database table
and is managed by the 'Fields' class.

Field represents a custom field that is used on a Page.
$field
$field = $fields->get('field_name');
Field objects are managed by the `$fields` API variable.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com


Common Inputfield properties that Field objects store:

@property int|bool|null $required Whether or not this field is required during input

@property string|null $requiredIf A selector-style string that defines the conditions under which input is required

@property string|null $showIf A selector-style string that defines the conditions under which the Inputfield is shown

@property int|null $columnWidth The Inputfield column width (percent) 10-100.

@property int|null $collapsed The Inputfield 'collapsed' value (see Inputfield collapsed constants).

@property int|null $textFormat The Inputfield 'textFormat' value (see Inputfield textFormat constants).

@method bool viewable(Page $page = null, User $user = null) Is the field viewable on the given $page by the given $user?

@method bool editable(Page $page = null, User $user = null) Is the field editable on the given $page by the given $user?

@method Inputfield getInputfield(Page $page, $contextStr = '') Get instance of the Inputfield module that collects input for this field.

@method InputfieldWrapper getConfigInputfields() Get Inputfields needed to configure this field in the admin.

@todo add modified date property

## access

@property bool $useRoles Whether or not access control is enabled

@property array $editRoles Role IDs with edit access, applicable only if access control is enabled.

@property array $viewRoles Role IDs with view access, applicable only if access control is enabled.

## properties

@property int $id Numeric ID of field in the database

@property string $name Name of field

@property string $table Database table used by the field

@property string $prevTable Previously database table (if field was renamed)

@property string $prevName Previously used name (if field was renamed), 3.0.164+

@property Fieldtype|null $type Fieldtype module that represents the type of this field

@property Fieldtype|null $prevFieldtype Previous Fieldtype, if type was changed

@property int $flags Bitmask of flags used by this field

@property-read string $flagsStr Names of flags used by this field (readonly)

@property string $label Text string representing the label of the field

@property string $description Longer description text for the field

@property string $notes Additional notes text about the field

@property string $icon Icon name used by the field, if applicable

@property string $tags Tags that represent this field, if applicable (space separated string).

@property-read array $tagList Same as $tags property, but as an array.

@property array $allowContexts Names of settings that are custom configured to be allowed for context.

## flagAutojoin

Field should be automatically joined to the page at page load time

## flagGlobal

Field used by all fieldgroups - all fieldgroups required to contain this field

## flagSystem

Field is a system field and may not be deleted, have it's name changed, or be converted to non-system

## flagPermanent

Field is permanent in any fieldgroups/templates where it exists - it may not be removed from them

## flagAccess

Field is access controlled

## flagAccessAPI

If field is access controlled, this flag says that values are still front-end API accessible

Without this flag, non-viewable values are made blank when output formatting is ON.

## flagAccessEditor

If field is access controlled and user has no edit access, they can still view in the editor (if they have view permission)

Without this flag, non-editable values are simply not shown in the editor at all.

## flagUnique

Field requires that the same value is not repeated more than once in its table 'data' column (when supported by Fieldtype)

When this flag is set and there is a non-empty $flagUnique property on the field, then it indicates a unique index
is currently present. When only this flag is present (no property), it indicates a request to remove the index and flag.
When only the property is present (no flag), it indicates a pending request to add unique index and flag.

@since 3.0.150

## flagFieldgroupContext

Field has been placed in a runtime state where it is contextual to a specific fieldgroup and is no longer saveable

## flagSystemOverride

Set this flag to override system/permanent flags if necessary - once set, system/permanent flags can be removed, but not in the same set().

## set()

Set a native setting or a dynamic data property for this Field

This can also be used directly via `$field->name = 'company';`


@param string $key Property name to set

@param mixed $value

@return Field|WireData

## setFlags()

Set the bitmask of flags for the field

@param int $value

## addFlag()

Add the given bitmask flag


@param int $flag

@return $this

## removeFlag()

Remove the given bitmask flag


@param int $flag

@return $this

## hasFlag()

Does this field have the given bitmask flag?


@param int $flag

@return bool

## get()

Get a Field setting or dynamic data property

This can also be accessed directly, i.e. `$fieldName = $field->name;`.


@param string $key

@return mixed

## setName()

Set the field’s name

This method will throw a WireException when field name is a reserved word, is already in use,
is a system field, or is in some format not accepted for a field name.


@param string $name

@return Field $this

@throws WireException

## setFieldtype()

Set what type of field this is (Fieldtype).


@param string|Fieldtype $type Type should be either a Fieldtype object or the string name of a Fieldtype object.

@return Field $this

@throws WireException

## getFieldtype()

Return the Fieldtype module representing this field’s type.

Can also be accessed directly via `$field->type`.


@return Fieldtype|null|string

@since 3.0.16 Added for consistency, but all versions can still use $field->type.

## getContext()

Get this field in context of a Page/Template


@param Page|Template|Fieldgroup|string $for Specify Page, Template, or template name string

@param string $namespace Optional namespace (internal use)

@param bool $has Return boolean rather than Field to check if context exists? (default=false)

@return Field|bool

@since 3.0.162

@see Fieldgroup::getFieldContext(), Field::hasContext()

## hasContext()

Does this field have context settings for given Page/Template?


@param Page|Template|Fieldgroup|string $for Specify Page, Template, or template name string

@param string $namespace Optional namespace (internal use)

@return Field|bool

@since 3.0.163

@see Field::getContext()

## getContexts()

Get all contexts this field is used in

@return array Array of 'fieldgroup-name' => [ contexts ]

@since 3.0.182

## setRoles()

Set the roles that are allowed to view or edit this field on pages.

Applicable only if the `Field::flagAccess` is set to this field's flags.


@param string $type Must be either "view" or "edit"

@param PageArray|array|null $roles May be a PageArray of Role objects or an array of Role IDs.

@throws WireException if given invalid argument

## ___viewable()

Is this field viewable?


- To maximize efficiency check that `$field->useRoles` is true before calling this.
- If you have already verified that the page is viewable, omit or specify null for $page argument.
- **Please note:** this does not check that the provided $page itself is viewable. If you want that
  check, then use `$page->viewable($field)` instead.

@param Page|null $page Optionally specify a Page for context (i.e. Is field viewable on $page?)

@param User|null $user Optionally specify a different user for context (default=current user)

@return bool True if viewable, false if not

## ___editable()

Is this field editable?

- To maximize efficiency check that `$field->useRoles` is true before calling this.
- If you have already verified that the page is editable, omit or specify null for $page argument.
- **Please note:** this does not check that the provided $page itself is editable. If you want that
  check, then use `$page->editable($field)` instead.


@param Page|null $page Optionally specify a Page for context

@param User|null $user Optionally specify a different user (default = current user)

@return bool

## save()

Save this field’s settings and data in the database.

To hook this save, hook to `Fields::save()` instead.


@return bool

## numFieldgroups()

Return the number of Fieldgroups this field is used in.

Primarily used to check if the Field is deletable.


@return int

## getFieldgroups()

Return the list of Fieldgroups using this field.


@param bool $getCount Get count rather than FieldgroupsArray? (default=false) 3.0.182+

@return FieldgroupsArray|int WireArray of Fieldgroup objects or count if requested

## getTemplates()

Return the list of of Templates using this field.


@param bool $getCount Get count rather than FieldgroupsArray? (default=false) 3.0.182+

@return TemplatesArray|int WireArray of Template objects or count when requested.

## ___getInputfield()

Get the Inputfield module used to collect input for this field.


@param Page $page Page that the Inputfield is for.

@param string $contextStr Optional context string to append to the Inputfield's name/id (for repeaters and such).

@return Inputfield|null

## ___getConfigInputfields()

Get any Inputfields needed to configure the field in the admin.


@return InputfieldWrapper

## getTable()

Get the database table used by this field.


@return string

@throws WireException

## setTable()

Set an override table name, or omit (or null) to restore default table name


@param null|string $table

## __toString()

The string value of a Field is always it's name

## __isset()

Isset

@param string $key

@return bool

## getText()

Return field label, description or notes for language

@param string $property Specify either label, description or notes

@param Page|Language $language Optionally specify a language. If not specified user's current language is used.

@return string

## setText()

Set a field label, description or notes for language

@param string $property Specify either label, description or notes

@param string $value Text to set for property

@param Page|Language $language Optionally specify a language. If not specified default language is used.

## getLabel()

Get field label for current language, or another specified language.

This is different from `$field->label` in that it knows about languages (when installed).


@param Page|Language $language Optionally specify a language. If not specified user's current language is used.

@return string

## getDescription()

Return field description for current language, or another specified language.

This is different from `$field->description` in that it knows about languages (when installed).


@param Page|Language $language Optionally specify a language. If not specified user's current language is used.

@return string

## getNotes()

Return field notes for current language, or another specified language.

This is different from `$field->notes` in that it knows about languages (when installed).


@param Page|Language $language Optionally specify a language. If not specified user's current language is used.

@return string

## getIcon()

Return the icon used by this field, or blank if none.


@param bool $prefix Whether or not you want the icon prefix included (i.e. "fa-")

@return mixed|string

## setLabel()

Set label, optionally for a specific language


@param string $text Text to set

@param Language|string|int|null $language Language to use

@since 3.0.16 Added for consistency, all versions can still set property directly.

## setDescription()

Set description, optionally for a specific language


@param string $text Text to set

@param Language|string|int|null $language Language to use

@since 3.0.16 Added for consistency, all versions can still set property directly.

## setNotes()

Set notes, optionally for a specific language


@param string $text Text to set

@param Language|string|int|null $language Language to use

@since 3.0.16 Added for consistency, all versions can still set property directly.

## setIcon()

Set the icon for this field


@param string $icon Icon name

@return $this

## getTags()

Get tags

@param bool|string $getString Optionally specify true for space-separated string, or delimiter string (default=false)

@return array|string Returns array of tags unless $getString option is requested

@since 3.0.106

## addTag()

Add one or more tags

@param string $tag

@return array Returns current tag list

@since 3.0.106

## hasTag()

Return true if this field has the given tag or false if not

@param string $tag

@return bool

@since 3.0.106

## removeTag()

Remove a tag

@param string $tag

@return array Returns current tag list

@since 3.0.106

## editUrl()

Get URL to edit field in the admin

@param array|bool|string $options Specify array of options, string for find option, or bool for http option.
 - `find` (string): Name of field to find in editor form
 - `http` (bool): True to force inclusion of scheme and hostname

@return string

@since 3.0.151

## setSetupName()

Set setup name from Fieldtype to apply when field is saved

@param string $setupName Setup name or omit to instead get the current value

@return string Returns current value

## __debugInfo()

debugInfo PHP 5.6+ magic method

This is used when you print_r() an object instance.

@return array
