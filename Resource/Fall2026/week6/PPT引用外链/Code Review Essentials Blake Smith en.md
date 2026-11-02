# Code Review Essentials Blake Smith

> 来源：<https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
Code Review is an essential part of any collaborative software project. Large software systems are usually written by more than one person, and so a highly functioning software team needs a robust process to keep its members, as well as the code base itself moving in the right direction.
Code Review is a powerful tool that:
- Helps team members adapt their mental model of the system as it’s changing
- Ensures the change correctly solves the problem
- Opens discussion for strengths and weaknesses of a design
- Catches bugs before they get to production
- Keeps the code style and organization consistent
It’s helpful to think of these benefits as a hierarchy of needs.
Keeping Team Members Together
The most critical function of a Code Review is to keep every member of the team moving in the right direction. You can’t safetly change a system you don’t understand, and so Code Review keeps the team mentally aligned together. When Bob submits a pull request for the accounting subsystem, Amy keeps her mental model of that system updated as she reviews Bob’s code. Amy gets the chance to ask questions about pieces she doesn’t understand, and Bob gets the benefit of clarifying his design decisions as well as teaching someone else about his work. When Amy has to make a change to the accounting subsystem a month later, her mental model of the system is already up to date and ready for action. She spends less time reading code and trying to piece the system together in her brain, and more time thinking about higher level abstractions and designs. Everyone wins, because everyone stays together.
Executing a Good Pull Request
Before you even write a line of code changing the system, ask yourself the following questions:
- “Is this the right thing to be working on?” There will always be competing needs from customers, internal team members and other parties. This can be a good way to keep priorities straight in your head before you dive in deep. Other processes like iteration / sprint planning meetings also help keep this on track.
- “Does the team already agree that the change is the right one?” If not, it’d be better to start a design discussion by email or maybe in person. Your changes are more likely to get accepted when people are in agreement about the design before you change it.
- “How can I break this change into digestable chunks that are easy to review and understand?” Small changes are easier to think about and understand. Good discussions flow from the team being able to comprehend your change quickly. If your change is massive, teammate’s eyes will glaze over, and you might only get a few style nitpicks from them.
- “How am I going to test this change to kill bugs and ensure correctness?” You might have a QA department, but it’s still your job as the developer to ship quality working software. Easily testable software is usually more decoupled, is broken into smaller chunks, and easier to reason about. You need to have a testing plan for all your changes.
I’ve found that answering these questions ahead of time has saved me a lot of headache in the long run. The last thing you want to do is spend days coding up a change only to have it rejected based on fundamental design flaws or team disagreement. Or for your change to get held up because no one can verify it for correctness. Again, the goal is to change the system while keeping other team members up to date with your changes. Asking yourself about how you’re going to break your work into bite-sized chunks and test those chunks is helpful on many fronts:
- It reduces risk
- It makes changes easier to reason about
- It pushes you towards a better design
You’d rather make many small, precise cuts with a scalpel than one giant gash with a machete. I prefer scalpel driven developement in most additive cases, and like to save the machete for when it’s time to delete large blocks of dead code.
Sending the Pull Request
Ok, so you’ve gotten buy-in from the team that your changes are good, and you’ve achieved the design you set out to build. What’s the most effective way to actually send your pull request? You’ve been working hard on your changes, and you want other members of your team to pay attention to your pull request and give you fast feedback. How can you do that?
Remember earlier when I said that the most important part of a code review is to keep the team’s collective mental model well aligned? Your other teammates are probably working on something completely different than you, maybe in a completely different part of the system. Their brains are in a completely different context, so you must overcome this by giving them the helpful guidance they need to do the review. This means writing a well-organized description of the changes you made, why you made them and any other relevant information they won’t get from just reading the code alone. Don’t make your teammates do more mental work than they have to.
Let’s look at some good and bad examples of pull request descriptions:
Bad Example:
Title: Fix uninitialized memory bug
Description: 
This is the bug Bob and I talked about earlier. I had
trouble with the compiler but managed to make this work. Let me
know what you guys think.
If you’re the developer of this pull request, stop and put yourself in your code reviewer’s shoes for a second. The title is vague, and raises more questions than answers: Where is the memory bug? How critical is this change? What was the bug that Bob and you talked about earlier? What trouble did you have with the compiler? The description doesn’t provide any helpful context about the problem, nor does it provide any helpful description of your changes. If this pull request is long, the reviewer is going to have to dive into the code and do mental gymnastics in an attempt to gain context before even getting a chance to think about how this change fits in to the coherent design of the system.
Here’s a improved example that helps clarify the changeset:
Title: Fix process crash on startup from uninitialized memory [#54633]
Description:
This bug was causing process crashes on boot due to a memory
initialization error in our statistics Counter class. I talked this
over with Bob, and we both agree the crashes are a rare edge case
that don't warrant a hot-fix release. Here's a summary of the
changes:
  - Moved the underlying int variable into the class initializer
    to prevent ununitialized memory in the Counter.
  - Reworked the Counter interface to simplify caller conditional
    logic and prevent further off-by-one counting problems.
  - Added a unit test that exposes the crash
Testing: I've verified the test suite still passes, and verified
manually that the crash doesn't happen locally.
A few things that have improved in this pull request description: The title is descriptive enough to give the reviewer some short context, and entice them to click on the email and learn more. The reviewer knows it’s a process crash (which is usually a really bad thing) and there’s also a bug report number where the reviewer can read more details about the bug report if they’re interested in understand more about the problem. The new description also outlines where the problem was occuring, and helps give some context about how critical the fix is. There’s a summary that lists the high level structural changes in the pull request, which will give the reviewer a mental picture of the changes before they even look at the code. Code reviewers should not be surprised with what they find. This example also outlines testing that was performed, which will give reviewers confidence that the changes were well thought out, well tested and ready to be merged. Set your reviewers up for success by making it stupid easy for them to click ‘merge’.
Reviewers: Giving Constructive Feedback
The next part of the review process to consider is giving constructive feedback to your peers. If the goal is clarity and alignment, giving quality constructive feedback helps everyone understand the system better and push towards better code.
Avoid saying things like:
- “This design is broken.” Why is it broken? How can it be made better? Statements like this hurt confidence and can bruise egos.
- “I don’t like this change.” Why don’t you like it? What would you like instead? It’s okay to not like something, but you should articulate your thoughts and provide helpful clues about how the code can be improved.
- “Can you rewrite this to be more clear?” What’s wrong with what I have now? How should I rewrite it? What’s unclear? Comments like this are themselves unclear, and don’t give a simple path forward.
Instead, say things like:
- “How does this code handle negative integers?” This feedback is specific, and causes the developer to think through the outcomes themselves. As a reviewer, you might know that the code in question crashes with negative integers, but it’s better to have the developer intuit this themselves. Questions like this might also be indicative of a testing gap, or a need for further specification of scope.
- “This section is confusing to me, I don’t understand why class A is talking to class B” If the developer hasn’t provided a helpful description, and the code isn’t neatly structured, this kind of comment helps drive for clarity of design and cleaner code.
- “It looks like you broke an interface boundary here. How will that affect the user?” You’ve pointed out an issue you noticed, giving them the benefit of the doubt that they meant to do it. Now they can think through the unseen ramifications of breaking the interface boundary and either provide a rationale for their decision, or choose to change it.
In general, framing feedback as questions is a good way to drive for clarity, correctness, and at the same time help the developer improve their designs in the future. This is usually how quality creative writing groups give each other feedback. In a creative writing setting, it’s harmful to say things like, “I don’t li

*[Snapshot truncated for archival size; images omitted.]*
