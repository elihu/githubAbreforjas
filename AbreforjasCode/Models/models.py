from django.db import models
from django.contrib.auth.models import User
from djcelery.models import PeriodicTask, IntervalSchedule
from datetime import datetime


class TaskScheduler(models.Model):
    
    periodic_task = models.ForeignKey(PeriodicTask)

    @staticmethod
    def schedule_every(task_name, period, every, args=None, kwargs=None):
		""" schedules a task by name every "every" "period". So an example call would be: TaskScheduler('mycustomtask', 'seconds', 30, [1,2,3]) that would schedule your custom task to run every 30 seconds with the arguments 1,2 and 3 passed to the actual task. """
		permissible_periods = ['days', 'hours', 'minutes', 'seconds']
		if period not in permissible_periods:
			raise Exception('Invalid period specified')
        # create the periodic task and the interval
		ptask_name = "%s_%s" % (task_name, datetime.now()) # create some name for the period task
		interval_schedules = IntervalSchedule.objects.filter(period=period, every=every)
		if interval_schedules: # just check if interval schedules exist like that already and reuse em
			interval_schedule = interval_schedules[0]
		else: # create a brand new interval schedule
			interval_schedule = IntervalSchedule()
			interval_schedule.every = every # should check to make sure this is a positive int
			interval_schedule.period = period 
			interval_schedule.save()
		ptask = PeriodicTask(name=ptask_name, task=task_name, interval=interval_schedule)
		if args:
			ptask.args = args
		if kwargs:
			ptask.kwargs = kwargs
		ptask.save()
		return TaskScheduler.objects.create(periodic_task=ptask)

    def stop(self):
        """ pauses the task """
        ptask = self.periodic_task
        ptask.enabled = False
        ptask.save()

    def start(self):
        ptask = self.periodic_task
        ptask.enabled = True
        ptask.save()

    def terminate(self):
        self.stop()
        ptask = self.periodic_task
        self.delete()
        ptask.delete()

class ProjectUsers(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    user = models.CharField(max_length=128L)
    rol = models.CharField(max_length=128L, blank=True, null=True)
    roles_code = models.ForeignKey('Roles', db_column='roles_code', blank=True, null=True)
    def __str__():
		return self.user
    class Meta:
        db_table = 'project_users'
        ordering = ["user"]

class Forges(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    def __str__(self):
		return self.code
    class Meta:
        db_table = 'forges'

class Datasets(models.Model):
    name = models.CharField(max_length=128)
    forge = models.ForeignKey(Forges)
    url = models.URLField()
    user = models.ForeignKey(User, blank=True)
    update_date = models.DateTimeField(auto_now=True)
    access_key = models.CharField(max_length=128, blank=True, null=True)
    schedule = models.ForeignKey(TaskScheduler, blank=True, null=True)
    description = models.TextField()
    class Meta:
        db_table = 'datasets'
        ordering = ["name"]
        
    def __str__(self):
		return self.name

class Users(models.Model):
    external_id = models.CharField(max_length=128L)
    #forge = models.CharField(max_length=128L, blank=True)
    dataset = models.ForeignKey(Datasets)
    username = models.CharField(max_length=128L, blank=True)
    name = models.CharField(max_length=128L, blank=True)
    email = models.CharField(max_length=128L, blank=True, null=True)
    created = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'users'
        ordering = ["username"]
		
class Projects(models.Model):
    #id = models.IntegerField(primary_key=True)
    external_id = models.CharField(max_length=128L, null=True, blank=True)
    name = models.CharField(max_length=128L, blank=True)
    dataset = models.ForeignKey(Datasets)
    homepage = models.URLField(blank=True, null=True)
    sfpercentile = models.DecimalField(null=True, max_digits=23, decimal_places=0, blank=True)
    sfdonation = models.CharField(max_length=128L, blank=True, null=True)
    status = models.IntegerField(null=True, blank=True)
    created = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=2000L, blank=True, null=True)
    sftotalnews = models.IntegerField(null=True, blank=True)
    sftotalposts = models.IntegerField(null=True, blank=True)
    totaltickets = models.IntegerField(null=True, blank=True)
    opentickets = models.IntegerField(null=True, blank=True)
    gcstars = models.IntegerField(null=True, blank=True)
    gcactivity = models.CharField(max_length=16L, blank=True, null=True)
    ghwatchers = models.IntegerField(null=True, blank=True)
    repoforks = models.IntegerField(null=True, blank=True)
    repotype = models.ForeignKey('RepositoryTypes', null=True, db_column='repotype', blank=True)
    repoaccess = models.CharField(max_length=512L, blank=True, null=True)
    repobrowse = models.CharField(max_length=512L, blank=True, null=True)
    totalreporeads = models.IntegerField(null=True, blank=True)
    totalrepowrites = models.IntegerField(null=True, blank=True)
    sfranking = models.IntegerField(null=True, blank=True)
    downloaddate = models.DateTimeField(null=True, blank=True)
    processdate = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=256L, blank=True, null=True)
    
    def __str__(self):
		return self.name
    
    class Meta:
        db_table = 'projects'
        ordering = ["name"]

