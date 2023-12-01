Contribute to MOTBX
===================


Add a resource to MOTBX
-----------------------

The EATRIS Multi-omics Toolbox is built *with* the community, *for* the community.
Suggestions for new resources are very welcome. You can `submit an issue`_
to request addition of a new resource, changes to existing resources, or removal of
a resource. We also welcome new ideas for this repository, or developers who
want to actively contribute to it.

`Contact us`_ if you have any questions.


Information for developers
--------------------------

When making changes to this repository, we follow the `GitHub flow`_. For each issue:
* Create a new branch
* Edit the file(s)
* Create a pull request (PR)
  * automatically triggers validation checks
* Merge PR into `main` branch after review
* Delete the branch after merging PR
* Review issue and mention PR in a comment
* Close issue

Issue templates
~~~~~~~~~~~~~~~

Issue templates can be edited in `.github/ISSUE_TEMPLATE`_.


GitHub actions
~~~~~~~~~~~~~~

Automated GitHub actions are defined in `.github/workflows`_.


Workflow: changing a MOTBX resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each suggested edit to MOTBX resources, a GitHub issue is created.
Changes are made based on the suggestion and a review by the MOTBX development team.
After `resource validation`_ triggered by a pull request, changes can be accepted
and added the resource collection.

.. graphviz::

   digraph add_resource {
        fontname="Helvetica,Arial,sans-serif"
        tooltip="Workflow: changing a MOTBX resource"
        node [
            fontname="Helvetica,Arial,sans-serif",
            shape=box, style="filled"]
        edge [fontname="Helvetica,Arial,sans-serif"]
        issue_creation [
            label=<<b>MOTBX community member:</b><br/>Create issue to request addition,<br/>removal or update of MOTBX resource​>,
            color="#fa9632", tooltip="Create issue", fontcolor="#ffffff",
            URL="https://github.com/EATRIS/motbx/issues/new/choose"];
        first_review [
            label=<<b>MOTBX team:</b><br/>Review request​>,
            color="#1d2850", fontcolor="#ffffff", tooltip="Review issue",
            URL="https://github.com/EATRIS/motbx/issues"];
        approve_request [
            label="Approve request?​",
            color="#d2d2d2", shape="diamond",
            tooltip="Should the resource be added?"];
        request_info [
            label="Request additional information?​",
            color="#d2d2d2", shape="diamond",
            tooltip="Is additional information needed?"];
        comment_issue [
            label=<<b>MOTBX team:</b><br/>Comment on issue to get additional details​>,
            color="#1d2850", fontcolor="#ffffff",
            tooltip="Request further information",
            URL="https://github.com/EATRIS/motbx/issues"];
        provide_info [
            label=<<b>MOTBX community member:</b><br/>Comment on issue to provide further details​>,
            color="#fa9632", tooltip="Provide further information",
            fontcolor="#ffffff", URL="https://github.com/EATRIS/motbx/issues"];
        close_reject_issue [
            label=<<b>MOTBX team:</b><br/>Close issue​>,
            color="#1d2850", fontcolor="#ffffff", tooltip="Close issue",
            URL="https://github.com/EATRIS/motbx/issues"];
        branch_creation [
            label=<<b>MOTBX team:</b><br/>Create a new branch, add assignee>,
            color="#1d2850", fontcolor="#ffffff", tooltip="Create branch",
            URL="https://github.com/EATRIS/motbx/issues"];
        branch_update [
            label=<<b>MOTBX team:</b><br/>Add, remove, or update resource in branch​>,
            color="#1d2850", fontcolor="#ffffff", tooltip="Update branch",
            URL="https://github.com/EATRIS/motbx/branches"];
        pull_request [
            label=<<b>MOTBX team:</b><br/>Create pull request​>,
            color="#1d2850", fontcolor="#ffffff", tooltip="Create pull request",
            URL="https://github.com/EATRIS/motbx/branches"];
        action_validation [
            label=<<b>Triggered automated GitHub action:</b><br/>Perform tests validating resources in repository​>,
            color="#6450a0", fontcolor="#ffffff",
            tooltip="Automated resource validation",
            URL="https://github.com/EATRIS/motbx/actions/workflows/validate_resources.yml"];
        pull_request_review [
            label=<<b>MOTBX team:</b><br/>Review pull request​>,
            color="#1d2850", fontcolor="#ffffff", tooltip="Review pull request",
            URL="https://github.com/EATRIS/motbx/pulls"];
        validation_passed [
            label="Did all automated checks pass?​",
            color="#d2d2d2", shape="diamond",
            tooltip="Could resources be validated?"];
        expectations_met [
            label="Do the implemented changes\nmeet expectations?​",
            color="#d2d2d2", shape="diamond",
            tooltip="Is resource described as expected?"];
        pull_request_merge [
            label=<<b>MOTBX team:</b><br/>Merge pull request and close issue​>,
            color="#1d2850", fontcolor="#ffffff", tooltip="Merge pull request",
            URL="https://github.com/EATRIS/motbx/pulls"];
        pull_request_draft [
            label=<<b>MOTBX team:</b><br/>Convert pull request to draft,<br/>comment on issue to request edit​>,
            color="#1d2850", fontcolor="#ffffff", tooltip="Edits required",
            URL="https://github.com/EATRIS/motbx/pulls"];
        issue_creation -> first_review -> approve_request;
        approve_request -> request_info [label=<<i>Reject</i>>, style="dotted"];
        request_info -> comment_issue [label=<<i>Yes</i>>, style="dotted"];
        comment_issue -> provide_info -> first_review [style="dotted"];
        request_info -> close_reject_issue [label=<<i>No</i>>, style="dotted"];
        approve_request -> branch_creation [label=<<i>Approve</i>>];
        branch_creation -> branch_update -> pull_request -> action_validation;
        action_validation -> pull_request_review -> validation_passed;
        validation_passed -> expectations_met [label=<<i>Yes</i>>];
        expectations_met -> pull_request_merge [label=<<i>Yes</i>>];
        validation_passed -> pull_request_draft [label=<<i>No</i>>, style="dotted"];
        expectations_met -> pull_request_draft [label=<<i>No</i>>, style="dotted"];
        pull_request_draft -> branch_update [style="dotted"];

   }


