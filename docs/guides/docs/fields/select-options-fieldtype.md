# Select Options Fieldtype (FieldtypeOptions)

Source: https://processwire.com/docs/fields/select-options-fieldtype/

## Summary

The Options Fieldtype provides single and multi choice selectable options in ProcessWire, as an alternative to using Page fields.

## Key Points

- The Options Fieldtype provides single and multi choice selectable options in ProcessWire, as an alternative to using Page fields.
- For features and highlights see our post on the Options Fieldtype or continue reading here to learn more about how to use it.
- While we usually recommend using the Page Fieldtype for selectable options, this Options Fieldtype provides a convenient alternative for when the selectable options will not benefit from being pages, or when a speedy definition process outweighs the benefits of using pages. Like with the Page Fieldtype, you can define what type of input should be used with the field settings. The input type can be any core or 3rd party Inputfield that extends ProcessWire's InputfieldSelect module. For core Inputfields, this includes: Single Select, Multiple Select, Checkboxes, Radio Buttons, and AsmSelect (a sortable multi-select).

## Sections


### About the Options Fieldtype

While we usually recommend using the Page Fieldtype for selectable options, this Options Fieldtype provides a convenient alternative for when the selectable options will not benefit from being pages, or when a speedy definition process outweighs the benefits of using pages. Like with the Page Fieldtype, you can define what type of input should be used with the field settings. The input type can be any core or 3rd party Inputfield that extends ProcessWire's InputfieldSelect module. For core Inputfields, this includes: Single Select, Multiple Select, Checkboxes, Radio Buttons, and AsmSelect (a sortable multi-select).


## Options Administration


### Creating an Options field


### Defining options

You can define options on the Details tab when editing an Options field (Setup > Fields > your field). Options are defined in a multi-line text box, where each line represents one option. You may type or paste in a list of options (like a list of countries for example, 1 per line) and save.


### Adding New Options

Enter the text of each new option on a new line anywhere in the existing options. You may omit the ID number as one will be automatically assigned after you save. Once assigned, you should never change this ID number, but you can change the title (or value) as much as you like.


### Moving or Sorting Options

Copy entire line(s), including ID number, and paste wherever you want them to go.


### Editing or Renaming Options

Modify the option title or value as you would like, ensuring that the original ID number remains connected with the option.


### Deleting Options

Delete the entire lines containing the options that you want to delete. You will be asked to confirm the deletion after you submit the form. The option will not be deleted until you click the box to confirm and submit the form again. Note that this also deletes any selections for that option in the database.
