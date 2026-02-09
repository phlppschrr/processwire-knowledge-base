# ProcessWire 3.0.73 and new Fieldset types

Source: https://processwire.com/blog/posts/processwire-3.0.73-and-new-fieldset-types/

## Sections


## ProcessWire 3.0.73 and new Fieldset types

25 August 2017 by Ryan Cramer [ 11 Comments](/blog/posts/processwire-3.0.73-and-new-fieldset-types/#comments)


## ProcessWire 3.0.73

This post is all about fieldsets in ProcessWire. Version 3.0.73 adds some nice UI upgrades when it comes to working with them. Plus we cover two new modules we have in development for managing groups of fields in fieldsets.


### New fieldtypes for fieldsets

In last week's [ProcessWire Weekly #171](https://weekly.pw/issue/171/), there was a poll titled “*what's the one feature that would add a lot of value to ProcessWire, but isn't currently on our roadmap?*” The winner in the poll at the beginning of this week (and still the winner today) is for “*A group fieldtype that allows sharing groups of fields between templates; similar to Repeaters, but without repeating or the need for separate pages behind the scenes.*”

I agree, this would be really nice to have, and it seemed like something that could be built without taking too long. So I got to work on it this week. While I don't have it ready just yet, I can tell you a little bit more about what's being built. And hopefully by this time next week, it'll be ready to use.

I'm building the new Fieldset features out as two different modules, each of which approach the need quite differently. These modules include FieldtypeFieldsetGroup and FieldtypeFieldsetPage. This week we'll cover both, but focus in on FieldtypeFieldsetGroup.


### Fieldset Group (FieldtypeFieldsetGroup)

This is a new module that I actually just finished coding today, but it turned out to involve quite a bit of code, so I want to give it a week of testing before asking others to try it. This module extends the existing Fieldset type in ProcessWire, but with one big difference: the group of fields that are contained within it are managed by it. So when you create a new Fieldset Group field, it then asks you to start adding fields to it:

Then you can add that Fieldset Group field to any templates, and they inherit all the fields in the group. For instance, the Fieldset Group we configured above looks like this in the page editor:

You can create a single field and add it to a dozen templates in one shot. No more need to add fields one-by-one, then drag each into a fieldset, and then repeat for each template. Meaning, this Fieldset Group can save you a lot of time. It literally adds the fieldset, and all the fields within the fieldset to each template using the fieldset.

**Mirroring changes** The usefulness of Fieldset Group goes beyond the initial creation and configuration of fields. Any changes you later make to that Fieldset Group (like adding new fields or changing the order of them) automatically get applied to to all appearances of the group, across all the templates using it.

**Contexts** Fieldset Group also supports template-field context. Meaning, you can adjust properties of each field (like width, visibility, label, etc.) within the context of the group. Those context changes automatically migrate to all the templates using the Fieldset Group. If a template has also applied context changes to a field within the group, then the two sets of context changes are merged with one another, so that both apply.

**Already familiar** There's nothing new to know about Fieldset Group fields on the API side. When you add a Fieldset Group to a template, the fields within it become fields of the page. The Fieldset Group does NOT add another layer that you must access them through on the API side. Meaning, if you added a Fieldset Group field to a template, and it contained a field named "author", then it would be accessed as `$page->author`. So its behavior is identical to that of Fieldsets that you already use in ProcessWire, and the fields within it are literal fields on the page.

**Any drawbacks?** The above is also a potential drawback of Fieldset Group fields for some. If a template already has a field named "author", and the Fieldset Group also has the "author" field, then that Fieldset Group field cannot be added to the template, since it already has an "author" field. But what if there were another layer between them? This is where the next type the we're going to talk about comes into play (FieldtypeFieldsetPage), and we'll spend more time talking about that in next week's post. But I'll just say a couple things briefly about it below:


### Fieldset Page (FieldtypeFieldsetPage)

The new Fieldset Page type accomplishes something very similar to the Fieldset Group type, but in a very different way. As the name implies, the necessary "layer" is in fact a separate page behind-the-scenes, similar to the Repeater approach. From the API side, rather than accessing `$page->field`, you would access `$page->fieldset->field`, where "fieldset" is the name of the fieldset, and "field" is of course the name of the field.

This fieldset type is represented by a Page, and because of that, it doesn't fit the requirements of the poll answer of “without requiring pages behind the scenes”. But I think a page is incredibly useful in this context, and I think you will agree when using it. Also, given the fact that we'll have two new grouped Fieldset types available, you'll be able to choose which best solves your needs. I'll cover a little more about Fieldset Page next week.


### ProcessWire 3.0.73 updates

As usual, this week's version includes some bug fixes and general tweaks. But it also contains a lot of updates having to do with fieldsets as well. In coding two new Fieldset modules this week, I found there were some core aspects that needed improvement, both on the interface/code side, and the UI side. On the UI side, the way that you interact with Fieldsets is now greatly improved:

**Moving fieldsets** Previously when you moved (dragged) a fieldset, it only moved where the fieldset started, and didn't move anything within it. Meaning, if you wanted to change the placement of a fieldset in a template, you would not only have to drag the rows for the fieldset start/end, but every single field within the fieldset as well. You'd essentially have to re-create the fieldset with your mouse, just to move it to another spot in the template. If you've ever had to do this, you know what a hassle it can be, especially on templates where you are using a lot of fieldsets and fields. No longer. Now when you drag a fieldset, it drags the whole thing on one shot!

**Adding fieldsets** While not as big of a deal as moving fieldsets, adding fieldsets in templates wasn't as straightforward as it could have been. You not only had to add the fieldset, but also the fieldset_END field as well, as two separate additions. Now when you add a fieldset, it automatically adds the fieldset_END as well, which just makes sense.

**Fieldset support added to asmSelect** Previously fieldset support was bolted in to our template editor, so that was the only place where you could visually see fieldsets. If you wanted fieldsets when configuring a repeater (or another type), you weren't able to see them in the right context and indentation. This week we added fieldset support natively to the our jQuery asmSelect plugin, so that fieldsets can now be visually represented anywhere that asmSelect is used for ordering fields.

Here's a short GIF screencast to demonstrate the upgrades for moving and adding fieldsets, now available in ProcessWire 3.0.73:

That's all for this week, hope that you have a great weekend. We'll be back next week with ProcessWire 3.0.74 and hopefully two new modules.
