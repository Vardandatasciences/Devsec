from django.db import models
from django.contrib.auth.models import User
 
# Users model (Django built-in User model is used)
class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=255)
    # MobileNo = models.CharField(max_length=15)
    # Email = models.CharField(max_length=255)
    # Department = models.CharField(max_length=255)
    # Designation = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    CreatedAt = models.DateTimeField()
    UpdatedAt = models.DateTimeField()
    # role = models.CharField(max_length=45)
    # branch = models.CharField(max_length=45)
 
    class Meta:
        db_table = 'users'
 
# Framework model
class Framework(models.Model):
    FrameworkId = models.AutoField(primary_key=True)
    FrameworkName = models.CharField(max_length=255)
    CurrentVersion = models.FloatField()
    FrameworkDescription = models.TextField()
    EffectiveDate = models.DateField()
    CreatedByName = models.CharField(max_length=255)
    CreatedByDate = models.DateField()
    Category = models.CharField(max_length=50)
    DocURL = models.CharField(max_length=255)
    Identifier = models.CharField(max_length=45)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Status = models.CharField(max_length=45, null=True, blank=True)
    ActiveInactive = models.CharField(max_length=45)
 
    class Meta:
        db_table = 'frameworks'
 
# Policy model
class Policy(models.Model):
    PolicyId = models.AutoField(primary_key=True)
    FrameworkId = models.ForeignKey(
        'Framework',
        on_delete=models.CASCADE,
        db_column='FrameworkId'
    )
    CurrentVersion = models.CharField(max_length=50, null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)
    PolicyDescription = models.TextField(null=True, blank=True)
    PolicyName = models.CharField(max_length=255)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    Department = models.CharField(max_length=255, null=True, blank=True)
    CreatedByName = models.CharField(max_length=255, null=True, blank=True)
    CreatedByDate = models.DateField(null=True, blank=True)
    Applicability = models.CharField(max_length=255, null=True, blank=True)
    DocURL = models.CharField(max_length=255, null=True, blank=True)
    Scope = models.TextField(null=True, blank=True)
    Objective = models.TextField(null=True, blank=True)
    Identifier = models.CharField(max_length=45, null=True, blank=True)
    PermanentTemporary = models.CharField(max_length=45, null=True, blank=True)
    ActiveInactive = models.CharField(max_length=45, null=True, blank=True)
 
    class Meta:
        db_table = 'policies'
 
# SubPolicy model
class SubPolicy(models.Model):
    SubPolicyId = models.AutoField(primary_key=True)
    PolicyId = models.ForeignKey('Policy', on_delete=models.CASCADE, db_column='PolicyId')
    SubPolicyName = models.CharField(max_length=255)
    CreatedByName = models.CharField(max_length=255)
    CreatedByDate = models.DateField()
    Identifier = models.CharField(max_length=45)
    Description = models.TextField()
    Status = models.CharField(max_length=50, null=True, blank=True)
    PermanentTemporary = models.CharField(max_length=50, null=True, blank=True)
    Control = models.TextField(null=True, blank=True)
 
    class Meta:
        db_table = 'subpolicies'
    
 
# Compliance model
class Compliance(models.Model):
    ComplianceId = models.AutoField(primary_key=True)
    SubPolicyId = models.ForeignKey('SubPolicy', on_delete=models.CASCADE, db_column='SubPolicyId')
    Identifier = models.CharField(max_length=50, null=True, blank=True)
    ComplianceItemDescription = models.TextField()
    mitigation = models.TextField(null=True, blank=True)
    IsRisk = models.BooleanField()
    PossibleDamage = models.TextField()
    Criticality = models.CharField(max_length=50)
    MandatoryOptional = models.CharField(max_length=50)
    ManualAutomatic = models.CharField(max_length=50)
    Impact = models.CharField(max_length=50)
    Probability = models.CharField(max_length=50)
    ActiveInactive = models.CharField(max_length=45, null=True, blank=True)
    PermanentTemporary = models.CharField(max_length=45)
    CreatedByName = models.CharField(max_length=250)
    CreatedByDate = models.DateField()
    ComplianceVersion = models.CharField(max_length=50)
    Status = models.CharField(max_length=50, null=True, blank=True)
 
    class Meta:
        db_table = 'compliance'
        # Since Django does not support composite primary keys, you can add a unique constraint to enforce uniqueness:
        unique_together = (('SubPolicyId', 'ComplianceVersion'),)
 
    def __str__(self):
        return f"Compliance {self.ComplianceId} - Version {self.ComplianceVersion}"
 
# Audit model
class Audit(models.Model):
    AuditId = models.AutoField(primary_key=True)
    Assignee = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='assignee', db_column='assignee')
    Auditor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='auditor', db_column='auditor')
    Reviewer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='reviewer', null=True, db_column='reviewer')
    FrameworkId = models.ForeignKey('Framework', on_delete=models.CASCADE, db_column='FrameworkId')
    PolicyId = models.ForeignKey('Policy', on_delete=models.CASCADE, db_column='PolicyId', null=True)
    SubPolicyId = models.ForeignKey('SubPolicy', on_delete=models.CASCADE, db_column='SubPolicyId', null=True)
    DueDate = models.DateField()
    Frequency = models.IntegerField(null=True)
    Status = models.CharField(max_length=45)
    CompletionDate = models.DateTimeField(null=True)
    ReviewerComments = models.CharField(max_length=255, null=True)
    AuditType = models.CharField(max_length=1)
 
    class Meta:
        db_table = 'audit'
 
