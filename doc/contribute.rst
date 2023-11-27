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


Workflow: changing a MOTBX resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. graphviz::

   digraph add_resource {
        fontname="Helvetica,Arial,sans-serif"
        node [
            fontname="Helvetica,Arial,sans-serif", fontsize=16,
            shape=box, style="filled"]
        edge [fontname="Helvetica,Arial,sans-serif"]
        issue_creation [
            label=<<b>MOTBX community member:</b><br/>Create issue to request addition,<br/>removal or update of MOTBX resource​>,
            color="#fa9632", tooltip="Create issue",
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
            URL="https://github.com/EATRIS/motbx/issues"];
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
            URL="https://github.com/EATRIS/motbx/actions"];
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
        approve_request -> request_info [label="Reject"];
        request_info -> comment_issue [label="Yes"];
        comment_issue -> provide_info -> first_review;
        request_info -> close_reject_issue [label="No"];
        approve_request -> branch_creation [label="Approve"];
        branch_creation -> branch_update -> pull_request -> action_validation;
        action_validation -> pull_request_review -> validation_passed;
        validation_passed -> expectations_met [label="Yes"];
        expectations_met -> pull_request_merge [label="Yes"];
        validation_passed -> pull_request_draft [label="No"];
        expectations_met -> pull_request_draft [label="No"];
        pull_request_draft -> branch_update;

   }




Developers
----------

When making changes to this repository, we follow the `GitHub flow`_. For each issue,
a new branch is created, files are edited, and a pull request is created. When checks are passed,
the pull request can be merged into the `main` branch.


Issue templates
~~~~~~~~~~~~~~~

Issue templates can be edited in `.github/ISSUE_TEMPLATE`_.


GitHub actions
~~~~~~~~~~~~~~

Automated GitHub actions are defined in `.github/workflows`_.


.. _submit an issue: https://github.com/EATRIS/motbx/issues/new/choose
.. _Contact us: https://motbx.eatris.eu/contact/
.. _GitHub flow: https://docs.github.com/en/get-started/quickstart/github-flow
.. _.github/ISSUE_TEMPLATE: https://github.com/EATRIS/motbx/tree/main/.github/ISSUE_TEMPLATE
.. _.github/workflows: https://github.com/EATRIS/motbx/tree/main/.github/workflows