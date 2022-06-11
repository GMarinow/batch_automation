from pprint import pprint
from deadline.api.DeadlineConnect import DeadlineCon  as Connect


class Repository:
    def __init__(self, repository_ip=str, port=int):
        self.repository_ip = repository_ip
        self.port = port

    def GetJobs(self) -> list:
        """
            Return Type: list
            Comment: Returns all jobs in selected repository.
        """
        return Connect(self.repository_ip, self.port).Jobs.GetJobs()

    def GetJobByName(self, job_name) -> list:
        """
            Return Type: list
            Comment: Returns all jobs in selected repository.
        """
        jobs_ = []
        for job in Connect(self.repository_ip, self.port).Jobs.GetJobs():
            if job_name in job['Props']['Name']:
                jobs_.append(job)
        return jobs_



    def GetJobIdIn(self, job_name) -> list:
        """
            Return Type: list -> [ [job_id1, job_name1], [job_id2, job_name2] ... ]
            Comment: Returns list of founded job id and job name
        """
        jobs_id = []
        for job in Connect(self.repository_ip, self.port).Jobs.GetJobs():
            if job_name in job['Props']['Name']:
                jobs_id.append([job['_id'], job['Props']['Name']])
        return jobs_id

    def GetJobIdEqual(self, job_name) -> str:
        """
            Return Type: str -> job_id
            Comment: Returns a job id
        """
        for job in Connect(self.repository_ip, self.port).Jobs.GetJobs():
            if job_name == job['Props']['Name']:
                return job['_id']

    def GetJobDetails(self, job_id=None, job_name=None) -> dict:
        """
            Return Type: dict -> JobDetails
            Comment: Returns a job details.
                    you can search by "job_name" or "job_id",
                    job_id method is a lot quicker
        """
        if job_id:
            return Connect(self.repository_ip, self.port).Jobs.GetJobDetails(job_id)
        else:
            for job in Connect(self.repository_ip, self.port).Jobs.GetJobs():
                if job_name == job['Props']['Name']:
                    return Connect(self.repository_ip, self.port).Jobs.GetJobDetails(job['_id'])


    def SubmitJob(self, info_file, plugin_file, aux = [], idOnly = False):
        return Connect(self.repository_ip, self.port).Jobs.SubmitJob(info_file, plugin_file, aux, idOnly)

    def JobInfoMax(**kwargs):
        """
        Return Type: dict \\
        Comment: Required keys: 
         - Name
         - BatchName
         - OutputDirectory0
        """
        max_job_info_add = kwargs
        max_job_info_deff = {
            "Name": "",
            "BatchName": "",
            "Department": "BATCH AUTOMATION",
            "Blacklist": "",
            "TaskTimeoutSeconds": 12813,
            "FailureDetectionJobErrors": 5,
            "FailureDetectionTaskErrors": 5,
            "EventOptIns": '',
            "Frames": 1,
            "MachineName": 'docker',
            "OverrideJobFailureDetection": 'True',
            "OverrideTaskExtraInfoNames": 'False',
            "OverrideTaskFailureDetection": 'True',
            "Plugin": "3dsmax",
            "Pool": "cutouts",
            "SecondaryPool": "all",
            "Priority": "10",
            "Region": '',
            "UserName": "docker.furniture_village",
            "OutputDirectory0": ""}
        max_job_info = {**max_job_info_deff, **max_job_info_add}
        return max_job_info

    def PluginInfoMax(**kwargs):
        """
        Return Type: dict \\
        Comment: Required keys: 
         - Camera
         - PostLoadScript
         - SceneFile
        """
        max_plugin_info_add = kwargs
        max_plugin_info_deff = {
            'DisableMultipass': 'False',
            'Camera': '',
            'GPUsPerTask': '0',
            'GPUsSelectDevices': '',
            'GammaCorrection': 'False',
            'GammaInput': '1.0',
            'GammaOutput': '1.0',
            'IgnoreMissingDLLs': 'True',
            'IgnoreMissingExternalFiles': 'True',
            'IgnoreMissingUVWs': 'True',
            'IgnoreMissingXREFs': 'True',
            'IsMaxDesign': 'True',
            'Language': 'Default',
            'LocalRendering': 'False',
            'OneCpuPerTask': 'False',
            'QuickFixScript': '',
            'PostLoadScript': '',
            'RemovePadding': 'True',
            'RestartRendererMode': 'True',
            'SceneFile': '',
            'ShowFrameBuffer': 'False',
            'UseSilentMode': 'False',
            'UseSlaveMode': '1',
            'Version': '2020'}
        max_plugin_info = {**max_plugin_info_deff, **max_plugin_info_add}
        return max_plugin_info

    def JobInfoPython(**kwargs):
        """
        Return Type: dict \\
        Comment: keys: 
         - Name
         - BatchName
         - JobDependency0: JobID (if needed)
        """
        python_job_info_add = kwargs
        python_job_info_deff = { 
            'Name': '',
            'Department': 'BATCH AUTOMATION',
            'UserName': 'docker.furniture_village',
            'Frames': '0',
            'Pool': 'fusion',
            'Priority': '10',
            'Blacklist': '',
            'OverrideTaskExtraInfoNames': 'False',
            'BatchName': '',
            'Plugin': 'Python',
            'EventOptIns': '',
            'Region': '',
            'StartJobTimeoutSeconds': '600',
            'TaskTimeoutSeconds': '3671'}
        python_job_info = {**python_job_info_deff, **python_job_info_add}
        return python_job_info

    def PluginInfoPython(**kwargs):
        """
        Return Type: dict \\
        Comment: keys: 
         - ScriptFile
        """
        python_plugin_info_add = kwargs
        python_plugin_info_deff = {
            'Arguments': '',
            'ScriptFile': '',
            'Version': '3.6',
            'SingleFramesOnly': 'False'}
        python_plugin_info = {**python_plugin_info_deff, **python_plugin_info_add}
        return python_plugin_info

    def JobInfo(**kwargs):
        return kwargs

    def PluginInfo(**kwargs):
        return kwargs

