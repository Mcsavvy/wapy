# wapy
## Python Whatsapp selenium api

Finally a tool that can verify if certain numbers exist on whatsapp without adding them to you contacts first.

**Direct messaging** also included!

The tool automatically skips any number that doesn't exist and fun part is __*everything is logged*__

USAGE
=====

import and create an instance of wapy
<code>
    from wapy import Wapy <br>
    instance = Wapy()
</code>

<p>set file for processed numbers</p>
<code>
    instance.processed = "processed.txt"
    <sub>#default</sub>
</code>

<p>set file for verified numbers</p>
<code>
    instance.success = "success.txt"
    <sub>#default</sub>
</code>

<p>add numbers</p>
<sub>
    accepted objects are:
    <ul>
        <li>iterable</li>
        <li>file_path</li>
        <li>string</li>
    </ul>
</sub>
<code>
    wapy.get_numbers(iterable|file_path|string)
</code>