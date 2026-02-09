# ProcessWire 3.0.74 adds new “FieldsetPage” field type

Source: https://processwire.com/blog/posts/processwire-3.0.74-adds-new-fieldsetpage-field-type/

## Sections


## ProcessWire 3.0.74 adds new “FieldsetPage” field type

1 September 2017 by Ryan Cramer [ 5 Comments](/blog/posts/processwire-3.0.74-adds-new-fieldsetpage-field-type/#comments)


## ProcessWire 3.0.74

Last week we talked about [new Fieldset modules](/blog/posts/processwire-3.0.73-and-new-fieldset-types/) for ProcessWire, and I was happy to hear about all the enthusiasm for these. In that post, we primarily looked at the new *FieldtypeFieldsetGroup* module in detail. This week we'll continue along a similar subject and look at the new *FieldtypeFieldsetPage* module. Actually we'll do more than look at it, we'll release it – it's now in ProcessWire core version 3.0.74, ready for you to use.


### What is FieldsetPage?

FieldsetPage uses a separate page (behind the scenes) to store values for the fields you select when configuring the fieldset. Relative to other types of fieldsets, a major benefit is that you can re-use fields that might already be present on your page, outside of the fieldset. For example, you could have a “title” field on your page, and another in your fieldset. Likewise for any other fields. This is possible because fields in the fieldset are in their own namespace. That namespace is another page, separate from the main page.

FieldsetPage also shares the benefit of FieldsetGroup – any changes made to the fieldset immediately apply to all usages of the fieldset, regardless of template or page. With a regular fieldset, if you wanted to add a field, delete a field, change the order, or change something about the context, you would have to make the same change on all templates where the fieldset is used. So using FieldsetPage or FieldsetGroup can be a big time saver when it comes to both initial setup and future changes.


### Why is FieldsetPage in the core?

The new *FieldtypeFieldsetPage* module was added to the core because it is very closely related to another core Fieldtype: *FieldtypeRepeater*. In fact, its classes extend those of Repeaters. By keeping it right alongside the Repeater module, I feel it will be simpler and more reliable to manage the future evolution of each as a pair. Especially since changes to one may sometimes involve changes to both. In addition, after using it quite a bit this week, I think there's a very good chance that this new module will see just as much use as Repeaters.

Because this module is already in the core, you already have it once running core 3.0.74 or newer. All you need to do is install it:

- Grab the latest dev branch, version 3.0.74 or newer.
- The core FieldtypeRepeater module is required, make sure that is installed.
- In the admin, go to Modules > Refresh.
- Go to Modules > Core > Fieldtype > Fieldset (Page), and click “Install”.
- Create a new field (Setup > Fields > New) and use “Fieldset (Page)” as the type.


### How does FieldsetPage differ from FieldsetRepeater?

While closely related to Repeater, they are quite different in appearance and usage. FieldsetPage is not just a simple “min=1, max=1” repeater. Far from it. Here are a few notable differences:

1. As the name suggests, FieldsetPage uses a separate Page to store data in the Fieldset. But Repeaters use a parent page plus 1 additional page per repeater item. Meaning, a populated repeater uses a minimum of 2 pages. But FieldsetPage instead uses a different storage mechanism that consumes a maximum of 1 page. So we are taking advantage of the known quantity “1”, to make it more efficient.

2. With just one Fieldset that is always present, there's no need for sorting, extra buttons or controls. Visually it looks nothing like a Repeater and instead looks identical to a regular Fieldset:

3. The API side is a whole lot simpler than with a Repeater. Since there can only be one item (the Fieldset), it is always present and accessible. Getting a value from an existing page is as simple as `$page->fieldset->title` and setting a value is as simple as `$page->fieldset->title = "Something";` There is nothing else to do or to check. When `$page` is saved, so is the Fieldset. See the API section of this post for more details.

4. Configuring a FieldsetPage is also simpler than configuring a Repeater. The only thing you have to decide is what fields will be in the Fieldset. It also comes with API instructions built-in (which we'll repeat in this post below).


### Using FieldsetPage from the API

As mentioned in the last section, using and manipulating FieldsetPage values from the API is very simple. It's pretty much identical to how you'd work with a single Page field. Only it's simpler than that, because it's always present, so there's no need to check if there is a selection or NullPage, or anything like that. Below are several API usage examples. The following examples assume we have a FieldsetPage field named "fieldset", and that it has a "title" field within it.

```php
// Getting a value:
$title = $page->fieldset->title;

// Outputting a value:
echo $page->fieldset->title;

// Setting a value:
$page->fieldset->title = 'This is some example text';

// Setting and saving a value:
$page->of(false); // when necessary
$page->fieldset->title = 'This is some example text';
$page->save();

// Assigning fieldset to another (shorter) variable:
$p = $page->fieldset;
echo $p->title;

// Finding pages
$items = $pages->find('fieldset.title%=example');
```


### Update on FieldsetGroup module

The other Fieldset type that we introduced last week (FieldtypeFieldsetGroup) isn't quite ready to release yet. Actually, it probably is, but I spent so much time this week getting the FieldsetPage module ready, that I didn't get enough time to invest in doing the necessary exhaustive testing of the FieldsetGroup module. That's what I'll be working on next week, and I'll have it ready by the end of the week. I'm going to release the beta version in the ProFields board by this time next week. If after using it, the testers feel it belongs in the core, then we'll look at adding this one to the core too.

One thing that I did add to FieldsetGroup since last week's post is the ability for the Fieldset to behave as a Fieldset or a Tab. A radio button in the field configuration lets you decide.

Thanks for reading! I look forward to hearing how FieldsetPage works for you. Unrelated, but one other thing I wanted to mention is that all the ProFields modules now support pages export/import, as is available on the current core dev branch. New versions were posted for most of the ProFields last week, so if you are using ProFields and export/import, make sure you grab the latest versions. Hope that you enjoy your weekend and likewise enjoy tomorrow's upcoming [ProcessWire Weekly](http://weekly.pw).
