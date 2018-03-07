# Logs Analysis
Project 3 of the **Udacity Full Stack Web Developer Nanodegree**

## About the project
Build an **internal reporting tool** that will use information from the database to discover what kind of articles the site's readers like. Create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python (2.7) program using the *psycopg2* module to connect to the database.

## How to run project
1. Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [Vagrant](https://www.vagrantup.com/downloads.html). Install the version for your operating system.
2. Clone or download the project files to your local environment
3. Start the virtual machine:
- Open your shell interface and navigate to the project directory, run the command `vagrant up`
- Run `vagrant ssh` when `vagrant up` is finished running
- Change directory to `/vagrant`
4. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip the file, put this file into the `vagrant` directory
5. Use the command `psql -d news -f newsdata.sql` to connect the database
6. Run `python logs_analysis.py` to execute the program