class Audiences(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'audiences'

class Categories(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'categories'

class Databases(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'databases'

class DownloadTypes(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'download_types'

class Downloads(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    uri = models.CharField(max_length=128L)
    type = models.CharField(max_length=128L, blank=True)
    publication = models.DateTimeField(null=True, blank=True)
    filesize = models.IntegerField(null=True, blank=True)
    information = models.CharField(max_length=128L, null=True, blank=True)
    downloadcount = models.IntegerField(null=True, db_column='downloadCount', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'downloads'

class ForgeApis(models.Model):
    forge = models.ForeignKey('Forges', db_column='forge')
    request_uri = models.CharField(max_length=128L)
    request_accept_header = models.CharField(max_length=128L, blank=True)
    type = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'forge_apis'

class Languages(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    sonar_code = models.CharField(max_length=128L)
    class Meta:
        db_table = 'languages'

class Licenses(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'licenses'

class Metrics(models.Model):
	name = models.CharField(max_length=128L, blank=True)
	description = models.CharField(max_length=128L, blank=True)
	
	def __str__():
		return self.name + ': ' + self.description
	
	class Meta:
		ordering = ["name"]
		db_table = 'metrics'

class MetricResults(models.Model):
	project = models.ForeignKey(Projects)
	metric = models.ForeignKey(Metrics)
	value = models.FloatField()
	
	def __str__():
		return self.project + ' - ' + self.metric + ': ' + self.value
	class Meta:
		db_table = 'metrics_projects'

class MetricUserResult(models.Model):
	user = models.ForeignKey(Users)
	project = models.ForeignKey(Projects)
	metric = models.ForeignKey(Metrics)
	value = models.FloatField()
	def __str__():
		return self.project + ' - ' + self.user + '-' + self.metric + ': ' + self.value
	class Meta:
		db_table = 'metrics_users'

class Milestones(models.Model):
    #id = models.IntegerField(primary_key=True)
    externalID = models.CharField(max_length=128L, db_column='externalID') # Field name made lowercase.
    title = models.CharField(max_length=128L, blank=True)
    due_on = models.DateField(null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    totaltickets = models.IntegerField(null=True, blank=True)
    opentickets = models.IntegerField(null=True, blank=True)
    completed_date = models.DateField(null=True, db_column='completed-date', blank=True) # Field renamed to remove unsuitable characters.
    user = models.ForeignKey('Users', null=True, blank=True)
    project = models.ForeignKey('Projects', null=True, db_column='project', blank=True)
    description = models.TextField(null=True, blank=True)
    descartado = models.TextField(null=True, blank=True)
    def __str__():
		return self.externalID + ': '  + self.project
    class Meta:
        db_table = 'milestones'
        ordering = ["externalID"]

class OperatingSystems(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'operating_systems'

class ProgrammingLanguages(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    cod_sf = models.ForeignKey('SfTrove', db_column='cod_sf')
    class Meta:
        db_table = 'programming_languages'

class ProjectAudiences(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    audience = models.ForeignKey(Audiences, db_column='audience')
    class Meta:
        db_table = 'project_audiences'

class ProjectDatabases(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    database = models.ForeignKey(Databases, db_column='database')
    class Meta:
        db_table = 'project_databases'

class ProjectLanguages(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    language = models.ForeignKey(Languages, db_column='language')
    class Meta:
        db_table = 'project_languages'

class ProjectLicenses(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    license = models.ForeignKey(Licenses, db_column='license')
    class Meta:
        db_table = 'project_licenses'

class ProjectOs(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    os = models.ForeignKey(OperatingSystems, db_column='os')
    class Meta:
        db_table = 'project_os'

class ProjectPl(models.Model):
    projects = models.ForeignKey('Projects')
    pl = models.ForeignKey(ProgrammingLanguages, db_column='pl')
    class Meta:
        db_table = 'project_pl'

class ProjectTopics(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    topic = models.ForeignKey('Topics', db_column='topic')
    class Meta:
        db_table = 'project_topics'

class ProjectUi(models.Model):
    project = models.ForeignKey('Projects', db_column='project')
    ui = models.ForeignKey('UserInterfaces', db_column='ui')
    class Meta:
        db_table = 'project_ui'

class RepositoryTypes(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'repository_types'

class Roles(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'roles'

class SfTrove(models.Model):
    uri = models.CharField(max_length=70L, primary_key=True)
    tabla = models.CharField(max_length=20L, blank=True)
    cod = models.CharField(max_length=128L)
    campo = models.CharField(max_length=20L, blank=True)
    class Meta:
        db_table = 'sf_trove'

class TicketCategories(models.Model):
    ticket = models.ForeignKey('Tickets', db_column='ticket')
    category = models.ForeignKey(Categories, db_column='category')
    class Meta:
        db_table = 'ticket_categories'

class TicketPriorities(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'ticket_priorities'

class TicketStatus(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'ticket_status'

class TicketTypes(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'ticket_types'

class Tickets(models.Model):
    #id = models.IntegerField(primary_key=True)
    project = models.ForeignKey(Projects, db_column='project')
    externalID = models.CharField(max_length=128L, db_column='externalID', blank=True) # Field name made lowercase.
    created = models.DateField(null=True, blank=True)
    updated = models.DateField(null=True, blank=True)
    completed = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=256L, blank=True)
    description = models.TextField(blank=True, null=True)
    totalcomments = models.IntegerField(null=True, db_column='totalComments', blank=True) # Field name made lowercase.
    status = models.ForeignKey(TicketStatus, null=True, db_column='status', blank=True)
    priority = models.ForeignKey(TicketPriorities, null=True, db_column='priority', blank=True)
    type = models.ForeignKey(TicketTypes, null=True, db_column='type', blank=True)
    author = models.ForeignKey('Users', related_name='author')
    owner = models.ForeignKey('Users', related_name='owner', blank=True, null=True)
    milestone = models.ForeignKey(Milestones, blank=True, null=True)
    votes = models.IntegerField(null=True, blank=True)
    def __str__():
		return self.externalID + ': '  + self.project
    class Meta:
        db_table = 'tickets'
        ordering = ["externalID"]

class Topics(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'topics'

class UserInterfaces(models.Model):
    code = models.CharField(max_length=128L, primary_key=True)
    description = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'user_interfaces'
