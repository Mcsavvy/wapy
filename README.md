# wapy
## Python Whatsapp selenium api

Finally a tool that can verify if certain numbers exist on whatsapp without adding them to you contacts first.

**Direct messaging** also included!

The tool automatically skips any number that doesn't exist and fun part is __*everything is logged*__

USAGE
=====

<pre>import and create an instance of wapy</pre>
<code>
    from wapy import Wapy <br>
    instance = Wapy()
</code>
<br>
<pre>set file for processed numbers</pre>
<sub>#default</sub><br>
<code>
    instance.processed = "processed.txt"
</code>
<br>
<pre>set file for verified numbers</pre>
<sub>#default</sub><br>
<code>
    instance.success = "success.txt"
</code>
<br>
<pre>add numbers</pre>
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
<pre>add text text to send</pre>
<sub>#optional</sub><br>
<code>
    instance.text = "this text was automatically sent"
</code>
<br>
<pre>run it by calling the instance</pre>
<code>
    instance()
</code>
<br>

#### your web browser would open, scan the qr code and leave the rest to wapy