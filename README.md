
# Table of Contents

1.  [Dataset](#orgf8eca52)
    1.  [Variables](#org5062b1f)
    2.  [Data sources](#orgf95e382)
2.  [Prototyping](#org6891baf)
    1.  [Features](#org5ff5a86)
    2.  [Wireframe](#org57f731f)
        1.  [Overall structure](#org4c9ff22)
        2.  [Structure of a frame](#orgb81a5c4)
        3.  [key messages](#org4300e5b)
            -   [Key message 7](#orgcdea107)
3.  [Development](#orgd44270e)
    1.  [Why did we pick Dash?](#org2695aef)
    2.  [Architecture](#orgd3686e5)
        1.  [Structure of `app.py`](#org06424e4)
            -   [Globals](#org41f6074)
            -   [Layout](#org1a6e074)
            -   [Callbacks functions](#org468f06c)
    3.  [Visual identity guidelines](#org1073b30)
        1.  [Colors](#orgc463005)
            -   [Primary colors](#org5e183a5)
            -   [Secondary colors](#org0c2144c)
        2.  [Fonts](#org6f26df8)
            -   [Primary fonts](#org3635c28)
            -   [Secondary fonts](#org329938d)
        3.  [Logo](#org527f346)
            -   [Symbol](#orga20b4b8)
            -   [Logotype](#org1ad348c)
    4.  [How to contribute](#org39d25fe)
        1.  [Setting up a new Git repository](#orgd348fdf)
        2.  [Adding or modifying owned files (`push`)](#orgaeb727a)
        3.  [Submit proposed changes to review (`pull-request`)](#org976d2f6)
4.  [Tools that we used](#orgdb88c71)



<a id="orgf8eca52"></a>

# Dataset


<a id="org5062b1f"></a>

## Variables


<a id="orgf95e382"></a>

## Data sources


<a id="org6891baf"></a>

# Prototyping


<a id="org5ff5a86"></a>

## Features


<a id="org57f731f"></a>

## Wireframe


<a id="org4c9ff22"></a>

### Overall structure


<a id="orgb81a5c4"></a>

### Structure of a frame

![img](./Pics/C_2_frame_structure.png "Frame structure")


<a id="org4300e5b"></a>

### key messages


<a id="orgcdea107"></a>

#### Key message 7

![img](./Pics/C_5-1_wireframe_7_sector.png "Key message 7 parameters")


<a id="orgd44270e"></a>

# Development


<a id="org2695aef"></a>

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


<a id="orgd3686e5"></a>

## Architecture


<a id="org06424e4"></a>

### Structure of `app.py`


<a id="org41f6074"></a>

#### Globals


##### Loading libraries, style, and data

-   Libraries

-   Style

-   Pandas DataFrame


##### Data prep


##### Global functions


<a id="org1a6e074"></a>

#### Layout


<a id="org468f06c"></a>

#### Callbacks functions


<a id="org1073b30"></a>

## Visual identity guidelines


<a id="orgc463005"></a>

### Colors


<a id="org5e183a5"></a>

#### Primary colors


<a id="org0c2144c"></a>

#### Secondary colors


<a id="org6f26df8"></a>

### Fonts


<a id="org3635c28"></a>

#### Primary fonts


<a id="org329938d"></a>

#### Secondary fonts


<a id="org527f346"></a>

### Logo


<a id="orga20b4b8"></a>

#### Symbol


<a id="org1ad348c"></a>

#### Logotype


<a id="org39d25fe"></a>

## How to contribute


<a id="orgd348fdf"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_carbon4/tree/master/plateforme
-   Ask to join our GitHub


<a id="orgaeb727a"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="org976d2f6"></a>

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
<td class="org-left">??</td>
</tr>


<tr>
<td class="org-left">j-back</td>
<td class="org-left">??</td>
</tr>


<tr>
<td class="org-left">morgandavidson</td>
<td class="org-left">`README.md`</td>
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


<a id="orgdb88c71"></a>

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


