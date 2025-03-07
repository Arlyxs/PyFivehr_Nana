# create user Class


class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title
        self.skills = []  # Initialize empty skills list

    def change_password(self, new_password):
        self.password = new_password
        return "Password updated successfully"

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title
        return f"Job title updated to: {new_job_title}"

    def add_skill(self, new_skill):
        if new_skill not in self.skills:
            self.skills.append(new_skill)
            return f"Skill '{new_skill}' added successfully"
        return f"Skill '{new_skill}' already exists"

    def gets_user_info(self):  # CodeGPT
        return {
            "name": self.name,
            "email": self.email,
            "current_job": self.current_job_title,
            "skills": self.skills,
        }

    def get_user_info(self):
        return f"User {self.name} currently works as a {self.current_job_title}. Skills sets are: {self.skills}.  You can contact them at {self.email}"
