BranchAI python client
======================

A python native client to run queries on BranchAI pipelines.

The client is tested for python 3.8 and higher.

Visit the official `BranchAI <https://www.branch-ai.com>`_ website for more information about BranchAI and how to use it in production.


How to use
---------------------
Search
*********************
Get matching documents for query from the vector DB 

.. code-block:: python

  import branchai
  client = branchai.Client("server_url")
  results = client.with_adapter(pipeline_id).search("what ....")


Generate
*********************
Generate answer from matching documents using chatGPT

.. code-block:: python

  import branchai
  client = branchai.Client("server_url")
  answer = client.with_adapter(pipeline_id).generate("what ....")

