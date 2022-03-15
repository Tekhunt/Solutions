from django.db import models
from .user_model import User
# from .checklist_model import CheckList
from .cleaning_area_model import CleaningArea
    
class Task(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("InProgress", "InProgress"),
        ("Completed", "Completed"),
        ("Assigned", "Assigned"),
        ("Accepted", "Accepted"), 
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    location =models.CharField(max_length=150)
    created_by = models.ForeignKey(User, limit_choices_to={'is_admin': True, 'is_manager': True}, related_name='creator', 
                                    on_delete=models.DO_NOTHING, verbose_name='created-by')
    assigned_to = models.ManyToManyField(User, limit_choices_to={'is_cleaner': True, 'is_bin_collector': True}, 
                                         related_name='assignee', verbose_name='assigned-to', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created-at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated-at')
    start_date = models.DateTimeField(null=True, verbose_name='task-start-date')
    end_date = models.DateTimeField(blank=True, null=True, verbose_name='task-end-Date')
    task_status = models.CharField(max_length=30, choices=STATUS, default='Pending', verbose_name='task-status')
    cleaning_area = models.ManyToManyField(CleaningArea, related_name='cleaning_area', verbose_name='cleaning-area', blank=True)
    
    
    def __str__(self):
        return self.title

    def done(self):
        return self.task_status == 'Completed'
