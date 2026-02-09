# Field permissions, overrides and more (2.6.2)

Source: https://processwire.com/blog/posts/field-permissions-overrides-and-more-2.6.2/

## Sections


## Field permissions, overrides and more (2.6.2)

29 May 2015 by Ryan Cramer [ 8 Comments](/blog/posts/field-permissions-overrides-and-more-2.6.2/#comments)

This week, ProcessWire 2.6.1 was made the new master version. In addition, ProcessWire 2.6.2 was pushed to the dev branch with all new field level access control and overrides support!


### **Granular access control with field level permissions**

This week we added field-level permissions to ProcessWire's core. This is the biggest update to ProcessWire's access control system in a long time, and it opens a whole new range of possibilities.

Previously, all access control was at the page level (defined at the template level). So you could limit edit and/or view access to pages, which included access to all the fields on that page… This is of course the most common and useful scenario when it comes to access control. But what if you wanted to limit view and/or edit access to a particular field, site-wide? Or perhaps just within the context of a particular template? Now you can.


### How field permissions are defined

When editing a field (Setup > Fields > any field) you now have a new Access tab, which is a lot like the one you see when editing a Template. When you enable Access Control for that field, it opens another group of fields where you can define what roles have view and edit access.

In order for a user to have edit access to a field, they must also have edit access to the page, as a prerequisite. Likewise–as you would expect–in order to have view access to a field, you must also have view access to the page where the field lives.


### Field permissions can also be defined in template context

When editing a field within the context of a particular template*, you also have a dedicated Access tab that lets you override any access control settings (or lack of them) specific to a particular template.

*To edit a field within the context of a template, edit the template (Setup > Templates > any template) and click any field name in the list shown on the default tab (Basics tab). This opens a modal window where you can adjust the settings of that field so that they only apply to instances of that field on pages using that template.


### How edit permission works

If you configure a role not to have edit access to a field that they otherwise would, then they will simply no longer see it in the page editor. They will be editing the page as if the field didn't exist, with no ability to modify any existing value that may be present. If you want them to see the value, but not be able to edit it, then we've got a checkbox that enables you to do that.


### How view permission works

Edit permission has to do with the PW admin side, whereas view permission has more to do with the front-end of your site. It determines whether or not a value from a particular field is accessible to a user.

When a user lacks view permission to a particular field on the page, ProcessWire simply replaces the value accessed from the API with a blank value of the expected type. Meaning, if it was a populated text field, then it becomes an empty string of text. Or if it was a Page field, then it becomes a blank PageArray. And so on. The point is that the expected type remains in tact, even if the content isn't present. This ensures that you can remove view access from a particular field without potentially breaking any existing code on the front-end of your site.

An important point to mention about this blank value substitution is that it only applies when a Page's output formatting is ON. This is to ensure that pages with non-viewable values aren't saved to the database, potentially replacing populated values.

*As a reminder, pages on the front-end of your site always have output formatting on, unless you've turned it off, with* `$page->of(false)`.

Another point to mention about the blank value substitution is that you can turn it off if you want to. There is a checkbox provided in the field access control settings to do just that. Should you disable the blank value substitution behavior, you can still perform your own access control checking from the API, like this:

```
if($page->viewable("my_field")) {
  // my_field is viewable
  echo $page->my_field;
} else {
  // my_field is not viewable
}
```

The `$page->viewable("my_field")` works regardless of whether output formatting is on or off.


### Using field permissions

Something to keep in mind when using field permissions is that it's a bit of a new paradigm for ProcessWire. Such granular control has previously not been available in the ProcessWire core. That means that you may come across situations where field permissions aren't taken into account, particularly when it comes to 3rd party modules.

Anything on the back-end API side has to specifically call `$page->viewable('field');` or `$page->editable('field');` before it knows if the field is viewable or editable, and this is a permission check that hasn't been necessary before. Use field permissions where they suit your needs and always thoroughly test that the access control works the way you expect, and in all the places where you expect it to.


### What's missing?

We don't yet have a built-in capability to limit edit access control by language (in a multi-language site), at least not without using hooks. However, there is demand for it and we do have plans to add this on the 2.6 dev branch, hopefully soon.


### **New “overrides” tab in field editor**

After putting in the new field-level access control features mentioned above, I thought "how am I going to keep track of this?" After all, access control, like many other field properties, can be defined with the field, and then overridden within the context of a specific template. There's no easy way to see, at a glance, all the variations a field might go through across all templates in your site.

While this ambiguity wasn't so much of an issue before, ambiguity has no place when it comes to access control. So with the new access control additions this week, the entire field editor received an upgrade to make it really clear what settings are being overridden, and where.

The new Overrides tab in the field editor appears only when the field has one or more of its settings overridden (by way of field-template context). It provides an easy way to see, at a glance, all variations of the field settings on a per-template basis. It highlights any setting that is overridden.


### Easily remove overridden properties

In addition, the Overrides tab gives you the ability to selectively remove any of the overrides individually, or as a group. Previously, the only way you could do this was to edit the field in the context of a template, and then restore it to the original value manually.


### Overrides work in template context too

When editing a field from a template (thereby editing it within the context of a specific template) you also get an Overrides tab in your modal window. The content of this Overrides tab is just like the one you see when editing the field outside of any context, except that it focuses only on the settings overridden by the template you are editing for. Like with the other Overrides tab, you can also remove any settings, easily restoring them to their original value.

Field-template context is one of ProcessWire's most useful and best kept secrets, as many people don't realize it's even there until they are specifically looking for it. This new Overrides tab greatly increases the usefulness and clarity of field-template context.
