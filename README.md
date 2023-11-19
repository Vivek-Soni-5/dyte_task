# Log Ingestor and Query Interface (SDE-1 and SDE Intern Assignment)

Developed a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.\n
Both the systems (the log ingestor and the query interface) has been built using flask , HTML , CSS & Javascript.\n
I am using firebase realtime database for storing the logs and provided the credendials for your use. If you want to use your own credendials then get the cred from firebase.

## Quick Start (Steps to Run this project)

Here are some steps to run this project:

1. Clone the project ( open new terminal on your VSCode) 

```
git clone https://github.com/Vivek-Soni-5/dyte_task.git
```

2. Make Virtual Environment for this project (optional)

```
python -m venv venv
```

3. Start Virtual Environment (if setup virtual enviroment)

```
venv/Scripts/activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Run the project

```
python main.py
```

6. Open localhost in browser

```
http://localhost:3000/
```

7. To Populate the logs

```
http://localhost:3000/
```

8. To filter logs

```
http://localhost:3000/get_logs
```

8. To filter  Multiple logs

```
http://localhost:3000/multiple_log_query
```



