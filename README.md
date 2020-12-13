
# Table of Contents

1.  [Dataset](#org5b4eeff)
    1.  [Variables](#orgb00cbbb)
    2.  [Data sources](#orge67b48f)
2.  [Prototyping](#orgeca9bba)
    1.  [Features](#org1711ac0)
    2.  [Wireframe](#orgff557e4)
        1.  [Overall structure](#orgdfd1967)
        2.  [Structure of a frame](#org0b73ab6)
        3.  [key messages](#org520b1c5)
            -   [Key message 7](#orge49f99f)
3.  [Development](#org2287987)
    1.  [Why did we pick Dash?](#org4d2aac4)
    2.  [Architecture](#org0760ccc)
        1.  [Structure of `app.py`](#org122298f)
            -   [Globals](#orgb0829ed)
            -   [Layout](#org3e2c870)
            -   [Callbacks functions](#org72538f2)
    3.  [Visual identity guidelines](#orgebca557)
        1.  [Colors](#org62e5a91)
            -   [Primary colors](#org1a32c20)
            -   [Secondary colors](#org619ba8b)
        2.  [Fonts](#org475c61c)
            -   [Primary fonts](#org4d423cd)
            -   [Secondary fonts](#org7b2eb32)
        3.  [Logo](#org3d1f009)
            -   [Symbol](#orgcb6b4db)
            -   [Logotype](#org9e0e7a5)
    4.  [How to contribute](#org8b96f2a)
        1.  [Setting up a new Git repository](#org3bb1299)
        2.  [Adding or modifying owned files (`push`)](#orgc6f2975)
        3.  [Update local repo with the new changes in the remote repo](#orgfb7db15)
        4.  [Submit proposed changes to review (`pull-request`)](#orgd8dccc4)
4.  [Tools that we used](#org6b93b62)



<a id="org5b4eeff"></a>

# Dataset


<a id="orgb00cbbb"></a>

## Variables


<a id="orge67b48f"></a>

## Data sources


<a id="orgeca9bba"></a>

# Prototyping


<a id="org1711ac0"></a>

## Features


<a id="orgff557e4"></a>

## Wireframe


<a id="orgdfd1967"></a>

### Overall structure


<a id="org0b73ab6"></a>

### Structure of a frame

![img](./Pics/C_2_frame_structure.png "Frame structure")


<a id="org520b1c5"></a>

### key messages


<a id="orge49f99f"></a>

#### Key message 7

![img](./Pics/C_5-1_wireframe_7_sector.png "Key message 7 parameters")


<a id="org2287987"></a>

# Development


<a id="org4d2aac4"></a>

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


<a id="org0760ccc"></a>

## Architecture


<a id="org122298f"></a>

### Structure of `app.py`


<a id="orgb0829ed"></a>

#### Globals


##### Loading libraries, style, and data

-   Libraries

-   Style

-   Pandas DataFrame


##### Data prep


##### Global functions


<a id="org3e2c870"></a>

#### Layout


<a id="org72538f2"></a>

#### Callbacks functions


<a id="orgebca557"></a>

## Visual identity guidelines


<a id="org62e5a91"></a>

### Colors


<a id="org1a32c20"></a>

#### Primary colors


<a id="org619ba8b"></a>

#### Secondary colors


<a id="org475c61c"></a>

### Fonts


<a id="org4d423cd"></a>

#### Primary fonts


<a id="org7b2eb32"></a>

#### Secondary fonts


<a id="org3d1f009"></a>

### Logo


<a id="orgcb6b4db"></a>

#### Symbol


<a id="org9e0e7a5"></a>

#### Logotype


<a id="org8b96f2a"></a>

## How to contribute


<a id="org3bb1299"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_carbon4/tree/master/plateforme
-   Ask to join our GitHub


<a id="orgc6f2975"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="orgfb7db15"></a>

### Update local repo with the new changes in the remote repo

    $ git pull


<a id="orgd8dccc4"></a>

### Submit proposed changes to review (`pull-request`)

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
<td class="org-left">`./data/*`</td>
</tr>


<tr>
<td class="org-left">morgandavidson</td>
<td class="org-left">`README.md`</td>
</tr>


<tr>
<td class="org-left">sebastienbourgeois</td>
<td class="org-left">`app.py`</td>
</tr>
</tbody>
</table>

To submit changes reviewees have to do : 

    $ git branch new-branch        #Creates a new branch nammed "new-branch"
    $ git checkout new-branch      #Switch to "new-branch"
    # alternatively these two commands can be condensed to "git checkout -b new-branch"
    $ git add filename
    $ git commit
    $ git push origin new-branch
    $ git checkout master          #Switch back to master

Then go on our [GitHub](https://github.com/dataforgoodfr/batch8_worldbank), and simply click on `compare & pull request` and pick a reviewer. Or do

-   cilck on `Pull requests`,
-   then on `New Pull Request`,
-   click on `compare across forks`,
-   select : `dataforgoodfr/batch8_carbon4 | =base: master` <- `revieweename/batch8_carbon4` | `new-branch`,
-   click on `create pull request`
-   enter GitHub reviewer name in `reviewers`, add title and comment,
-   click on `create pull request`


<a id="org6b93b62"></a>

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

