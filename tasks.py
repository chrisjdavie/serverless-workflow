from invoke import task


@task
def deploy_cloud_function(c):

    c.run("gcloud functions deploy hello_http --runtime python37 --trigger-http --max-instances 2")
