CREATE TABLE users (
    username VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    user_username VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    status BIT DEFAULT 0
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_username) REFERENCES users(username)
);

CREATE TABLE streaks {
    user_username PRIMARY KEY VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (user_username) REFERENCES users(username)
}