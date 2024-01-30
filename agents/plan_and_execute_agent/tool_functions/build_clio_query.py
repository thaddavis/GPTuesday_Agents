def build_clio_query(input: str) -> str:
    print("Enter BuildClioQuery tool...")

    return """TLDR:
Convert a natural language PROMPT to a valid SQL query.


EXAMPLES:
What tasks are overdue as of 11-9-2023 and which employees are responsible for following up on them?
SELECT t.id, t.description, e.id, e.name FROM tasks t JOIN employees e ON t.assignee_id = e.id WHERE t.due_at < '2023-09-11';

What tasks are overdue as of 11-9-2023 and which employees are responsible for following up on them?
SELECT t.id AS task_id, t.name AS task_name, t.due_at AS due_date, e.id AS employee_id, e.name AS employee_name FROM tasks t JOIN employees e ON t.assignee_id = e.id WHERE t.due_at < '2023-11-09' AND t.status != 'completed';

What are 10 overdue tasks as of 11-9-2023 and which employees are responsible for following up on them?
SELECT t.id, t.description, e.id AS employee_id, e.name AS employee_name FROM tasks t JOIN employees e ON t.assignee_id = e.id WHERE t.due_at < '2023-11-09' AND t.status != 'completed' ORDER BY t.due_at ASC LIMIT 10;

List 10 matters in Clio along with their creation dates
SELECT description, open_date FROM public.matters ORDER BY open_date LIMIT 10;

List the 10 most recent matters in Clio along with their creation dates
SELECT description, open_date FROM public.matters ORDER BY open_date DESC LIMIT 10;

List the 10 most recent matters in Clio along with their id and creation dates
SELECT id, description, open_date FROM public.matters ORDER BY open_date DESC LIMIT 10;

List all the tasks related to the matter #4813
SELECT * FROM tasks WHERE matter_id = 4813;

List all the tasks related to the matter #4813. Include the Assignee and Assigner name.
SELECT t.id, t.name, t.description, t.status, assigner.name as assigner, assignee.name as assignee, t.created_at, t.updated_at FROM tasks t JOIN matters m ON  m.id = t.matter_id JOIN employees assigner ON assigner.id = t.assigner_id JOIN employees assignee ON assignee.id = t.assignee_id WHERE m.id = 4813;

List 10 matters and the client they are associated with.
SELECT m.id as "Matter ID", m.description, c.name FROM public.matters AS m JOIN public.contacts AS c ON m.client_id = c.id WHERE c.is_client = TRUE LIMIT 10;

What are 100 tasks overdue as of today (11-9-2023)?
SELECT * FROM tasks t WHERE t.due_at < '2023-11-09' ORDER BY t.due_at LIMIT 100;

List 100 tasks overdue as of today (11-9-2023)? Include the task's id, status, priority, name, and due_date formatted as TOML.
SELECT id, status, priority, name, due_at FROM tasks WHERE due_at < '2023-09-11' AND status != 'complete' ORDER BY due_at ASC LIMIT 100;

List 10 tasks overdue as of today (11-9-2023)? Include the task's id, status, priority, name, and due_date
SELECT id, status, priority, name, due_at AS due_date FROM tasks WHERE due_at < '2023-11-09' AND status != 'completed' ORDER BY due_at ASC LIMIT 10;

List all the tasks associated with allan young's matters
SELECT t.id, t.name, t.description, t.status FROM tasks t JOIN matters m ON m.id = t.matter_id JOIN contacts c ON m.client_id = c.id WHERE c.name = 'allan young';

List all the tasks associate with Barbara J Hennessy's matter
SELECT t.id, t.name, t.description, t.status FROM tasks t JOIN matters m ON m.id = t.matter_id JOIN contacts c ON m.client_id = c.id WHERE c.name = 'barbara j hennessy';

List all the tasks associate with barbara j hennessy's matter
SELECT t.id, t.name, t.description, t.status FROM tasks t JOIN matters m ON m.id = t.matter_id JOIN contacts c ON m.client_id = c.id WHERE c.name = 'barbara j hennessy';

List all the tasks associated with gaylen evans's matter
SELECT t.* FROM tasks AS t JOIN matters AS m ON t.matter_id = m.id JOIN contacts AS c ON m.client_id = c.id WHERE c.name = 'gaylen evans';

List all the tasks associated with lince munoz's matters
SELECT t.* FROM tasks AS t JOIN matters AS m ON t.matter_id = m.id JOIN contacts AS c ON m.client_id = c.id WHERE c.name = 'lince munoz';

List all the tasks associated with eugene ball's matters
SELECT tasks.* FROM tasks INNER JOIN matters m ON tasks.matter_id = m.id WHERE m.client_id IN (SELECT id FROM contacts WHERE name = 'eugene ball');

List all the tasks associated with mercedes santos's matters
SELECT tasks.* FROM tasks JOIN matters ON tasks.matter_id = matters.id JOIN contacts ON matters.client_id = contacts.id WHERE LOWER(contacts.name) = 'mercedes santos';

List all the tasks associated with merritt pember's matters
SELECT tasks.* FROM tasks JOIN matters ON tasks.matter_id = matters.id JOIN contacts ON matters.client_id = contacts.id WHERE LOWER(contacts.name) = 'merritt pember';

List all the tasks associated with the contact kevin vazquez's matters
SELECT t.id, t.description FROM tasks t INNER JOIN matters m ON t.matter_id = m.id INNER JOIN contacts c ON m.client_id = c.id WHERE c.name = 'kevin vazquez';

List all the tasks associated with the contact kevin vazquez's matters
SELECT tasks.id, tasks.name, tasks.description, tasks.status, tasks.priority, tasks.due_at, tasks.assignee_id,  matters.id AS matter_id FROM tasks JOIN matters ON tasks.matter_id = matters.i JOIN contacts ON matters.client_id = contacts.id WHERE contacts.name = 'kevin vazquez';

List 20 matters and the contacts associated with them ordered from newest to oldest:
SELECT matters.*, contacts.* FROM matters JOIN contacts ON matters.client_id = contacts.id ORDER BY matters.open_date DESC LIMIT 20;

Here are 20 matters and the contacts associated with them, ordered from newest to oldest. Include relevant dates with each matter.
SELECT m.description, m.open_date, m.last_contact, m.last_docket_review, m.last_activity, c.name FROM matters AS m JOIN contacts AS c ON m.client_id = c.id ORDER BY m.open_date DESC LIMIT 20;

Return what tasks are overdue as of 11-9-2023 and which employees are responsible for following up on them? Limit the matches to 16.
ELECT t.id AS task_id, t.name AS task_name, t.due_at AS due_date, e.id AS employee_id, e.name AS employee_name FROM tasks t INNER JOIN employees e ON t.assignee_id = e.id WHERE t.due_at < '2023-11-09' AND t.status != 'completed' LIMIT 16;

Return what tasks are overdue as of 11-9-2023 and which employees are responsible for following up on them? Limit the matches to 16. Order the tasks by due date from oldest to newest.
SELECT t.id AS task_id, t.name AS task_name, t.due_at AS due_date, e.id AS employee_id, e.name AS employee_name FROM tasks t INNER JOIN employees e ON t.assignee_id = e.id WHERE t.due_at < '2023-11-09' AND t.status != 'completed' ORDER BY t.due_at ASC LIMIT 16;

What are all the matters that employee jenny consuegra is assigned to?
SELECT m.* FROM matters m JOIN tasks t ON m.id = t.matter_id JOIN employees e ON t.assignee_id = e.id WHERE LOWER(e.name) = 'jenny consuegra';

Which employees are assigned to Martinez, Elie vs Guzman, Elizabeth a?
SELECT e.id, e.name FROM employees e JOIN tasks t ON e.id = t.assignee_id JOIN matters m ON t.matter_id = m.id WHERE LOWER(m.description) = 'martinez, elie vs guzman, elizabeth a';

Which employees are assigned to the matter with description 'Martinez, Elie vs Guzman, Elizabeth a'?
SELECT e.id, e.name FROM employees e JOIN tasks t ON e.id = t.assignee_id JOIN matters m ON t.matter_id = m.id WHERE LOWER(m.description) = 'martinez, elie vs guzman, elizabeth a';

Which employees are assigned to Aurelien, Eddy Junior vs Etienne, Manuella?
SELECT e.id, e.name FROM employees e JOIN tasks t ON e.id = t.assignee_id JOIN matters m ON t.matter_id = m.id WHERE LOWER(m.description) = 'aurelien, eddy junior vs etienne, manuella';

What are all the matters related to Mashal Ahmed?
SELECT matters.* FROM matters INNER JOIN contacts ON matters.client_id = contacts.id WHERE LOWER(contacts.name) = 'mashal ahmed';

Today is 11-9-2023. What tasks are overdue related to the matter with description 'Bouvy, Ralph vs Khayat, Tarek El'?
SELECT tasks.* FROM tasks JOIN matters ON tasks.matter_id = matters.id WHERE tasks.due_at < '2023-11-09' AND LOWER(matters.description) = 'bouvy, ralph vs khayat, tarek el' AND tasks.status != 'completed';

List 20 matters and the clients they are each associated with
SELECT m.id as "Matter ID", m.description as "Matter Description", c.name as "Client Name" FROM public.matters AS m JOIN public.contacts AS c ON m.client_id = c.id WHERE c.is_client = TRUE ORDER BY m.open_date DESC LIMIT 20;

Are there any tasks related to David R Gonzales's matter?
SELECT * FROM tasks WHERE matter_id IN (SELECT id FROM matters WHERE description = 'State Of Florida vs David R Gonzales');

Are there any tasks related to 'State Of Florida vs David R Gonzales'?
SELECT * FROM tasks WHERE matter_id IN (SELECT id FROM matters WHERE description = 'State Of Florida vs David R Gonzales');

Are there any tasks related to the matter with description 'State Of Florida vs David R Gonzales'?
SELECT * FROM tasks WHERE matter_id IN (SELECT id FROM matters WHERE description = 'State Of Florida vs David R Gonzales');

Get all Miranda Lukasik's matters.
SELECT m.* FROM matters m JOIN contacts c ON m.client_id = c.id WHERE LOWER(c.name) = 'miranda lukasik';

Get all contact Miranda Lukasik's matters.
SELECT m.* FROM matters m JOIN contacts c ON m.client_id = c.id WHERE LOWER(c.name) = 'miranda lukasik';

Get all matters related to the contact named Miranda Lukasik.
SELECT m.* FROM matters m JOIN contacts c ON m.client_id = c.id WHERE LOWER(c.name) = 'miranda lukasik';

Get all Miranda Lukasik's matter and related tasks.
SELECT M.*, T.* FROM contacts C JOIN matters M ON C.id = M.client_id LEFT JOIN tasks T ON M.id = T.matter_id WHERE LOWER(C.name) = 'miranda lukasik';

Get all matters and tasks related to the contact named Miranda Lukasik
SELECT M.*, T.* FROM contacts C JOIN matters M ON C.id = M.client_id LEFT JOIN tasks T ON M.id = T.matter_id WHERE LOWER(C.name) = 'miranda lukasik';

List all matters and tasks related to the contact named Miranda Lukasik
SELECT M.*, T.* FROM contacts C JOIN matters M ON C.id = M.client_id LEFT JOIN tasks T ON M.id = T.matter_id WHERE LOWER(C.name) = 'miranda lukasik';


SCHEMA_DESCRIPTION:
create table contacts (
    id serial PRIMARY KEY,
    is_client BOOLEAN NOT NULL,
    prefix VARCHAR(50),
    name VARCHAR(100) NOT NULL,
    primary_email_address VARCHAR(100),
    primary_phone_number VARCHAR(50),
    created_at DATE NOT NULL,
    initials VARCHAR(10) NOT NULL,
    clio_connect_email VARCHAR(100),
    secondary_email_address  VARCHAR(100),
    secondary_phone_number VARCHAR(50),
    clio_id INT NOT NULL UNIQUE
);
create table matters (
    id serial PRIMARY KEY,
    status VARCHAR(20) NOT NULL,
    practice_area TEXT,
    display_number VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    last_contact DATE NULL,
    last_docket_review DATE NULL,
    last_activity DATE NULL,
    open_date DATE,
    pending_date DATE NULL,
    close_date DATE NULL,
    county_raw VARCHAR(100) NULL, 
    county_parsed VARCHAR(100) NULL,
    case_number_raw VARCHAR(100) NULL, 
    case_number_parsed VARCHAR(100) NULL,
    client_id INT REFERENCES contacts(id),
    clio_id INT UNIQUE
);
create table users (
   id serial PRIMARY KEY,
   enabled boolean,
   name VARCHAR(100) NOT NULL,
   email VARCHAR(100) NOT NULL,
   subscription_type VARCHAR(100) NOT NULL, 
   clio_id INT NOT NULL UNIQUE
);
create table tasks (
   id serial PRIMARY KEY,
   status VARCHAR(30) NOT NULL,
   priority VARCHAR(30) NOT NULL,
   name TEXT NOT NULL,
   due_at DATE,
   description TEXT,
   assignee_id INT REFERENCES users(id),
   assigner_id INT REFERENCES users(id),
   matter_id INT REFERENCES matters(id),
   created_at timestamp,
   updated_at timestamp,
   completed_at timestamp,
   clio_id INT UNIQUE
);
create table calendar_entries (
   id serial PRIMARY KEY,
   etag VARCHAR(100) NOT NULL,
   summary TEXT NOT NULL,
   description TEXT NOT NULL,
   location TEXT NOT NULL,
   start_at TIMESTAMP,
   end_at TIMESTAMP,
   all_day BOOLEAN NOT NULL,
   created_at TIMESTAMP,
   updated_at TIMESTAMP,
   start_at_time_zone VARCHAR(100) NOT NULL,
   matter_id INT REFERENCES matters(id),
   clio_id VARCHAR(100) NOT NULL
);


REQUIREMENTS:
- make sure the column names for each referenced table in the generated SQL query are valid according to the SCHEMA_DESCRIPTION
- there are 5 tables in the SCHEMA_DESCRIPTION: 'tasks', 'users', 'matters', 'contacts', and 'calendar_entries'
- the exact column names for the tasks table in the SCHEMA_DESCRIPTION are: tasks.id, tasks.status, tasks.priority, tasks.name, tasks.due_at, tasks.description, tasks.assignee_id, tasks.assigner_id, tasks.matter_id, tasks.created_at, tasks.updated_at, tasks.completed_at
- the exact column names for the users table in the SCHEMA_DESCRIPTION are: users.id, users.enabled, users.name, users.email, users.subscription_type
- the exact column names for the matters table in the SCHEMA_DESCRIPTION are: matters.id, matters.status, matters.practice_area, matters.display_number, matters.description, matters.last_contact, matters.last_docket_review, matters.last_activity, matters.open_date, matters.pending_date, matters.close_date, matters.client_id
- the exact column names for the contacts table in the SCHEMA_DESCRIPTION are: contacts.id, contacts.is_client, contacts.prefix, contacts.name, contacts.primary_email_address, contacts.primary_phone_number, contacts.created_at, contacts.initials character, contacts.clio_connect_email, contacts.secondary_email_address, contacts.secondary_phone_number
- the exact column names for the calendar_entries table in the SCHEMA_DESCRIPTION are: calendar_entries.id, calendar_entries.etag, calendar_entries.summary, calendar_entries.description, calendar_entries.location, calendar_entries.start_at, calendar_entries.end_at, calendar_entries.all_day, calendar_entries.created_at, calendar_entries.updated_at, calendar_entries.start_at_time_zone,  calendar_entries.matter_id
- the users table holds all the users registered as employees in Clio
- there is not a table named 'clients' in the schema
- build a valid SQL query based on the SCHEMA_DESCRIPTION that can be executed against a live database that answers the following PROMPT: {input}
- If the prompt refers to an entity which is not uniquely identifiable then ask the prompter to clarify the full name
- If the prompt refers to an entity which is likely misspelled then ask the prompter to clarify the full name
""".format(
        input=input
    )
