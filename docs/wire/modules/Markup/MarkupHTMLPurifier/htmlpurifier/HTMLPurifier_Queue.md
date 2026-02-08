# HTMLPurifier_Queue

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

A simple array-backed queue, based off of the classic Okasaki
persistent amortized queue.  The basic idea is to maintain two
stacks: an input stack and an output stack.  When the output
stack runs out, reverse the input stack and use it as the output
stack.

We don't use the SPL implementation because it's only supported
on PHP 5.3 and later.

Exercise: Prove that push/pop on this queue take amortized O(1) time.

Exercise: Extend this queue to be a deque, while preserving amortized
O(1) time.  Some care must be taken on rebalancing to avoid quadratic
behaviour caused by repeatedly shuffling data from the input stack
to the output stack and back.

## push()

Pushes an element onto the front of the queue.

## isEmpty()

Checks if it's empty.
