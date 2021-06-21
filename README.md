# wapy
## Python Whatsapp selenium api

Finally a tool that can verify if certain numbers exist on whatsapp without adding them to you contacts first.

**Direct messaging** also included!

The tool automatically skips any number that doesn't exist and fun part is __*everything is logged*__

USAGE
=====

<p>import and create an instance of wapy</p>
<code>
    from wapy import Wapy <br>
    instance = Wapy()
</code>
<br>
<p>set file for processed numbers</p>
<sub>#default</sub><br>
<code>
    instance.processed = "processed.txt"
</code>
<br>
<p>set file for verified numbers</p>
<sub>#default</sub><br>
<code>
    instance.success = "success.txt"
</code>
<br>
<p>add numbers</p>
<sub>
    accepted objects are:
</sub>
<ul>
    <li>iterable</li>
    <li>file_path</li>
    <li>string</li>
</ul>
<code>
    wapy.get_numbers(iterable|file_path|string)
</code>
<br>
<p>add text text to send</p>
<sub>#optional</sub>
<code>
    instance.text = "this text was automatically sent"
</code>
<br>
<p>run it by calling the instance</p>
<code>
    instance()
</code>
<br>

#### your web browser would open, scan the qr code and leave the rest to wapy