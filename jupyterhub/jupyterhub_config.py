c.JupyterHub.bind_url = "http://0.0.0.0:8000"
c.Authenticator.admin_users = {"admin"}
c.Authenticator.allowed_users = {"admin"}
c.DummyAuthenticator.password = "admin"
c.JupyterHub.authenticator_class = "dummy"
c.Spawner.cmd = ["/usr/local/bin/jupyterhub-singleuser"]
