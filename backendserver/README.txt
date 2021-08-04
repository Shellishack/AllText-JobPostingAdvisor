This folder is not part of the frontend deployment.
This docker runs on a separated container to overcome the un-changable CORS settings in Azure ML deployment;
also, this docker runs Python http server while the frontend only runs nginx.