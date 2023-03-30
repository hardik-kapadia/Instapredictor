import instaloader

from pathlib import Path

class InstagramData:
    def __init__(self) -> None:

        self.L = instaloader.Instaloader()
        # self.L.login('chapri.slayer','CommonPassword99')

    def download_ig_profile(self, username: str, max_count: int = 30):

        try:
            profile_node = instaloader.Profile.from_username(self.L.context, username)
        except instaloader.exceptions.ProfileNotExistsException:
            raise ValueError("Profile doesn't exist")
        except instaloader.exceptions.LoginRequiredException:
            raise ValueError('Login required')

        profile_follower_count = profile_node.followers

        count = 0

        for post in profile_node.get_posts():

            if count >= max_count:
                break

            if post.is_video:
                continue

            count += 1

            post_likes = post.likes
            post_id = post.mediaid
            post_comments = post.comments
            
            # creation_time = post.date_local

            # foldername = f"{username}_{profile_follower_count}_{post_id}_{post_likes}_{post_comments}"
            path = Path('Data/'+ f"{username}_{profile_follower_count}_{post_id}_{post_likes}_{post_comments}")
            self.L.download_post(post, path)
