BranchAI python client
======================

A python native client to run queries on BranchAI pipelines.

The client is tested for python 3.8 and higher.

Visit the official `BranchAI <https://www.branch-ai.com>`_ website for more information about BranchAI and how to use it in production.


How to use
---------------------

.. code-block:: python

  import branchai
  client = branchai.client("server_url")
  results = client.with_pipeline(pipeline_id).search("what ....")

