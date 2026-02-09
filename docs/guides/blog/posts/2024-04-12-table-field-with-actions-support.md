# ProFields Table Field with Actions support

Source: https://processwire.com/blog/posts/table-field-with-actions-support/

## Sections


## New ProFields Table Field with Actions support

12 April 2024 by Ryan Cramer [ 2 Comments](/blog/posts/table-field-with-actions-support/#comments)

This week we have some updates for the ProFields table field (FieldtypeTable). These updates are primarily focused on adding new tools for the editor to facilitate input and management of content in a table field.

Please see the video above (no audio) for an overview of what's new in this version of ProFields Table.


### Sorting rows as a group

Previously you could only sort rows one at a time. Now you can select multiple rows and move them as a group. You can select multiple rows by clicking the icon in the row’s first column (the sort icon). And you can select a range of rows by selecting the row that stars the range and then shift-click select the row that ends the range. Once multiple rows are selected, click and hold the sort icon for any of the selected rows and drag the group of rows to the target location. Note that when dragging a group of rows, only the row being dragged is visible — the other rows will become visible once the operation is complete.


### Row actions

Once you have one or more selected rows, you can apply actions to them. Below are some of the actions included in this latest version of ProFields Table:


### Add rows above or below current selection

Add a given number of rows above (or below) the current selected row(s). If no rows are selected then they will be added to the top (or bottom). When selecting one of the "Add rows" actions, it will prompt you for a quantity of rows to add.


### Copy selected rows

Copy all selected rows to paste somewhere else, whether on the same page or another. You can copy rows, then switch to another tab and paste them to another page, without reloading it. Note that rows copied from a particular field can only be pasted into the same field, though it doesn't matter which page they are pasted to, so long as the user has access to edit both the page the rows were copied from and the one they are pasted to. Another thing to note is that only rows that have been previously saved to the page may be copied and pasted.


### Paste rows above or below selection

Paste copied rows above (or below) current selected row(s). If there are no selected rows then they will be pasted to the top if pasting "above", or bottom if pasting "below".


### Clear copy/paste buffer

This clears any rows currently present in the copy/paste buffer.


### Select all and Unselect all

This selects all rows currently in the field. The Unselect all action remove all currently selected rows from the selection, leaving no rows selected. You can also select or unselect rows by clicking the sort arrows for the row.


### Select all above or below

This selects all rows above (or below) the currently selected row(s), adding them to the current selection.


### Move selected rows to top or bottom

This moves the currently selected row(s) to the top (or bottom) of the field. In some cases this may be more handy than manually dragging the group of rows to the top or bottom, especially on pages having lots of rows in the field.


### Delete or undelete selected rows

This deletes (or undeletes) all currently selected rows. If you delete a newly added row (i.e. not yet saved row), it is removed immediately. But if you delete a row that was already present, then it is marked for deletion and not actually deleted until you save the page. Rows marked for deletion can be undeleted by clicking the Trash icon in their row, or by selecting them and then choosing the Undelete action.


### How to enable row actions

By default row actions are not enabled but enabling them is a matter of checking one box. Go to Setup > Fields > your_table_field > Details, then scroll to the bottom "Settings & Actions" fieldset. Click to open and check the box for the "Enable row actions?" setting.

If you find the "Enable row actions" setting is disabled, this means that your table has either automatic sorting or pagination enabled. Row actions are not supported when automatic sorting or pagination is enabled.


### Small inputs option

If you are using *AdminThemeUikit* (ProcessWire's current default) you can specify that Table should use smaller inputs. This is particularly useful on large table fields where you have many rows, as it enables you to fit significantly more information in the page editor before you have to scroll. This setting is also disabled by default, but can be enabled via a checkbox immediately below the Row Actions setting.


### Required columns

This new version of the Table field also supports required values for many column types. To make a column required, specify `required=1` in the column's Settings when editing your table field. While not new to this version, it's also worth pointing out that for "Select" types, you can specify `noblank=1` in the column's Settings to prevent it from showing a blank (unselected) option, which is another way of forcing a column to be required.


### Download

This version of ProFields table is available for download now as a beta version in the ProFields support board download thread (login required). ProFields Table is part of the ProFields package of Pro modules available for ProcessWire. Because this version (v28) has a lot of new features, it is initially released as a beta version and I recommend testing thoroughly in a development or testing environment before using in a production environment. For the current main/stable version use ProFields Table v26.
