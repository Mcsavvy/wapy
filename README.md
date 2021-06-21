# wapy
## Python Whatsapp selenium api

Finally a tool that can verify if certain numbers exist on whatsapp without adding them to you contacts first.

**Direct messaging** also included!

The tool automatically skips any number that doesn't exist and fun part is __*everything is logged*__

USAGE
=====

<p> import and create an instance of wa </p>
<code>
    from wa import WA <br>
</code>
<p>set file for processed numbers</p>
<code>wapy.processed = "processed.txt" #default</code>
<p>set file for verified numbers</p>
<code>wapy.success = "success.txt" #default</code>
<p>add numbers to wapy</p>
<sub>accepted objects are</sub>
<ul>
    <li>iterable</li>
    <li>file_path</li>
    <li>string</li>
</ul>
<code>
    wapy.get_numbers(iterable|file_path|string)
</code>