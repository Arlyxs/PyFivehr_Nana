# import user then user.User =
from user import User  # import def instead
from post import Post

# :- Object Oriented Programming
# Create a new user
app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")

# Create a new user CodeGPT
user2 = User(
    user_email="kk@kk.com",
    name="Anna Flanashiat",
    password="secure123",
    current_job_title="AI Engineer",
)

# Create a new post
new_post = Post("om a secret mission today", {user2.name})

print(user2.add_skill("Python"))
print(user2.add_skill("Docker"))
print(app_user_one.add_skill("Slacker"))
print(user2.change_job_title("Senior DevOps Engineer"))
print(user2.get_user_info())
print(app_user_one.get_user_info())
print("**************")
print(user2.gets_user_info())
print(app_user_one.gets_user_info())
print("**************")
print(new_post.get_post_info())