Workflow: summarise changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

While individual resources can be continuously edited, updates to the MOTBX website
are made in regular time intervals. For this purpose, summaries of all resources
and changes made compared to a previous summary are made.

.. graphviz::

   digraph summarise_resources {
        fontname="Helvetica,Arial,sans-serif"
        tooltip="Workflow: summarise MOTBX resource and changes"
        node [
            fontname="Helvetica,Arial,sans-serif",
            shape=box, style="filled"]
        edge [fontname="Helvetica,Arial,sans-serif"]
        action_summary [
            label=<<b>GitHub action:</b><br/>Create resource summary>,
            fontcolor="#ffffff",
            color="#6450a0", tooltip="Manually triggered GitHub action",
            URL="https://github.com/EATRIS/motbx/actions/workflows/create_summary.yml"];
        send_for_approval [
            label=<<b>MOTBX team:</b><br/>Send change summary to<br/>MOTBX content committee​>,
            color="#1d2850", tooltip="Send summary for approval",
            fontcolor="#ffffff",
            URL="https://github.com/EATRIS/motbx/tree/main/resources/summary"]
        content_review [
            label=<<b>MOTBX content committee:</b><br/>Review changes​>,
            color="#00b4b4", tooltip="Changes are reviwed by content committee",
            URL="https://motbx.eatris.eu/motbx-team/", fontcolor="#ffffff"]
        changes_approved [
            label="Are all changes approved?",
            color="#d2d2d2", shape="diamond",
            tooltip="Does the content committee approve resource changes?"]
        publish_changes [
            label=<<b>MOTBX team:</b><br/>Publish changes on MOTBX website>,
            color="#1d2850", tooltip="Publish changes on MOTBX website",
            URL="https://motbx.eatris.eu/", fontcolor="#ffffff"]
        resolve_issues [
            label=<<b>MOTBX team:</b><br/>Follow the above workflow <i>changing a<br/>MOTBX resource </i> to resolve approval issues>,
            tooltip="Create issue per resource and make edits",
            color="#1d2850", fontcolor="#ffffff",
            URL="https://github.com/EATRIS/motbx/issues"
        ]

        action_summary -> send_for_approval -> content_review -> changes_approved;
        changes_approved -> publish_changes [label=<<i>Yes</i>>];
        changes_approved -> resolve_issues [label=<<i>No</i>>, style="dotted"];
        resolve_issues -> action_summary [style="dotted"];

   }


.. _submit an issue: https://github.com/EATRIS/motbx/issues/new/choose
.. _Contact us: https://motbx.eatris.eu/contact/
.. _GitHub flow: https://docs.github.com/en/get-started/quickstart/github-flow
.. _.github/ISSUE_TEMPLATE: https://github.com/EATRIS/motbx/tree/main/.github/ISSUE_TEMPLATE
.. _.github/workflows: https://github.com/EATRIS/motbx/tree/main/.github/workflows
.. _resource validation: https://github.com/EATRIS/motbx/actions/workflows/validate_resources.yml
