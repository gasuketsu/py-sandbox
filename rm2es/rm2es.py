import json
from elasticsearch import Elasticsearch
from redminelib import Redmine


def add_to_es(tickets):
    for v in tickets:
        v_json = json.dumps(v)
        es = Elasticsearch()
        es.index(index='first_index', doc_type='doc', body=v_json, id=v['id'])


def populate_issue_data(identifier):
    tickets = []
    redmine = Redmine(
        'http://example.redmine.com/', key='your-redmine-api-key')
    issues = redmine.issue.filter(project_id=identifier, status_id='*')

    for issue in issues:
        ticket = {}
        if hasattr(issue, 'category'):
            ticket['category'] = issue.category.name
        ticket['id'] = issue.id
        ticket['status'] = issue.status.name
        ticket['subject'] = issue.subject
        ticket['tracker'] = issue.tracker.name
        ticket['priority'] = issue.priority.name
        if hasattr(issue, 'assigned_to'):
            ticket['assigned_to'] = issue.assigned_to.name
        ticket['project'] = issue.project.name
        cd = str(issue.created_on)
        cd = cd.replace(' ', 'T')
        ticket['created_on'] = cd
        if issue.custom_fields.get(22).value != '':
            ticket['cause'] = issue.custom_fields.get(22).value
        if issue.custom_fields.get(23).value != '':
            ticket['factor'] = issue.custom_fields.get(23).value
        if issue.custom_fields.get(9) is not None and issue.custom_fields.get(
                9).value != '':
            ticket['reproducibility'] = issue.custom_fields.get(9).value
        tickets.append(ticket)
    return tickets


projects = ['rm-project-1', 'rm-project-2']
for p in projects:
    data_list = populate_issue_data(p)
    add_to_es(data_list)
