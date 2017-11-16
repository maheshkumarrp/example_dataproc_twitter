#MIT License
#
#Copyright (c) 2017 Willian Fuks
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

"""Main app used to send tasks into queue. This App is supposed to be accessed
by a GAE Cron job.
"""

import datetime

from flask import Flask, request
from google.appengine.api import taskqueue
from utils import process_url_date

app = Flask(__name__)

@app.route("/export_customers")
def export_customers():
    """When this method is invoked a new task is added to the queue where
    eventually data from BigQuery is exported to GCS.
    """
    date = process_url_date(request.args)
    task = taskqueue.add(url='/queue_export',
                         target='worker',
                         params={'date': date})
    return "Taks {} enqued, ETA {}".format(task.name, task.eta)