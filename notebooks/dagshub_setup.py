import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/dharsourav03/MLOPS-MINI-PROJECT-V3.mlflow')
dagshub.init(repo_owner='dharsourav03', 
             repo_name='MLOPS-MINI-PROJECT-V3', 
             mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)