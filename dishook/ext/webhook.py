import requests, json

class webhook:

    @staticmethod
    def post_username(username, avatar_url, content, webhook):
        webhook_url  = webhook
        main_content = {
                           'username': username,
                           'avatar_url': avatar_url,
                           'content': content
                       }
        headers  = {'Content-Type': 'application/json'}
        response  = requests.post(webhook_url, json.dumps(main_content), headers=headers)