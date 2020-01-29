from multiprocessing import Pool
from modules.github.repositories import Repositories
from config.threads import Threads
from modules.core.boot import Boot

logo = f"""
{'#' * 69}
#                                                                   #
# Indexit: Created by @Filtration                                   #
#                                                                   #
# Index it stores github repos in the database for better searches  #
#                                                                   #
{'#' * 69}
"""


class Indexit:

    # Indexit constructor
    def __init__(self):
        self.repositories = Repositories()

    # Get the repo
    def run(self, repo):

        # Don't run if already indexed
        if self.repositories.indexed(repo):
            return

        uri = "https://api.github.com/repositories/%d" % repo
        repository = self.repositories.get(uri)

        # Clone the repo
        print(repository)
        if 'html_url' in repository:
            print(repository)
            self.repositories.clone(
                repository['full_name'],
                repository['html_url']
            )

        # Run through files and store contents

    def main(self):
        #Pool connections to speed up our job
        with Pool(processes=Threads().total()) as pool:
            pool.map(self.run, range(10))

        # print(self.repos)


# Indexit logo
print(logo)

# Boot method (LEAVE ALONE)
Boot()

# Let's go!
Indexit().main()

