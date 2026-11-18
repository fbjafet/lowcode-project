## Business problem
Requests from internal teams that are sent directly to team members email addresses that can get lost or be unattended. All the requests should be directed to a shared email inbox and an excel file or SharePoint should be created to gather all the requests. Instead of using an email, the requests should be sent via an Form
 
## Trigger
The start event is a form filed requesting a job to be done. It's a webhook via Make.
 
## Steps
1. Form response arrives and is stored in a Excel/SharePoint
2. An email is sent to a shared email address to notify a new task
3. Task is assigned to the right team member but all team has access to it
 
## Failure questions
- What if it fires twice?
Tasks will be duplicated and/or the same task could be dealt by two different team members

- What if a step fails halfway?
Tasks will be unattended causing SLA and CX problems

- What data crosses a third party, and is any of it personal?
No sensitive data are involved on this task, only email addresses, and names. 
