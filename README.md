
# Table of Contents

1.  [Dataset](#org3dd9f02)
    1.  [Variables](#orga515b07)
    2.  [Data sources](#org45071ac)
2.  [Prototyping](#orgb16eece)
    1.  [Features](#org4d62125)
    2.  [Wireframe](#orgc75fbbf)
3.  [Development](#org5d7c271)
    1.  [Why did we pick Dash?](#org6bb8b0f)
    2.  [Architecture](#org62034f7)
        1.  [Structure of `app.py`](#orgc5a495b)
            -   [Globals](#orgdf50091)
            -   [Layout](#orgcf27bb2)
            -   [Callbacks functions](#org6c0d94c)
    3.  [Visual identity guidelines](#org62126d5)
        1.  [Colors](#org7e9022a)
            -   [Primary colors](#org1d71a13)
            -   [Secondary colors](#org796fa6a)
        2.  [Fonts](#org532f3e2)
            -   [Primary fonts](#orged276ed)
            -   [Secondary fonts](#orgaebfa1f)
        3.  [Logo](#org036d018)
            -   [Symbol](#org7a973bc)
            -   [Logotype](#org26eff21)
    4.  [How to contribute](#org5a4d266)
        1.  [Setting up a new Git repository](#orgf75e7bc)
        2.  [Adding or modifying owned files (`push`)](#orgf591423)
        3.  [Submit proposed changes to review](#orga412103)
4.  [Tools that we used](#org83fe082)



<a id="org3dd9f02"></a>

# Dataset


<a id="orga515b07"></a>

## Variables


<a id="org45071ac"></a>

## Data sources


<a id="orgb16eece"></a>

# Prototyping


<a id="org4d62125"></a>

## Features


<a id="orgc75fbbf"></a>

## Wireframe


<a id="org5d7c271"></a>

# Development


<a id="org6bb8b0f"></a>

## Why did we pick [Dash](https://plotly.com/dash/)?

As we wanted to use Python to build the Dashboard we had to pick among [Python dashboard libraries](https://pyviz.org/tools.html) :

![img](./Pics/dashboardlibraries.png "Python dashboarding libraries")

According to following benchmarck the team decided to develop the PoC with ****Dash****

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Maturity</th>
<th scope="col" class="org-left">Popularity</th>
<th scope="col" class="org-left">Simplicity</th>
<th scope="col" class="org-left">Adaptability</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Streamlit</td>
<td class="org-left">C</td>
<td class="org-left">A</td>
<td class="org-left">A</td>
<td class="org-left">C</td>
</tr>


<tr>
<td class="org-left">Dash</td>
<td class="org-left">B</td>
<td class="org-left">A</td>
<td class="org-left">B</td>
<td class="org-left">B</td>
</tr>


<tr>
<td class="org-left">Voila</td>
<td class="org-left">C</td>
<td class="org-left">C</td>
<td class="org-left">A</td>
<td class="org-left">C</td>
</tr>
</tbody>
</table>

****Maturity****: Based on the age of the project and how stable it is.

****Popularity****: Based on adoption and GitHub stars.

****Simplicity****: Based on how easy it is to get started using the library.

****Adaptability****: Based on how flexible and opinionated the library is.


<a id="org62034f7"></a>

## Architecture


<a id="orgc5a495b"></a>

### Structure of `app.py`


<a id="orgdf50091"></a>

#### Globals


##### Loading libraries, style, and data

-   Libraries

-   Style

-   Pandas DataFrame


##### Data prep


##### Global functions


<a id="orgcf27bb2"></a>

#### Layout


<a id="org6c0d94c"></a>

#### Callbacks functions


<a id="org62126d5"></a>

## Visual identity guidelines


<a id="org7e9022a"></a>

### Colors


<a id="org1d71a13"></a>

#### Primary colors


<a id="org796fa6a"></a>

#### Secondary colors


<a id="org532f3e2"></a>

### Fonts


<a id="orged276ed"></a>

#### Primary fonts


<a id="orgaebfa1f"></a>

#### Secondary fonts


<a id="org036d018"></a>

### Logo


<a id="org7a973bc"></a>

#### Symbol


<a id="org26eff21"></a>

#### Logotype


<a id="org5a4d266"></a>

## How to contribute


<a id="orgf75e7bc"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_carbon4/tree/master/plateforme
-   Ask to join our GitHub


<a id="orgf591423"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="orga412103"></a>

### Submit proposed changes to review

When modifying an existing file, if you're not its owner, you have to submit the modifications to its owner (i.e. reviewer). Ownership is distributed as follow :

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Owner GitHub name</th>
<th scope="col" class="org-left">File</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">linetonthat</td>
<td class="org-left">??</td>
</tr>


<tr>
<td class="org-left">j-back</td>
<td class="org-left">??</td>
</tr>


<tr>
<td class="org-left">morgandavidson</td>
<td class="org-left">??</td>
</tr>
</tbody>
</table>

To submit changes reviewees have to do: 

    $ git checkout -b pick_a_branch_name
    $ git push origin pick_a_branch_name
    $ git add filename
    $ git commit
    $ git checkout master

Then go on our [GitHub](https://github.com/dataforgoodfr/batch8_worldbank), 

-   cilck on `Pull requests`,
-   then on `New Pull Request`,
-   click on `compare across forks`,
-   select : `dataforgoodfr/batch8_carbon4 | =base: master` <- `revieweename/batch8_carbon4` | `pick_a_branch_name`,
-   click on `create pull request`
-   enter GitHub reviewer name in `reviewers`, add title and comment,
-   click on `create pull request`


<a id="org83fe082"></a>

# Tools that we used

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Tools</th>
<th scope="col" class="org-left">Usage</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Slack</td>
<td class="org-left">Chat</td>
</tr>


<tr>
<td class="org-left">Pycharm, Jupyter</td>
<td class="org-left">Code editing</td>
</tr>


<tr>
<td class="org-left">Git, GitHub</td>
<td class="org-left">Code storage/versioning</td>
</tr>


<tr>
<td class="org-left">Python, CSS</td>
<td class="org-left">Coding languages</td>
</tr>


<tr>
<td class="org-left">Org-mode, Github, Notion</td>
<td class="org-left">Documentation</td>
</tr>


<tr>
<td class="org-left">Zoom</td>
<td class="org-left">Meetings</td>
</tr>


<tr>
<td class="org-left">dash, pandas</td>
<td class="org-left">Python librairies</td>
</tr>


<tr>
<td class="org-left">Google Slides</td>
<td class="org-left">Wireframing</td>
</tr>
</tbody>
</table>


