<br></br>
<p align="center">
  <a>
    <img alt="SoikRs" title="SoikRs" src="https://avatars.githubusercontent.com/u/112499783?v=4">
  </a>
</p>
<p align="center"> POC (This is not meant to be used) </p>
<p align="center"> A python project to facilitate DataBreaches indexation and searching.</p>
<br></br>

### Current functions

<span style="color:#b45e02">Function</span> | <span style="color:#5f1e2d">Command</span> | <span style="color:#aa5502">Argument</span>
--- | --- | ---
Indexation of a Database   | python main.py -t [file] | file in the `tosort` folder
Search of Databases      | python main.py -r [email] | email in the `*@*` format

### Indexation of a Database
The command will take a `file` as argument. The function will then find emails on this file that respect the `*@*` format. On each email found the function will extract the first two letters or numbers (a and b). It will then add the whole line where the email is contained to the `./a/b/ab.txt` text file. This will permit when performing searches to more or less divide the number of lines to search by `36*36=1296`.

### Search of Databases
This command will take an `email` with the `[\w.+-]+@[\w-]+\.[\w.-]` format. It will then ask after being executed if the user want to only search locally or also with APIs. These `APIs will need to be configured on the main.py file`. If the user choose not to search with apis then the function will search on the `./a/b/ab.txt` text file with a and b being the first two letters or numbers from the email and return the line. If the user choose to use APIs services then the email will also be searched on the `leakcheck.net` website and their existence will be verified by the `isitarealemail ` API. After performing APIs task it will `search the email locally`. After that, if an email is found on the local database then the line where the email is will be scanned for an ip and then the API will give basic informations about it (whois, approximative location...).
