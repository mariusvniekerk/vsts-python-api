# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from msrest.pipeline import ClientRequest
from .git_client_base import GitClientBase


class GitClient(GitClientBase):
    """Git

    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(GitClient, self).__init__(base_url, creds)

    def get_vsts_info(self, relative_remote_url):
        request = ClientRequest()
        request.url = self._client.format_url(relative_remote_url.rstrip('/') + '/vsts/info')
        request.method = 'GET'
        headers = {'Accept': 'application/json'}
        if self._suppress_fedauth_redirect:
            headers['X-TFS-FedAuthRedirect'] = 'Suppress'
        response = self._send_request(request, headers)
        return self._deserialize('VstsInfo', response)

    @staticmethod
    def get_vsts_info_by_remote_url(remote_url, credentials, suppress_fedauth_redirect=True):
        request = ClientRequest()
        request.url = remote_url.rstrip('/') + '/vsts/info'
        request.method = 'GET'
        headers = {'Accept': 'application/json'}
        if suppress_fedauth_redirect:
            headers['X-TFS-FedAuthRedirect'] = 'Suppress'
        git_client = GitClient(base_url=remote_url, creds=credentials)
        response = git_client._send_request(request, headers)
        return git_client._deserialize('VstsInfo', response)

