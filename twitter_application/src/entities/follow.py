import uuid


class Follow:
    def __init__(self, follow_id=None, follower=None, following=None, send_time=None):
        self.id = follow_id or str(uuid.uuid4())
        self.follower = follower
        self.following = following
        self.send_time = send_time
