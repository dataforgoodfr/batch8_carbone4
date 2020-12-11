
# Table of Contents

1.  [Dataset](#orgce8a2e3)
    1.  [Variables](#org5f7ac01)
    2.  [Data sources](#org6f1e528)
2.  [Prototyping](#org269602b)
    1.  [Features](#orgb8220a7)
    2.  [Wireframe](#orgcd760d2)
        1.  [Overall structure](#orga0f6960)
        2.  [Structure of a frame](#org2895ee2)
        3.  [key messages](#orga4e6b98)
            -   [Key message 7](#org203eba7)
3.  [Development](#orge955932)
    1.  [Why did we pick Dash?](#org47522cd)
    2.  [Architecture](#orgbb64231)
        1.  [Structure of `app.py`](#org86a3c8e)
            -   [Globals](#orgb4fb8e1)
            -   [Layout](#orgf0d962d)
            -   [Callbacks functions](#org2289d62)
    3.  [Visual identity guidelines](#orge6db36e)
        1.  [Colors](#org477f8be)
            -   [Primary colors](#orgf650136)
            -   [Secondary colors](#orgf22a905)
        2.  [Fonts](#orgac200cb)
            -   [Primary fonts](#org6dfc082)
            -   [Secondary fonts](#orga578a0a)
        3.  [Logo](#org85f75d0)
            -   [Symbol](#org1175291)
            -   [Logotype](#orgb034140)
    4.  [How to contribute](#org8a80be5)
        1.  [Setting up a new Git repository](#orga8dabcd)
        2.  [Adding or modifying owned files (`push`)](#orgd5fdcb5)
        3.  [Update local repo with the new changes in the remote repo](#orgf088ce1)
        4.  [Submit proposed changes to review (`pull-request`)](#orgcd20449)
4.  [Tools that we used](#orge8f2f41)



<a id="orgce8a2e3"></a>

# Dataset


<a id="org5f7ac01"></a>

## Variables


<a id="org6f1e528"></a>

## Data sources


<a id="org269602b"></a>

# Prototyping


<a id="orgb8220a7"></a>

## Features


<a id="orgcd760d2"></a>

## Wireframe


<a id="orga0f6960"></a>

### Overall structure


<a id="org2895ee2"></a>

### Structure of a frame

![img](./Pics/C_2_frame_structure.png "Frame structure")


<a id="orga4e6b98"></a>

### key messages


<a id="org203eba7"></a>

#### Key message 7

![img](./Pics/C_5-1_wireframe_7_sector.png "Key message 7 parameters")


<a id="orge955932"></a>

# Development


<a id="org47522cd"></a>

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


<a id="orgbb64231"></a>

## Architecture


<a id="org86a3c8e"></a>

### Structure of `app.py`


<a id="orgb4fb8e1"></a>

#### Globals


##### Loading libraries, style, and data

-   Libraries

-   Style

-   Pandas DataFrame


##### Data prep


##### Global functions


<a id="orgf0d962d"></a>

#### Layout


<a id="org2289d62"></a>

#### Callbacks functions


<a id="orge6db36e"></a>

## Visual identity guidelines


<a id="org477f8be"></a>

### Colors


<a id="orgf650136"></a>

#### Primary colors


<a id="orgf22a905"></a>

#### Secondary colors


<a id="orgac200cb"></a>

### Fonts


<a id="org6dfc082"></a>

#### Primary fonts


<a id="orga578a0a"></a>

#### Secondary fonts


<a id="org85f75d0"></a>

### Logo


<a id="org1175291"></a>

#### Symbol


<a id="orgb034140"></a>

#### Logotype


<a id="org8a80be5"></a>

## How to contribute


<a id="orga8dabcd"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_carbon4/tree/master/plateforme
-   Ask to join our GitHub


<a id="orgd5fdcb5"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="orgf088ce1"></a>

### Update local repo with the new changes in the remote repo

    $ git pull


<a id="orgcd20449"></a>

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
<td class="org-left">sebastienbourgeois</td>
<td class="org-left">`app.py`</td>
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


<a id="orge8f2f41"></a>

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


