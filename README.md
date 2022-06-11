# Batch Automation
![Image](https://img.shields.io/pypi/v/batch_automation.svg) [![Downloads](https://img.shields.io/pypi/dm/batch_automation)](https://pypistats.org/packages/batch_automation)

<!-- [![Stable Version](https://img.shields.io/batch_automation/v/batch_automation?color=blue)](https://pypi.org/project/batch_automation/) -->

Batch Automation is a Python library with a variety of functions and APIs for dealing with 3d and non-3d related stuff.

A few examples:
* AWS Thinkbox Deadline API
* Blackmagic API
* Google Services API
* MongoDB API
* Custom Tools

*more functions will be added overtime*

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Batch Automation.

```bash
pip install batch_automation
```

## Usage

*AWS Thinkbox Deadline API*

```python
from batch_automation.deadline.custom.custom import *

# Returns all jobs in selected repository.
print (Repository('WebServiceName', Port).GetJobs())

# Returns all jobs in selected repository.
print (Repository('WebServiceName', Port).GetJobByName('Job-Name'))

# Returns a job details.
# you can search by "job_name" or "job_id", job_id method is a lot quicker
print (Repository('WebServiceName', Port).GetJobDetails('Job-Name'))

# Create the info_file and plugin_file and submit them to deadline
info_file = Repository().JobInfo(Name='Job-Name', 
                                UserName='UserName', 
                                Frames='1', 
                                Plugin='VraySpawner')
plugin_file = Repository().PluginInfo(Version='Max2023')
print(Repository('WebServiceName', Port).SubmitJob(info_file, plugin_file))

```
*All standard api calls are included as well*

```python
from batch_automation.deadline.api.DeadlineConnect import DeadlineCon as Connect

repo = Connect('WebServiceName', Port)

#The list of Group names.
print (repo.Groups.GetGroupNames())

# The list of Jobs
print (repo.Jobs.GetJobs())
```
*Blackmagic API Full list of funcions* [Link](https://deric.github.io/DaVinciResolve-API-Docs/)

```python
from batch_automation.davinci.MediaPool import MediaPool
from batch_automation.davinci.ProjectManager import ProjectManager

# Returns currently selected Folder
print (MediaPool.GetCurrentFolder())

# Adds new timeline with given name
print (MediaPool.CreateEmptyTimeline('New-Timeline'))

# Imports specified file/folder paths into current Media Pool folder.
# Input is an array of file/folder paths. Returns a list of the MediaPoolItems created.
print (MediaPool.ImportMedia(['/mdeia/clip.mov']))

# Creates and returns a project if projectName (string) is unique, and None if it is not.
print(ProjectManager.CreateProject('New-Project'))

# Returns a list of dictionary items (with keys 'DbType', 'DbName' and optional 'IpAddress')
# corresponding to all the databases added to Resolve
print(ProjectManager.GetDatabaseList())

# Loads and returns the project
print(ProjectManager.LoadProject('Project-Name'))
...
```
*Google API*

```python
from batch_automation.google.api import create_service

# Creates an Google Service
print (create_service('https://www.googleapis.com/auth/spreadsheets', 'sheets', 'v4', '/cred/OAuth.json'))

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0)