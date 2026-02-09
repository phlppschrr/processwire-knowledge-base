# FieldsetGroup module released

Source: https://processwire.com/blog/posts/fieldsetgroup-module-released/

## Sections


## Part 3 of the Fieldset series: FieldsetGroup released

8 September 2017 by Ryan Cramer [ 0 Comments](/blog/posts/fieldsetgroup-module-released/#comments)

Last week we added the [FieldsetPage](/blog/posts/processwire-3.0.74-adds-new-fieldsetpage-field-type/) module to the ProcessWire core (dev branch). Today I've released the FieldsetGroup module in the [ProFields board](/talk/topic/6413-profields-download/) (requires login). This is a first beta release, and it requires ProcessWire 3.0.74 or newer. Like anything that's in beta, this is a test version, and may not yet be ready for your production sites. Think of it like the dev branch of the ProcessWire core. While I don't anticipate any major problems with it, I always suggest testing something new like this in an environment that isn't critical, where you can afford for things to go haywire (even if unlikely). This module has a lot of code behind it, and has the ability to add, modify or remove fields from all templates in your site, so it's a power tool in beta, be safe. :)

I'm releasing this in the ProFields board because it's easier for me to support it that way, at least in the short term. I have nearly a full day every week dedicated to Pro modules support and an established support system there that will help to ensure this module gets out of beta sooner rather than later. After getting feedback from more people and seeing what the usage is like, we'll either end up migrating it into the core, or keep it in the ProFields package. While FieldsetGroup and FieldsetPage (now in the core) do very similar things, they do it in very different ways. FieldsetPage is a little simpler and takes less planning, while FieldsetGroup is more of a power tool that has potential optimization and efficiency advantage at larger scales (since it doesn't use extra pages). We'll get more into the differences further down in this post.

Configuring a FieldsetGroup field:


### FieldsetGroup vs. regular Fieldset

From the technical side, FieldsetGroup does not replace or depreciate the existing Fieldset module that's been with ProcessWire since the beginning. It's actually an extension of the existing Fieldset module (literally, extends FieldtypeFieldsetOpen). It basically adds a managed layer on top of the existing Fieldset module.

FieldsetGroup is useful for fieldsets that you want to re-use in multiple templates, where you want it to be identical (or nearly so) in all usages. It enables you to manage the contents of the fieldset in a single place, rather than independently in each template. I've heard the example of an “SEO fieldset” mentioned a few times, and I think that's an excellent example of where you might use FieldsetGroup (or FieldsetPage, already in the core).

Where you would likely want to keep using the original Fieldset type (FieldtypeFieldsetOpen), is in cases where you are using it with a single template, or in cases where you might be adjusting the settings of fields in the fieldset on a per-template basis. The original Fieldset type is still the most flexible and efficient way to create fieldsets and tabs. The new fieldset types are not intended to replace it. Instead, the new fieldset types are there to save you time by simplifying the initial setup and ongoing management of a fieldset.


### FieldsetGroup vs. FieldsetPage

The primary benefit of FieldsetGroup over FieldsetPage is that it accomplishes something very similar without using any extra pages in the system. Ironically, depending on your needs, this is also the primary benefit of FieldsetPage over FieldsetGroup. Since FieldsetPage uses an extra page for the fieldset, fields live in their own namespace, thus enabling the same field(s) to be re-used inside and outside of the the fieldset. But with that namespace comes the overhead of another page. Though you'd have to be pretty large-scale before that would be much of a consideration. But as you can see, what's a benefit or drawback really depends on the case. And that's why these two new Fieldset types have been developed alongside each other.

FieldsetGroup lets you dictate whether it should appear as a Fieldset or as a Tab. FieldsetPage does not provide this option at present (though I am looking into it).

Performing `$pages->find()` queries on pages using FieldsetGroup is more straightforward and efficient because its fields live on the same page that the fieldset lives on. The fields behave the same way as any other field on the page in any API scenario.

Accessing or manipulating fields is equally simple for either of the fieldset types. However, the code to do it will be different. With FieldsetGroup you get or set `$page->field` directly (with no mention of the fieldset), whereas with FieldsetPage you get or set `$page->fieldset->field` with that “fieldset” layer in between the `$page` and the `field`.

It's actually possible to add fields to a FieldsetGroup for a single template, so that the fieldset contains an extra field (or fields) in a particular context. To do this, you just edit the template and add the field into the fieldset there (rather than adding it from the fieldset). Note the earlier screenshot that had the “Just FYI” section – it was telling us that there was an extra “body” field present in the fieldset for the “about-core” template. This is something you can't do with FieldsetPage.

When you delete a field from a FieldsetGroup, you can choose to delete the field and data, or just remove the field from the fieldgroup, leaving the field on the template along with any data it contains.

What appears when you remove a field from the fieldgroup:


### Wrapping up

With FieldsetGroup now released in beta, and FieldsetPage added to the core, that wraps up our 3-week trilogy on fieldsets. Next week we'll be looking at some updates to ProDrafts that have been in development for a long time. **We'll also be releasing a new open source module for ProcessWire that I'm excited about**, but I'll save that for next week. After next week, we'll be back to core development and focused on covering issues reports, working towards getting our current dev branch to the next master version. Hope that you all have a great weekend and enjoy reading the [ProcessWire Weekly](http://weekly.pw).

PS: *If you have a moment, please vote for ProcessWire in CMS Critic's “Best Small Business CMS” (SMB) category, located [here](https://www.cmscritic.com/awards/2017-web-nominations/). *
