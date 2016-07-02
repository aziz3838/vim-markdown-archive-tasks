import os
import datetime
import vim


class ArchiveTasks():

    def __init__(self):
        # self.tasks_file = vim.current.buffer.name
        self.tasks_file = vim.current.buffer.name
        self.archive_file = os.path.splitext(self.tasks_file)[0] + \
            '_archive.markdown'

    def get_done_tasks(self):
        lines = []

        # Read all lines
        with open(self.tasks_file) as f:
            lines = f.readlines()

        # Get done tasks
        done_tasks = [task for task in lines if task.startswith('- [x]')]
        return done_tasks

    def get_today_date(self):
        today = datetime.date.today()
        # Format: November 14, 2016
        return today.strftime('%B %d, %Y')

    def remove_done_tasks(self):
        lines = []
        with open(self.tasks_file) as f:
            lines = f.readlines()
        # Filter out done tasks
        lines = filter(lambda line: not line.startswith('- [x]'), lines)
        with open(self.tasks_file, 'w') as f:
            f.writelines(lines)

    def archive_tasks(self):
        # Get new done tasks
        done_tasks = self.get_done_tasks()
        if not done_tasks:
            print 'No done tasks to be archived'
            return

        # Does archive file exist?
        archive = []
        if os.path.isfile(self.archive_file):

            # Does today's date exist in archive?
            with open(self.archive_file) as f:
                archive = f.readlines()

            # Check today's date mathces the last header
            header_exists = None
            for line in reversed(archive):
                # Get last header
                if line.startswith('## '):
                    if line.startswith('## ' + self.get_today_date()):
                        header_exists = True
                    break

            # Append new tasks
            if header_exists:
                archive.extend(done_tasks)
            else:
                archive.append('\n\n' + '## ' + self.get_today_date() + '\n\n')
                archive.extend(done_tasks)

        else:

            archive.append('# Archived Tasks' + '\n\n')
            archive.append('## ' + self.get_today_date() + '\n\n')
            archive.extend(done_tasks)

        # Write content to archive
        with open(self.archive_file, 'w') as f:
            f.writelines(archive)

        # Remove done tasks from index
        self.remove_done_tasks()