# AuditFinding model
class AuditFinding(models.Model):
    AuditFindingsId = models.AutoField(primary_key=True)
    AuditId = models.ForeignKey(Audit, on_delete=models.CASCADE, db_column='AuditId')
    ComplianceId = models.ForeignKey(Compliance, on_delete=models.CASCADE, db_column='ComplianceId')
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='UserId')
    Evidence = models.TextField()
    Check = models.CharField(max_length=1, choices=[('0', 'Not Compliance'), ('1', 'Compliance'), ('2', 'Partially Compliance'), ('3', 'Not Applicable')], default='0')
    HowToVerify = models.TextField(null=True, blank=True)
    Impact = models.TextField(null=True, blank=True)
    Recommendation = models.TextField(null=True, blank=True)
    DetailsOfFinding = models.TextField(null=True, blank=True)
    Comments = models.TextField(null=True, blank=True)
    CheckedDate = models.DateTimeField(null=True, blank=True)
    AssignedDate = models.DateTimeField()
 
    class Meta:
        db_table = 'audit_findings'
 
# Incident model
class Incident(models.Model):
    IncidentId = models.AutoField(primary_key=True)
    IncidentTitle = models.CharField(max_length=255)
    Description = models.TextField()
    Mitigation = models.TextField(null=True, blank=True)
    AuditId = models.ForeignKey(Audit, on_delete=models.CASCADE, null=True, blank=True, db_column='AuditId')
    ComplianceId = models.ForeignKey(Compliance, on_delete=models.CASCADE, null=True, blank=True, db_column='ComplianceId')
    Date = models.DateField()
    Time = models.TimeField()
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, db_column='UserId')
    Origin = models.CharField(max_length=50)
    Comments = models.TextField(null=True, blank=True)
    RiskCategory = models.CharField(max_length=100, null=True, blank=True)
    RiskPriority = models.CharField(max_length=20, null=True, blank=True)
    Attachments = models.TextField(null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=45, null=True, blank=True)
    IdentifiedAt = models.DateTimeField(null=True, blank=True)
 
    class Meta:
        db_table = 'incidents'
 
# Risk model
class Risk(models.Model):
    RiskId = models.AutoField(primary_key=True)
    ComplianceId = models.ForeignKey(Compliance, on_delete=models.CASCADE)
    RiskCategory = models.CharField(max_length=100)
    RiskDescription = models.TextField()
    RiskLikelihood = models.FloatField()
    RiskImpact = models.FloatField()
    RiskExposureRating = models.FloatField()
    RiskPriority = models.CharField(max_length=100)
    RiskMitigation = models.TextField()
 
    class Meta:
        db_table = 'risk'
 
# RiskInstance model
class RiskInstance(models.Model):
    RiskInstanceId = models.AutoField(primary_key=True)
    RiskId = models.ForeignKey(Risk, on_delete=models.CASCADE)
    Criticality = models.IntegerField()
    PossibleDamage = models.TextField()
    Category = models.CharField(max_length=45)
    Appetite = models.TextField()
    RiskDescription = models.TextField()
    RiskLikelihood = models.FloatField()
    RiskImpact = models.FloatField()
    RiskExposureRating = models.FloatField()
    RiskPriority = models.CharField(max_length=100)
    RiskResponseType = models.CharField(max_length=100)
    RiskResponseDescription = models.TextField()
    RiskOwner = models.CharField(max_length=45)
    RiskStatus = models.CharField(max_length=45)
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE)
    Date = models.DateTimeField()
 
    class Meta:
        db_table = 'risk_instance'
 
# Workflow model
class Workflow(models.Model):
    Id = models.AutoField(primary_key=True)
    FindingId = models.ForeignKey(AuditFinding, on_delete=models.CASCADE, db_column='finding_id')
    IncidentId = models.ForeignKey(Incident, on_delete=models.CASCADE, db_column='IncidentId')
    AssigneeId = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='assignee_id', related_name='workflow_assignee')
    ReviewerId = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='reviewer_id', related_name='workflow_reviewer')
    AssignedAt = models.DateTimeField()
 
    class Meta:
        db_table = 'workflow'
 
class PolicyVersion(models.Model):
    VersionId = models.AutoField(primary_key=True)
    PolicyId = models.ForeignKey('Policy', on_delete=models.CASCADE, db_column='PolicyId')
    Version = models.CharField(max_length=20)
    PolicyName = models.CharField(max_length=255)
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateField()
    PreviousVersionId = models.IntegerField(null=True, blank=True)
 
    class Meta:
        db_table = 'policyversions'
 
class PolicyApproval(models.Model):
    ApprovalId = models.AutoField(primary_key=True)
    Identifier = models.CharField(max_length=45)
    ExtractedData = models.JSONField(null=True, blank=True)
    UserId = models.IntegerField()  # Can also be models.ForeignKey(User, on_delete=models.CASCADE) if mapped to user table
    ReviewerId = models.IntegerField()  # Similarly, replace with ForeignKey if needed
    Version = models.CharField(max_length=50, null=True, blank=True)
    ApprovedNot = models.BooleanField(null=True)

    def __str__(self):
        return f"PolicyApproval {self.Identifier} (Version {self.Version})"

    class Meta:
        db_table = 'policyapproval'