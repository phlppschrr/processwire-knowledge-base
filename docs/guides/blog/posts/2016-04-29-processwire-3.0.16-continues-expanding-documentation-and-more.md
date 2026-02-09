# ProcessWire 3.0.16 continues expanding documentation and more

Source: https://processwire.com/blog/posts/processwire-3.0.16-continues-expanding-documentation-and-more/

## Sections


## ProcessWire 3.0.16 continues expanding documentation and more

29 April 2016 by Ryan Cramer [ 8 Comments](/blog/posts/processwire-3.0.16-continues-expanding-documentation-and-more/#comments)


## ProcessWire 3.0.16

[Last week](/blog/posts/processwire-3.x-api-reference/) I mentioned we'd be continuing the documentation updates into this week and that's exactly what we did. So rather than writing a lot about it here, I'd encourage you to go [check it out](../../../full/index.md), as that's where all the writing is this week! And actually, it was quite a lot! But I'll give you a summary here.

All in all, these documentation updates involved 46 files and 5264 additions, so far. That's a lot. It's the first time I think that I've had GitHub tell me that a commit was [too large](https://github.com/ryancramerdesign/ProcessWire/commit/f10bea0201bf4ae167230b8c4d69673759764898?diff=split) to display.


### ProcessWire core classes now in API reference

Last week I tried to get the main API variables covered. This week those were wrapped up, and then work on the most important core classes commenced. If you go look at the [ProcessWire 3.x API reference](../../../full/index.md), you'll now see more than 20 of the most used core classes now fully covered. Here's a few examples of what you might find…

- Ever wondered [what the core Wire class does](../../../full/wire/core/Wire/index.md)?
- Ever been curious about [all that you can do with a WireArray](../../../full/wire/core/WireArray/index.md)?
- Not totally clear on [what a NullPage is all about](../../../full/wire/core/NullPage/index.md)?
- Any questions on [what makes a Module a Module](../../../full/wire/core/_Module/index.md)? (there's a lot to see here)
- Ever needed a comprehensive list of methods, properties and constants available for an [Inputfield](../../../full/wire/core/Inputfield/index.md) or [InputfieldWrapper](../../../full/wire/core/InputfieldWrapper/index.md)?
- Ever wondered [what all the various methods in a Fieldtype were for](../../../full/wire/core/Fieldtype/index.md)?
- Interested in [what you can do with WireHttp](../../../full/wire/core/WireHttp/index.md)?
- Curious about some of the [fun tools available in WireArray](../../../full/wire/core/WireArray/index.md#pw-methods-fun-tools)?

You'll find all this, and much more in the latest ProcessWire 3.x documentation updates.


### ProcessWireAPI module update expands and improves output

Beyond the documentation updates to the core itself (which are now committed in 3.0.16), a lot of work also went into improving the ProcessWireAPI module which is parsing and outputting all the documentation. Here's just a few of the improvements below.

It can now display more extensive class documentation, like you see [here](../../../full/wire/core/_Module/index.md) for Module interface. This is all coming from Markdown in PHP comments directly in the core code. This enables us to really improve the documentation not just at the method level, but at the overall class level too. Last week our documentation was primarily limited to class methods.

There's now a "quick jump" select that lets you jump to anywhere in the API reference very easily. There's a lot of material in the API reference, so figured we needed something like this.

Last week a couple people asked about @since phpdoc support, which was in place, but not yet used for output. It's been enabled, and the requested changelog support has been added as well. Since there's no phpdoc @changelog tag (that I could find), we're instead using a #pw-changelog tag. You'll see both @since and #pw-changelog in use for [this method](../../../full/wire/core/Modules/method-getconfig.md), as an example.

There's lots more too, but stop reading and head on over to the [3.x API reference](../../../full/index.md). :) Please let me know if you spot any output issues along the way. Yes, there's still a lot more to cover in terms of core classes, but I think we've got the most used and most important ones pretty well covered now. I'll be continuing to add more and more though, this will be an ongoing process. Please let me know if you spot any major holes, or any additional classes you'd like to see here in the next updates.
